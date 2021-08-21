<template>

  <v-app-bar class ="head">
      <div class ="top">
        <v-img src="dgb.jpg"></v-img>
      </div>
      
      <div class= "right">
        <v-layout align-center>
          <v-flex xs12 sm4 text-xs-center>
            <v-btn @click="onHome">
              <span class="material-icons">home</span>
              Home
            </v-btn>
          </v-flex>
          <v-flex xs12 sm4 text-xs-center>
            <v-btn @click="onLogin">
              <span class="material-icons">fingerprint</span>
              로 그 인
            </v-btn>
          </v-flex>
          <v-flex xs12 sm4 text-xs-center>
            <v-btn @click="onSignup">
              <span class="material-icons">perm_identity</span>
              회원가입
            </v-btn>
          </v-flex>
        </v-layout>
      </div>
  </v-app-bar>
</template>

<script>
export default {
  methods: {
    onLogin() {
      this.$router.push("/login");
    },
    onSignup() {
      this.$router.push("/signup");
    },
    onHome() {
      this.$router.push("/home");
    }
  }
}
</script>

<style scoped>
.head {
  position:fixed;
  left:0;
  top:0;
  width:100vw;
  z-index:300;
  height: auto;
  text-align: center;
}

.top {
  position: fixed;
  margin-left : 300px;
  width: 200px;
}

.right {
  position : fixed;
  display: inline-block;
  margin-left : 1500px;
  font-size : 15px;
  font-family:'Jua';
}

.flex {
  display : flex;
  margin-left : 10px;
}


</style>