<template>
  <div class="warp">
    <div id="signupBeer">
      <div class="right">
        <h1 class="text-center" id="title">'비어'있는 편의점</h1>
        <h3 class="text-center" id="subTitle">회원가입</h3>
        <div
          id="signupForm"
        > 
          <div class="signup-form-with-btn">
            <div class="signup-form-line border-radius" style="width:75%; margin:0;">
              <label for="userId" style="width:37.475%;">아이디</label>
              <input type="text" v-model="userId" @keyup.enter="onSignup">
            </div>
            <button class="duplicate-check-btn border-radius" style="width:20%;" @click="checkIdDuplicate" id="checkIdBtn"><i class="fas fa-check"></i></button>
          </div>
          <div class="signup-form-with-btn">
            <div class="signup-form-line border-radius" style="width:75%; margin:0;">
              <label for="nickName" style="width:37.475%;">닉네임</label>
              <input type="text" v-model="nickName" @keyup.enter="onSignup">
            </div>
            <button class="duplicate-check-btn border-radius" style="width:20%;" @click="checkNickNameDuplicate" id="checkNickNameBtn"><i class="fas fa-check"></i></button>
          </div>
          <div class="signup-form-line border-radius">
            <label for="pwd">비밀번호</label>
            <input type="password" v-model="pwd" @keyup.enter="onSignup">
          </div>
          <div class="signup-form-line border-radius">
            <label for="pwdConfirm">비밀번호 확인</label>
            <input type="password" v-model="pwdConfirm" @keyup.enter="onSignup">
          </div>
          <button class="border-radius" @click="onSignup" id="signupBtn">회원가입</button>
          <p>회원이십니까? <router-link to="/" style="color:black;">로그인</router-link></p>
        </div>
        <!-- <div id="loginBtn">
          <img @click="goToKakao" :src="KakaoImage" alt="" id="btnImage" >
        </div> -->
      </div>
    </div>
  </div>
</template>

<script>
import beerImage from '@/assets/login_beer.png'
import drink2 from '@/assets/drink2.gif'
import KakaoImage from '@/assets/kakao_login_large_narrow.png'
import http from '@/util/http-common.js'

export default {
  name : 'SignupUser',
  data () {
    return {
      beerImage : beerImage,
      KakaoImage: KakaoImage,
      drink2 : drink2,

      userId: "",
      nickName : "",
      pwd : "",
      pwdConfirm : "",

      idCheck : false,
      nickNameCheck : false
    }
  },
  watch:  {
    userId: function () {
      this.checkId();
    },
    nickName : function() {
      this.checkNickName();
    }

  },
  methods: {
    checkId(){
      const btn = document.getElementById('checkIdBtn')
      btn.style.backgroundColor = "transparent"
      btn.style.color = "black"
      btn.innerHTML ="<i class='fas fa-check'></i>"
      this.idCheck = false
    },
    checkNickName(){
      const btn = document.getElementById('checkNickNameBtn')
      btn.style.backgroundColor = "transparent"
      btn.style.color = "black"
      btn.innerHTML ="<i class='fas fa-check'></i>"
      this.nickNameCheck = false
    },
    goToKakao(){
      alert('카카오 페이지로 이동')
      this.$router.push('/signup')
    },
    onSignup() {
      if(!this.idCheck){alert('아이디 체크를 완료해 주세요'); return}
      if(!this.nickNameCheck){alert('닉네임 체크를 완료해 주세요'); return}
      if(this.pwd !== this.pwdConfirm){alert('비밀번호가 일치하지 않습니다.');return}
      const Form = new FormData();
      Form.append("userID", this.userId)
      Form.append("nickname", this.nickName)
      Form.append("password", this.pwd)
      this.$store.dispatch("SIGN_UP", Form)
      .then(()=>{
        alert('회원가입이 완료되었습니다')
        this.$router.push('/signup')
      })
    },
    checkIdDuplicate() {
      http.get(`register/userID/${this.userId}/`)
      .then(()=>{
        alert('사용가능한 아이디입니다')
        const btn = document.getElementById('checkIdBtn')
        btn.style.backgroundColor = "#28a745"
        btn.style.color = "white"
        btn.innerText="O"
        this.idCheck = true
      })
      .catch(()=>{
        alert('이미 존재하는 아이디입니다')
      })


    },
    checkNickNameDuplicate(){
      http.get(`register/nickname/${this.nickName}/`)
      .then(()=>{
        alert('사용가능한 닉네임입니다')
        const btn = document.getElementById('checkNickNameBtn')
        btn.style.backgroundColor = "#28a745"
        btn.style.color = "white"
        btn.innerText="O"
        this.nickNameCheck = true
      })
      .catch(()=>{
        alert('이미 존재하는 닉네임입니다')
      })
    }
  }

}
</script>

<style scoped>
.warp{
  position: relative;
}
#signupBeer{
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
.border-radius {
  border-radius: 5px;
}
#title{
  font-size: 40px;
  margin-top: 10%;
  margin-bottom: 5%;
}
#subTitle{
  font-size: 30px;
  margin-bottom: 10%;
  color: rgba(132, 122, 108, 1);

}
#signupForm{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  /* filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25)); */
  font-size: 1.2em;
}
.signup-form-with-btn {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;

  width: 70%;
  margin-bottom: 5%;
}

.duplicate-check-btn{
  width: 10%;
  height: 65px;
  border-radius: 5px;
  box-shadow: 0px 2px 5px black;
  
}
.signup-form-line{
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
.signup-form-line > label {
  text-align: center;
  width: 25%;
  border-right: 1px solid rgba(0, 0, 0, 0.25);
  font-weight: bold;
  /* margin: 0 1%; */
}
.signup-form-line > input{
  width: 75%;
  margin-left: 2%;
}
.signup-form-line > input:focus {
  outline: none;
}
.signup-form-line > button {
  width: 20%;
}
#signupBtn {
  width: 15%;
  height: 50px;
  text-align: center;
  background-color: #0d47a1;
  color:white;
  border-radius: 5px;
  margin-bottom: 3.5%;
}
#signupForm > p  {
  margin: 0;
}
#signupForm > p > a {
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

  #signupBeer{
    background-image: url("../assets/drink1.gif");
  }
  .right {
    /* display: none; */
    width: 100%;
    background-color: transparent;
    height: 100%;
  }
  #signupBtn{
    width: 25%;
  }
  .signup-form-line >label {
    font-size: 0.8em;
  }
  /* .signup-form-with-btn > button{
    font-size: 0.8em;
  } */
  .duplicate-check-btn{
    font-size: 1px;
  }
}
</style>
