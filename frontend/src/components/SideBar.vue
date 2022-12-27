<template>
  <nav id="sideBar">
    <i @click="closeSideBar" style="float:right; margin-top: 5%; margin-right: 10%; font-size: 2em;" id="closeSideBarBtn" class="fas fa-angle-left fa-9x"></i>
    <div id="logoPart" @click="goToMainPage">
      <img style="width:60%; margin-top: 15%;" :src="Logo" alt="">
    </div>
    <div id="profilePart">
      <div id="profileInfo">
        <p style="font-size: 20px;" id="nickName" @click="goToMyPage">{{this.nickName}}</p>
        <!-- <div id="levelBar">레벨 : {{level}}</div> -->
      </div>
      <!-- <a :href="`http://localhost:3000/mypage/${this.$store.getters.getUserId}/`" style="color:black;"><i class="fa fa-plus-circle fa-lg cursor-pointer"></i></a> -->
      <a :href="`https://j5c205.p.ssafy.io/mypage/${this.$store.getters.getUserId}`" style="color:black;"><i class="fa fa-plus-circle fa-lg cursor-pointer"></i></a>
    </div>
    <div id="sideBarMenu">
      <div class="sidebar-item" @click="goToReccomendPage">
        <div>
          <i class="far fa-thumbs-up fa-lg"></i>
        </div>
        <span>내게 맞는 맥주</span> 
      </div>
      <div class="sidebar-item" @click="goToBeerPage">
        <div>
          <i class="fas fa-beer fa-lg"></i>
        </div>
        전체 맥주 목록
      </div>
      <div class="sidebar-item" @click="goToLikeBeerPage">
        <div>
          <i class="fas fa-heart fa-lg"></i>
        </div>
        찜한 맥주 목록
      </div>
      <!-- <div class="sidebar-item" @click="goToImageBeerPage">
        <div>
          <i class="fas fa-camera-retro fa-lg"></i>
        </div>
        이미지로 맥주 찾기
      </div> -->
      <div class="sidebar-item" @click="goToStorePage">
        <div>
          <i class="fas fa-map-marker-alt fa-lg"></i>
        </div>
        근처 친구찾기
      </div>
      <div class="sidebar-item" @click="goToSettingPage">
        <div>
          <i class="fas fa-cog fa-lg"></i>
        </div>
        설정
      </div>
      <div id="logoutBtn" @click="logout">
        로그아웃
      </div>
    </div>
  </nav>
</template>

<script>
// import http from '@/util/http-common.js'

import Logo from '@/assets/newlogo4.png'
import Plus from '@/assets/plus.png'

export default {
  name : 'SideBar',

  data () {
    return {
      Logo : Logo,
      Plus : Plus,
      level : "3",
      userId : "",
      nickName : this.$store.getters.getUserId,
      imgPath : this.$store.getters.getNickName,
    }
  },
  computed : {
  },
  created (){

    try{
      let width= document.body.clientWidth
      let sideBar = document.getElementById('sideBar')
      if(width <= 768){
        sideBar.style.display = "none"
      } else{
        sideBar.style.display = "block"
      }
    }catch(error){
      console.log(error)
    }
  },
  mounted () {
    window.addEventListener('resize', this.handleResize)
  },

  methods : {
    handleResize(){
       let width= document.body.clientWidth
       const closeBtn = document.getElementById('closeSideBarBtn')
       let sideBar = document.getElementById('sideBar')
       if(width <= 768){
          closeBtn.style.display = "block";
          sideBar.style.display = "none"
       } else{
         closeBtn.style.display = "none"
         sideBar.style.display = "block"
       }
    },
    closeSideBar(){
      document.getElementById('sideBar').style.display = 'none'
      document.getElementById('sideBarBtn').style.display = 'block'
    },
    goToMainPage() {
      this.$router.push('/main')
    },
    goToMyPage(){
      this.$router.push(`/mypage/${this.userId}`)
    },
    goToReccomendPage(){
      this.$router.push('/recommend')
    },
    goToBeerPage() {
      this.$router.push('/beerlist')
    },
    goToLikeBeerPage() {
      this.$router.push('/beer/like')
    },
    goToImageBeerPage(){
      this.$router.push('/camera_detection')
      // alert('이미지로 맥주 찾기로 이동')
    },
    goToStorePage(){
      this.$router.push('/beer_party')
      // alert('가게 페이지로 이동')
    },
    goToSettingPage(){
      this.$router.push('/setting')
    },
    logout(){
      const value = confirm('로그아웃 하시겠습니까?')
      if(value){
        alert('로그 아웃')
        localStorage.removeItem("vuex")
        this.$router.push('/')
      } 
    }
  }

}
</script>

<style scoped>
*{
  margin: 0;
  padding: 0;
}
#sideBar{
  position : fixed;
  margin: 0;
  top: 0;
  left: 0;
  background-image: url('../assets/sidebar-background.png');
  background-size: cover;
  width: 15%;
  height: 100vh;
  z-index: 99;
  font-size: 1em;
}
#closeSideBarBtn{
  display: none;
  text-align: end;
  font-size: 1.5em;
}
#logoPart{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 3% 0;
  cursor:pointer;
  height: 125px;
}
#logoPart > span {
  margin-top: 5%;
  font-size: 1.1em;
  font-weight: 900;
}
#profilePart{
  margin: 25% 6% 8% 6%;
  display: flex;
  justify-content: space-around;
  align-items: center;
}
#profilePicture{
  width: 30%;
  aspect-ratio: 1;
  border-radius: 50%;
  background-color: gray;
}
#profileInfo{
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 50%;
}
#nickName{
  margin: 0;
  font-size: 1.3em;
  font-weight: 900;
}
#levelBar{
  display: flex;
  justify-content: center;
  width: 75%;
  color: rgb(255, 238, 238);
  font-size: 0.5em;
  height: 20px;
  background-color: #B1B5FF;
  border-radius: 0.5em;
}
.cursor-pointer{
  cursor:pointer;
}
#sideBarMenu :hover{
  background-color: #E5E2E1;
  cursor: pointer;
}
.sidebar-item{
  display: flex;
  align-items: center;
  height: 60px;
}
.sidebar-item > div {
  display: flex;
  width: 30%;
  justify-content: center;
  align-items: center;
}
.sidebar-item-image-contianer {
  display: flex;
  justify-content: center;
  width: 30%;
}

#logoutBtn {
  display: flex;
  margin-top: 25%;
  align-items: center;
  height: 5vh;
  font-size: 1em;
  padding-left: 30%;
  background-color: #E5E2E1;
  cursor: pointer;
}
@media screen and (max-width: 768px){
  #sideBar{
    display: none;
    background-color: white;
    opacity: 1;
    width: 30%;
  }
}
@media screen and (max-width: 360px){
  #sideBar{
    display: none;
    background-color: white;
    opacity: 1;
    width: 50%;
  }
}
</style>