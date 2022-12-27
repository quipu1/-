<template>
  <header>
    <div
     @click="showSideBar"
    >
      <i id="sideBarBtn" class="fas fa-bars fa-2x"></i>
    </div>
    <div id="searchBarBackground">
      <select name="whatToSearch" id="selectSearch" style="width:20%; text-align:center; text-align-last: center;">
        <option value="beer" style="text-align:center;">맥주 이름</option>
        <option value="user" style="text-align:center;">유저 아이디</option>
      </select>
      <input type="text" id="searchBar" v-model="keyword" @keyup.enter="search">
      <i class="fab fa-sistrix cursor-pointer fa-lg" @click="search"></i>
    </div>
    <div id="headerIconBackground">
      <div class="icon-background" @click="goToHomePage">
        <i class="fas fa-home fa-2x"></i>
        <span style="display:flex;" >홈</span>
      </div>
      <div class="icon-background" @click="goToFeedPage">
        <i class="far fa-sticky-note fa-2x"></i>
        <span style="display:flex;">피드</span>
      </div>
      <div class="icon-background">
        <a :href="`http://j5c205.p.ssafy.io/api/chat/${this.$store.getters.getUserId}/?username=${this.$store.getters.getNickName}`"><i class="far fa-comment fa-2x" style="color:black;"></i></a>
        <span style="display:flex;">채팅</span>
      </div>
    </div>
  </header>
</template>

<script>
import http from '@/util/http-common.js'

export default {
  name : 'Header',
  data(){
    return {
      keyword: '',
      nickName: '',
      userId: '',
    }
  },
  created(){
    http.get(`user/${this.$store.getters.getUserId}/detail/`)
    .then((res)=>{
      this.userId = res.data.userID
      this.nickName = res.data.nickname
    })

    try{
      let width = document.body.clientWidth
      var sideBarBtn = document.getElementById('sideBarBtn')
      if(width <= 768){
        sideBarBtn.style.display = "block";
      } else{
        sideBarBtn.style.display = "none"
      }
    }catch (error){
      console.log(error)
    }
  },
  mounted(){
    window.addEventListener('resize', this.handleResize)

  },
  methods : {
    handleResize(){
      let width= document.body.clientWidth
      var sideBarBtn = document.getElementById('sideBarBtn')
      if(width <= 768){
        sideBarBtn.style.display = "block";
      } else{
        sideBarBtn.style.display = "none";
      }
    },
    search(){
      var d = document.getElementById('selectSearch')
      var selected = d.options[d.selectedIndex].value
      if (selected === "beer"){
        this.$router.push({name : "BeerSearchPage", params:{ keyword : this.keyword}});
      }
      if (selected === "user"){
        this.$router.push({name : "UserSearchPage", params:{ keyword : this.keyword}});
      }
    },
    goToHomePage() {
      this.$router.push('/main')
    },
    goToFeedPage(){
      this.$router.push('/feed')
    },
    goToChatPage() {
      window.open(`http://j5c205.p.ssafy.io/api/chat/${this.nickName}/?username=${this.nickName}`)
    },
    showSideBar(){
      document.getElementById('sideBar').style.display = 'block'
      document.getElementById('sideBarBtn').style.display = 'none'
      document.getElementById('closeSideBarBtn').style.display = 'block'
    }
  }
}
</script>

<style scoped>
*{
  margin: 0;
  padding: 0;
}
.cursor-pointer {
  cursor: pointer;
}
header{
  position: relative;
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  height: 125px;
  z-index: 1;
}
#sideBarBtn{
  display: none;
  font-size: 3em;
}
#searchBarBackground{
  width: 40%;
  padding-right: 1%;
  height: 50%;
  margin-left: 30.5%;
  border-radius: 0.5em;
  background-color: #C4C4C4;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
#selectSearch{
  margin: 0 2%;
  padding: 0;
}
#searchBar{
  outline: none;
  width: 90%;
  font-size: 1.5em;
}
#searchBar :focus{
  outline: none;
}
#headerIconBackground{
  display: flex;
  justify-content: center;
  width: 30%;
}
.icon-background{
  display: flex;
  width: auto;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 0 3%;
  cursor: pointer;
  text-align: center;
}
@media screen and (max-width: 768px) {
  header{
    display: flex;
    justify-content: space-around;
  }
  #sideBarBtn{
    font-size: 2rem;
    display: block;
    margin-left: 50%;
  }
  #searchBarBackground{
    font-size: 1rem;
    width: 50%;
    margin-left: 15%;
  }
  #headerIconBackground{
    font-size: 1rem;
  }
  #selectSearch{
    font-size: 0.5rem;
  }
  @media screen and (max-width: 360px) {
    #sideBarBtn{
      font-size: 0.5rem;
    }
    #searchBarBackground{
      font-size: 0.5rem;
      width: 50%;
      margin-left: 15%;
    }
    #headerIconBackground{
      font-size: 0.5rem;
    }
  }
}
</style>