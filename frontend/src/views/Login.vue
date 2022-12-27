<template>
  <div class="warp">
    <div id="loginBeer">
      <div class="right">
        <h1 class="text-center" id="title">'비어'있는 편의점</h1>
        <h3 class="text-center" id="subTitle">C205</h3>
        <div
          id="loginForm"
        >
          <div class="login-form-line">
            <label for="loginForm.userID">아이디</label>
            <input type="text" v-model="loginForm.userID" @keyup.enter="onLogin">
          </div>
          <div class="login-form-line">
            <label for="loginForm.password">비밀번호</label>
            <input type="password" v-model="loginForm.password" @keyup.enter="onLogin">
          </div>
          <button @click="onLogin" id="loginBtn">로그인</button>
          <p>아직 회원이 아니십니까? <router-link to="/signup/user">회원가입</router-link></p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import beerImage from '@/assets/login_beer.png'
import drink2 from '@/assets/drink2.gif'
import KakaoImage from '@/assets/kakao_login_large_narrow.png'


export default {
  name : 'Login',
  data () {
    return {
      beerImage : beerImage,
      KakaoImage: KakaoImage,
      drink2 : drink2,
      loginForm : {
        userID: "",
        password : "",
      }
    }
  },
  methods: {
    onLogin() {
      const Form = new FormData();
      Form.append("userID" , this.loginForm.userID)
      Form.append("password", this.loginForm.password)
      this.$store.dispatch("LOG_IN", Form)
      .then(()=>{
        this.$router.push('/main')
      })
      .catch((res)=>{
        console.log(res)
        alert("아이디나 비밀번호가 일치하지 않습니다")
        this.$router.replace("/")
      })
    },
    goToKakao(){
      alert('카카오 페이지로 이동')
      this.$router.push('/signup')
    },
  }

}
</script>

<style scoped>
.warp{
  position: relative;
}
#loginBeer{
  width : 100vw;
  height : 100vh;
  background-image: url("../assets/drink2.gif");
  background-repeat: no-repeat;
  background-size: cover;
}
.right{
  width: 50%;
  height: 100%;
  float: right;
  background: white;
  /* display: flex; */
  /* justify-content: center; */
  /* flex-direction: column; */
  /* align-items: center; */
}
.text-center{
  text-align: center;
}
#title{
  font-size: 40px;
  margin-top: 12.5%;
  margin-bottom: 5%;
}
#subTitle{
  font-size: 30px;
  margin-bottom: 12.5%;
  color: rgba(132, 122, 108, 1);
}

#loginForm{
  /* margin-top: 5%; */
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
/* filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25)); */
  font-size: 1.25em;

}

.login-form-line{
  display: flex;
  align-items: center;
  width: 70%;
  height: 65px;
  border-radius: 5px;
  /* border: none; */
  /* outline: none; */
  box-shadow: 0px 2px 5px black;
  margin-bottom: 5%;
}
.login-form-line > label {
  text-align: center;
  width: 25%;
  border-right: 1px solid rgba(0, 0, 0, 0.25);
  font-weight: bold;
}
.login-form-line > input{
  width: 75%;
  margin-left: 2%;
}
.login-form-line > input:focus {
  outline: none;
}
#loginBtn{
  width: 15%;
  height: 50px;
  text-align: center;
  background-color: #0d47a1;
  color:white;
  border-radius: 5px;
  margin-bottom: 3.5%;
}
#loginForm > p {
  margin: 0;
}
#loginForm > p > a {
  text-decoration: none;
  color: black;
}
/* 
#loginBtn{
  display: flex;
  justify-content: center;
  margin-bottom: 10%;
  cursor: pointer;
} */

/* #btnImage{
  width: 250px;
} */
@media screen and (max-width : 768px) {
  /* .warp{
    display: none;
  } */
  #loginBeer{
    background-image: url("../assets/drink1.gif");
  }
  .right {
    /* display: none; */
    width: 100%;
    background-color: transparent;
    height: 100%;
  }
}
</style>
