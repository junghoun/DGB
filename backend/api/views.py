#기본 import
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response    # 응답하기
from django.http import JsonResponse    # Json으로 값 넘겨주기
from rest_framework import status       # response의 예외처리
from datetime import datetime, timedelta

from rest_framework.serializers import Serializer    # datetime : 시간관련 계산 / timedelta : 시간/날짜 빼기
from .serializers import UserSerializer, AccountSerializer, AdvertisingSerializer
from .models import User, Account, Advertising
from django.db.models import Q       # 2개 이상 인자 비교해서 값 얻을 때 사용

#token 관련 import
from backend.settings import SECRET_KEY
import jwt, bcrypt      # jwt : django에서 jwt사용하기 / bcrypt : 비밀번호 암호화


# query문 사용할 수 있게 cursor 등록
import sqlite3
conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()



# 고객 token 관리
def token_vaild(request):
    access_token = request.headers['token']
    payload = jwt.decode(access_token, SECRET_KEY, algorithm='HS256')
    user = User.objects.get(id=payload['id'])
    return user


# 로그인
@api_view(['POST'])
def user_login(request):
    try:
        user = User.objects.get(pk=request.data['id'])
        if not bcrypt.checkpw(request.data['password'].encode('utf-8'), user.password.encode('utf-8')):
            print("     Password Fail\n")
            return JsonResponse({'token' : "null", 'message' : "pw_fail"}, status = status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        print("     Login Fail\n")
        return JsonResponse({'token' : 'NULL', 'message' : "id_fail"}, status = status.HTTP_400_BAD_REQUEST)

    token = jwt.encode({'id' : request.data['id'], 'exp' : datetime.utcnow() + timedelta(seconds=1800)} ,SECRET_KEY, algorithm = "HS256") # timedelta 인자 : seconds, hours, days, weeks
    token = token.decode('utf-8')


    day = datetime.now().strftime('%Y-%m-%d')
    print(day)

    print("     Login Success\n")

    return JsonResponse({'token' : token, 'message' : "success", 'user_id' : user.id}, status = status.HTTP_200_OK)


# 회원가입 
@api_view(['POST'])
def user_join(request):

    password = request.data['password'].encode('utf-8')
    password_crypt = bcrypt.hashpw(password, bcrypt.gensalt())  # 암호 복호화
    password_crypt = password_crypt.decode('utf-8')
    request.data['password'] = password_crypt
    
    print("========================");
    serializer = UserSerializer(data=request.data)

    print(serializer.is_valid());
    print(serializer);

    if serializer.is_valid():
        # 로그인 성공
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        # 로그인 실패
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# 고객 정보(확인 / 수정)
@api_view(['GET', 'PUT'])
def user_info(request):

    user = token_vaild(request)
    
    if request.method =='GET':
        # 고객 정보 전체 보내주기
        queryset = User.objects.get(id=user.id)
        serializer = UserSerializer(queryset)

        return Response(serializer.data)
    else:
        # 임시로 이름으로 확인
        user.name = request.data['name']
        # 고객 정보 바꿀 것 바꾸기
        user.save();
        return Response(status=status.HTTP_200_OK)




##################### 첫 페이지 관련 값 가져오기

# 1. 내 계좌 수 가져오기

@api_view(['GET'])
def count(request) :
    user = token_vaild(request)


    cnt = Account.objects.filter(ownerId = user.id).count()

    print(cnt);
    return Response({"count" : cnt});


# 2. 계좌 모두 가져오기 (type 1 : 대표계좌 들고오기 / type 2 : 전체 다 들고 오기)

@api_view(['GET'])
def myaccount(request) :

    user = token_vaild(request)

    type = request.query_params.get("type")
    print("type = " + type);
    if type == "1" :
        query = Account.objects.get(Q(ownerId = user.id) & Q(title = 1));

        serializer = AccountSerializer(query)
        return Response(serializer.data)
        
    else :

        sql = "select * from api_account "
        queryset = Account.objects.filter(ownerId = user.id).order_by('-title')
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)



# 원하는 계좌 정보 가져오기

@api_view(['GET'])
def findaccount(request) :

    value = request.query_params.get("value")

    if value.isdigit() :
        value = int(value)
        queryset = Account.objects.filter(Q(accNum = value));
    else :
        queryset = Account.objects.filter(Q(ownerName = value));

    print(queryset)

    serializer = AccountSerializer(queryset, many=True)
    return Response(serializer.data)

# 해당 계좌 가져오기

@api_view(['GET'])
def oneaccount(request) :

    value = request.query_params.get("value")

    query = Account.objects.get(accNum = value)

    serializer = AccountSerializer(query);

    return Response(serializer.data)




# 송금한 결과 값 양쪽에 반영하기
@api_view(['PUT'])
def tradefinish(request):
    
    value = int(str(request.data['money']))
    
    sql = "update api_account set balance = balance - " + str(value) + " where accNum = " + str(request.data['sender'])

    print(sql)

    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute(sql)

    conn.commit()

    sql = "update api_account set balance = balance + " + str(value) + " where accNum = " + str(request.data['receiver'])

    print(sql)

    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute(sql)

    conn.commit()

    return Response(status=status.HTTP_201_CREATED)


## 거래내역 저장하기
@api_view(['PUT'])
def addtrade(request):

    value = int(str(request.data['money']))

    sendAcc = Account.objects.get(accNum = str(request.data['sender']));
    receiveAcc = Account.objects.get(accNum = str(request.data['receiver']));
    print("###############################")
    print(datetime.now())
    print("###############################")
    date = str(datetime.now())[:10]
    time = str(datetime.now())[12:19]

    sql = "insert into api_traninfo (send_accNum, send_name, receive_accNum, receive_name, money, trade_date, trade_time) values ( " + str(sendAcc.accNum) + ", '" + str(sendAcc.ownerName) + "', " + str(receiveAcc.accNum) + ", '" + str(receiveAcc.ownerName) + "', " + str(value) + ", '" + str(date) + "', '" + str(time) + "')"; 

    print(sql)

    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute(sql)

    conn.commit()

    return Response(status=status.HTTP_201_CREATED)

## 일주일 사용금액 가져오기
@api_view(['GET'])
def getweek(request):

    accNum = request.query_params.get("value")

    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    
    result = []
    
    for i in range(6, -1, -1) :
        sql = "select IFNULL(sum(money), 0) from api_traninfo where trade_date like date('now', '-" + str(i) + " days') and send_accNum = '" + str(accNum) + "'"
        cursor.execute(sql)
        cnt = cursor.fetchone()
        result.append(cnt[0])
        

    pre = (datetime.today()-timedelta(6)).strftime("%Y-%m-%d")
    today = datetime.today().strftime("%Y-%m-%d")
    results = [result, pre, today]
    
    return Response(results)


## 입/출금 기록하기
@api_view(['PUT'])
def record(request):
    money = int(str(request.data['money']))
    type = int(str(request.data['type']))
    accNum = int(str(request.data['accNum']))
    account = Account.objects.get(accNum = accNum);
    user = User.objects.get(id = account.ownerId);

    print("record 시작");

    ## 1. 입금(cash 빠지고, 계좌에 돈 들어가고)
    if type == 1 : 
        cash = user.cash
        user.cash = cash - money;
        user.save();

        cash = account.balance;
        account.balance = cash + money;
        account.save();
        
        date = str(datetime.now())[:10]
        time = str(datetime.now())[12:19]

        sql = "insert into api_traninfo (send_accNum, send_name, receive_accNum, receive_name, money, trade_date, trade_time) values ( 508220789200, '스마트ATM', " + str(account.accNum) + ", '" + str(account.ownerName) + "', " + str(money) + ", '" + str(date) + "', '" + str(time) + "')"; 


        print(sql)
        conn = sqlite3.connect("db.sqlite3")
        cursor = conn.cursor()
        cursor.execute(sql)

        conn.commit()



    ## 2. 출금(계좌에서 빠지고, cash에 들어가고)
    else :
        cash = user.cash
        user.cash = cash + money;
        user.save();

        cash = account.balance;
        account.balance = cash - money;
        account.save();

        date = str(datetime.now())[:10]
        time = str(datetime.now())[12:19]

        sql = "insert into api_traninfo (send_accNum, send_name, receive_accNum, receive_name, money, trade_date, trade_time) values ( " + str(account.accNum) + ", '" + str(account.ownerName) + "', 508220789200, '스마트ATM', " + str(money) + ", '" + str(date) + "', '" + str(time) + "')"; 

        print(sql)

        conn = sqlite3.connect("db.sqlite3")
        cursor = conn.cursor()
        cursor.execute(sql)

        conn.commit()

    return Response(status=status.HTTP_201_CREATED)



# 광고 정보 가져오기

@api_view(['GET'])
def alladver(request) :


    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    sql = "select * from api_advertising;"

    cursor.execute(sql)

    alls = cursor.fetchall()

    columns = [column[0] for column in cursor.description]
    results = []
    for row in alls:
        results.append(dict(zip(columns, row)))

    return Response(results)


# 광고 조회
@api_view(['GET'])
def getadver(request) :

    aName = request.query_params.get("value")

    adver = Advertising.objects.get(aName = aName)

    serializer = AdvertisingSerializer(adver)

    return Response(serializer.data)



## 최근 거래내역 5개 가져오기

@api_view(['GET'])
def tradefive(request):

    accNum = request.query_params.get("value")

    sql = "select (case when(send_accNum == '" + accNum + "') then receive_name else send_name end) as 'name', money, (case when(send_accNum == '"+ accNum +"') then '0' else '1' end) as 'type', (case when(send_accNum == '"+ accNum +"') then '출금' else '입금' end) as 'type', trade_date, (julianday(date('now')) - julianday(trade_date)) as minus from api_traninfo where (send_accNum == '" + accNum  +"' or receive_accNum == '" + accNum +"') order by trade_date desc, trade_time desc limit 5;"

    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    

    cursor.execute(sql)

    results = cursor.fetchall()
    
    print(results)

    return Response(results)


## 날짜 가져오기
@api_view(['GET'])
def date(request):

    value = request.query_params.get("value")

    now = datetime.now()

    pre = now + timedelta(days=-(int)(value));

    now = now.strftime('%Y-%m-%d')
    pre = pre.strftime('%Y-%m-%d')
    
    print(now)
    print(pre)
    
    results = [pre, now]

    return Response(results)


## 거래내역 다 들고오기
@api_view(['GET'])
def recordlist(request):

    accNum = request.query_params.get("accNum")
    day = (int)(request.query_params.get("day"))


    
    sql = "select (case when(send_accNum == '" + accNum + "') then receive_name else send_name end) as 'name', money, (case when(send_accNum == '"+ accNum +"') then '0' else '1' end) as 'type', (case when(send_accNum == '"+ accNum +"') then '출금' else '입금' end) as 'type', trade_date, (julianday(date('now')) - julianday(trade_date)) as minus from api_traninfo where (send_accNum == '" + accNum  +"' or receive_accNum == '" + accNum +"') and trade_date BETWEEN date('now', '-"+str(day)+" days') and date('now') order by trade_date desc, trade_time desc;"

    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    #print(sql)

    cursor.execute(sql)

    result = cursor.fetchall()
    
    sql = "select count(*) from api_traninfo where (send_accNum == '" + accNum  +"' or receive_accNum == '" + accNum +"') and trade_date BETWEEN date('now', '-"+str(day)+" days') and date('now') order by trade_date desc, trade_time desc;"

    cursor.execute(sql)
    cnt = cursor.fetchone()[0]

    print(cnt)
    
    

    

    return Response({"results" : result, "cnt" : cnt})



# 계좌 추가하기
@api_view(['POST'])
def addaccount(request) :

    
    type = request.data['type']

    if type == 1:
        user = token_vaild(request)
        print(user)

    password = request.data['password']

    sql = "select accNum from api_account order by accNum desc limit 1;"

    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()

    print(sql)

    cursor.execute(sql)

    acc = cursor.fetchone()[0] + 123

    if type == 1:

        sql = "select count(*) from api_account where ownerId = '"+ str(user.id)+"' and title = 1";

        cursor.execute(sql)

        cnt = cursor.fetchone()[0]

        if cnt == 0 :
            sql = "insert into api_account (accNum, password, balance, ownerId, ownerName, title) values ('"+ str(acc) +"', " + str(password) + ", 0, '"+ str(user.id)+"', '"+ str(user.userName)+"', 1)"
        else:
            sql = "insert into api_account (accNum, password, balance, ownerId, ownerName, title) values ('"+ str(acc) +"', " + str(password) + ", 0, '"+ str(user.id)+"', '"+ str(user.userName)+"', 0)"

        
    

    print(sql)
    cursor.execute(sql)

    conn.commit()

    return Response(True)





## 대표계좌 변경
@api_view(['PUT'])
def change(request) :

    user = token_vaild(request);

    accNum = request.data['accNum']

    serializer = Account.objects.get(Q(ownerId = user.id) & Q(title = 1));

    serializer.title = 0

    serializer.save()
    change = Account.objects.get(accNum = accNum)

    change.title = 1;

    change.save()

    return Response(True)