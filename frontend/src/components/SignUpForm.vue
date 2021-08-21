<template>
  <div id="app" class="app">
    <div>
      <div class="card">
        <h1 class="card-title">Sign Up</h1>
        <v-form ref="form" v-model="valid" style="font-family:'Jua';">
          사용자이름
          <v-text-field
            placeholder="이름을 입력해주세요."
            name="userName"
            prepend-icon="person"
            v-model="userName"
            type="text"
            color="teal accent-3"
            :rules="[rules.required]"
          />
          아이디
          <v-text-field
            name="id"
            prepend-icon="person"
            v-model="id"
            placeholder="ID를 입력하세요."
            type="text"
            color="teal accent-3"
            @keyup.enter="onlogin"
            :rules="[rules.required]"
          />
          비밀번호
          <v-text-field
            name="Password"
            prepend-icon="lock"
            v-model="password"
            placeholder="비밀번호를 입력하세요."
            type="Password"
            color="teal accent-3"
            @keyup.enter="onlogin"
            :rules="[rules.required, rules.min]"
          />
          <v-text-field
            name="PasswordCheck"
            prepend-icon="lock"
            v-model="passwordCheck"
            placeholder="비밀번호 확인."
            type="Password"
            color="teal accent-3"
            @keyup.enter="onlogin"
            :rules="[rules.required, rules.min, rules.check]"
          />
          전화번호
          <v-text-field
            name="phoneNumber"
            prepend-icon="call"
            v-model="phoneNumber"
            type="Number"
            placeholder="000-0000-0000"
            color="teal accent-3"
            @keyup.enter="onlogin"
            :rules="[rules.required]"
          ></v-text-field>
          현금 보유
          <v-text-field
            name="cash"
            prepend-icon="money"
            v-model="cash"
            placeholder="0"
            color="teal accent-3"
            @keyup.enter="onlogin"
          ></v-text-field>
        </v-form>
        <br />
        
        <menu class="field-actions">
          <v-btn
            :disabled="!valid"
            color="cyan"
            class="field-submit"
            @click="validate"
            >Sign Up</v-btn
          >
        </menu>
      </div>
      <div class="instructions" style="font-family:'Jua';">
        간단한 <code>회원정보</code> 입력으로 회원가입하세요.
      </div>
    </div>
    
  </div>
  
</template>
<script>
import { registerUser } from "@/api/auth";
export default {
  data() {
    return {
      valid: true,
      id: "",
      password: "",
      passwordCheck : "",
      userName: "",
      phoneNumber: "",
      cash: 0,
      login: {
        id: "",
        password: "",
      },
      
      rules: {
        required: (value) => !!value || "필수 입력사항입니다.",
        min: (v) =>
          /^(?=.*[a-z])(?=.*[0-9]).{8,30}$/.test(v) ||
          "영문,숫자 포함 8 자리이상 이어야 합니다.",
        check: () => (this.password === this.passwordCheck) || "동일한 비밀번호를 입력해 주세요."
      },
    };
  },
  methods: {
    

    validate() {
      this.$refs.form.validate();
      this.onJoin();
    },
    async onJoin() {
      let userData = {
        id: this.id,
        password: this.password,
        userName: this.userName,
        accCnt : 0,
        cash: this.cash,
        phoneNumber: this.phoneNumber
      };
      console.log("회원가입정보:" + userData);
      try {
        console.log(userData);
        const { data } = await registerUser(userData);
        console.log(data);
        alert("회원가입 성공");
        this.$router.push("/login");
      } catch (error) {
        //console.log(error);
        alert("이미 가입된 아이디입니다.");
      } finally {
        this.initForm();
      }
    },
    initForm() {
      this.$refs.form.reset();
      this.id = "";
      this.password = "";
    },
    gojoin() {
      this.$router.push("/login");
    },
  },
};
</script>
<style scoped>

.app {
  
  margin-top : 100px;
  


}

body {
  background-color: #faecef;
  color: #154271;
  font-family: "nudista-web", sans-serif;
  font-weight: 600;
  margin: 0;
}
.card {
  background-color: white;
  border-radius: 16px;
  box-shadow: 24px 24px 60px rgba(81, 53, 115, 0.3);
  margin-bottom: 2em;
  margin-left: auto;
  margin-right: auto;
  margin-top: 2em;
  padding: 2.5em;
  width: 20em;
}

.card-title {
  font-size: 2.5em;
  font-weight: 700;
  margin-bottom: 0;
  margin-top: 0.25em;
}

.card-title::after {
  background-color: currentColor;
  content: "";
  display: block;
  height: 0.25em;
  margin-bottom: 1em;
  margin-top: 0.25em;
  width: 2em;
}

/* Field */

.field-actions {
  display: block;
  margin-bottom: -2.5em;
  margin-left: -2.5em;
  margin-right: -2.5em;
  margin-top: 3.5em;
  padding: 0;
}

.field-feedback {
  font-size: 0.7579em;
  height: 2em;
  padding-top: 0.5em;
  text-transform: uppercase;
}

.field-label {
  display: block;
  font-size: 1em;
  line-height: 1.5em;
  margin: 0;
  padding-bottom: 2px;
  padding-right: 32px;
  padding-top: 0.5em;
  position: relative;
}

.field-input {
  background-color: #f9f6f6;
  border: none;
  box-shadow: 0 2px #dcd7d7;
  color: #154271;
  display: block;
  font-size: 1.125em;
  margin-bottom: 0;
  margin-left: 0;
  margin-right: 0;
  margin-top: 0.375em;
  outline: none;
  padding: 0.75em 0.75em;
  transition: box-shadow 200ms;
  width: calc(100% - 32px);
}

.field-input-focus {
  background-color: #154271;
  bottom: 0;
  height: 2px;
  left: 0;
  pointer-events: none;
  position: absolute;
  transform: scaleX(0);
  transition: transform 200ms cubic-bezier(0.4, 0, 0.2, 1);
  width: calc(100% - 32px);
}

.field-submit {
  appearance: none;
  background-color: #55f1be;
  border-bottom-left-radius: 16px;
  border-bottom-right-radius: 16px;
  border: none;
  color: white;
  cursor: pointer;
  display: block;
  font-family: "nudista-web", sans-serif;
  font-size: 1.3195em;
  font-weight: 600;
  outline: none;
  padding-bottom: 1em;
  padding-top: 1em;
  text-align: center;
  transition: background-color 200ms;
  width: 100%;
}

.field-submit:focus,
.field-submit:hover {
  background-color: #21cfbf;
}

/* Instructions */

.instructions {
  margin-left: auto;
  margin-right: auto;
  margin-top: 2em;
  opacity: 0.3;
  text-align: center;
  width: 20em;
}

.instructions code {
  font-size: 1.1487em;
}

/* Strength */

.strength-meter {
  background-image: linear-gradient(90deg, #f700ff, #55f1be);
  height: 4px;
  width: calc(100% - 32px);
}

.strength-pointer {
  height: 0;
  position: relative;
  transition: transform 200ms cubic-bezier(0.4, 0, 0.2, 1);
  width: calc(100% - 32px);
}

.strength-pointer::after {
  border-color: transparent transparent #154271 transparent;
  border-style: solid;
  border-width: 5px;
  content: "";
  display: block;
  height: 0;
  left: 0;
  margin-left: -5px;
  position: absolute;
  top: 100%;
  width: 0;
}

/**
 * States
 */

/* Field Focus */

.field-input:focus ~ .field-input-focus {
  transform: scaleX(1);
}

/* Invalid */

.field-label.is-invalid .field-input-error {
  opacity: 1;
  transform: translateY(0);
}
.field-label.is-invalid .field-input-focus {
  background-color: #f602ff;
}
.field-label.is-invalid + .field-feedback {
  color: #f602ff;
}

/* Valid */

.field-label.is-valid .field-input-success {
  opacity: 1;
  transform: translateY(0);
}
.field-label.is-valid .field-input-focus {
  background-color: #36fd84;
}
.field-label.is-valid + .field-feedback {
  color: #36fd84;
}
</style>
