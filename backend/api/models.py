from django.db import models
import os
from django.db.models.fields.related import ForeignKey
from pytz import timezone   #한국시간 넣기

# database 만들기


# 고객
class User(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    password = models.CharField(max_length=500)
    userName = models.CharField(max_length = 50)
    accCnt = models.IntegerField()
    cash = models.IntegerField()
    phoneNumber = models.CharField(max_length=50)

    def __str__(self):
        return f'id : {self.id} | password: {self.password} | userName : {self.userName} | accCnt : {self.accCnt} | cash : {self.cash} | phoneNumber : {self.phoneNumber}'


# 계좌
class Account(models.Model):
    aId = models.AutoField(primary_key = True)                  # 계좌 PK
    accNum = models.IntegerField(unique=True)                   # 계좌 번호
    password = models.IntegerField()                            # 계좌 비밀번호
    balance = models.IntegerField()                             # 돈
    ownerId = models.CharField(max_length=20)                   # 보유자 아이디
    ownerName = models.CharField(max_length = 50)               # 보유자 이름
    title = models.IntegerField()                               # 대표 계좌 유무
    card = models.CharField(max_length = 50, null = True)


    def __str__(self):
        return f'accNum : {self.accNum}  | balance : {self.balance} |'
    


# 거래내역
class TranInfo(models.Model):
    tId = models.AutoField(primary_key=True)
    send_accNum = models.CharField(max_length=20)
    send_name = models.CharField(max_length = 20)
    receive_accNum = models.CharField(max_length=20)
    receive_name = models.CharField(max_length = 20)
    money = models.IntegerField()
    trade_date = models.CharField(max_length = 20)
    trade_time = models.CharField(max_length = 20)
    comment = models.TextField(null = True)

    def __str__(self):
        return f'name : {self.send_name} | aNumber : {self.send_accNum} => name : {self.receive_name} | account_number : {self.receive_accNum} | money : {self.money} | date : {self.trade_date}'


# 상품몰
class Advertising(models.Model):
    aId = models.AutoField(primary_key=True)
    aName = models.CharField(max_length = 100)
    title = models.CharField(max_length = 500)
    contents = models.TextField(null= True)
    img = models.CharField(max_length = 100)

    def __str__(self):
        return f'aName : {self.aName}'

