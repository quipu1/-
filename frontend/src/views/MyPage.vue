<template>
  <div class="warp">
    <main>
      <div id="profilePart">
        <div id="profileImage"></div>
        <div id="profileNickName">
          <span>{{nickName}}</span>
          <div v-if="!this.isYourPage">
            <button v-if="friend" id="friendBtn" @click="clickDeleteFriendBtn"  style="background-color:#F96565;">친구끊기</button>
            <button v-if="friendAdd" id="friendBtn" @click="clickCancleFriendBtn" style="background-color:#2ECC40;">신청 중</button>
            <button v-if="friendYet" id="friendBtn" @click="clickFriendBtn" style="background-color:#86D1DC;" >친구신청</button>
            <button id="friendBtn" @ style="background-color:#F1C40F;">
              <a style="text-decoration:none; color:white;" :href="`http://j5c205.p.ssafy.io/api/chat/${this.$store.getters.getUserId}/?username=${this.$store.getters.getNickName}`">내 채팅방</a>
            </button>
          </div>
          <div>
            <button v-if="this.isYourPage" id="friendBtn" style="background-color:#F1C40F;">
              <a style="border:none; color:white;" :href="`http://j5c205.p.ssafy.io/api/chat/${this.userId}/?username=${this.$store.getters.getNickName}`">내 채팅방</a>
            </button>

          </div>
        </div>
        <div id="profileInfoPart">
          <span id="profileInfo">
            <span @click="showFeed">내 피드 : {{feedNum}}개 </span>
            <span @click="showReview">/ 내 리뷰 : {{reviewNum}}개</span>
          </span>
          <span id="friendNum" @click="showFriend">내 친구 : {{friendNum}}명</span>
        </div>
      </div>
      <div id="profileContent">
        <div id="menu">
          <div class="menu-item" @click="showFeed" id="menuFeedTitle">피드</div>
          <div class="menu-item" @click="showReview" id="menuReviewTitle">리뷰</div>
          <!-- <div class="menu-item" @click="showBadge" id="menuBadgeTitle">내 뱃지</div> -->
          <div class="menu-item" @click="showFriend" id="menuFriendTitle">친구</div>
        </div>
        <hr>
      </div>
      <FeedContent v-if="feedShow" :user_id="userId"/>
      <ReviewContent v-if="reviewShow" :user_id="userId"/>
      <BadgeContent v-if="badgeShow"/>
      <FriendContent v-if="friendShow" :user_id="userId"/>
    </main>
  </div>
</template>

<script>
import http from '@/util/http-common.js'

import BadgeContent from '@/components/BadgeContent.vue'
import FeedContent from '@/components/FeedContent.vue'
import ReviewContent from '@/components/ReviewContent.vue'
import FriendContent from '@/components/FriendContent.vue'


export default {
  name : 'MyPage',
  props : {
    userId : String,
  },
  components: {
    BadgeContent,
    FeedContent,
    ReviewContent,
    FriendContent,
  },
  
  created(){
    http.get(`user/${this.userId}/detail/`)
    .then((res)=>{
      this.user = res.data
      this.nickName = this.user.nickname
    })

    http.get(`user/${this.userId}/friends/`)
    .then((res)=>{
      this.friendNum = res.data.length
      for(let i = 0; i < res.data.length; i++){
        let userId = this.$store.getters.getUserId
        if(res.data[i] == userId){
          this.friend = true
          this.friendAdd = false
          this.friendYet = false
          break
        }
      }
    })

    http.get(`user/${this.userId}/friends/add/`)
    .then((res)=>{
      let userId = this.$store.getters.getUserId
      for(let i = 0; i < res.data.length; i++){
        if(res.data[i] == userId){
          this.friendAdd = true
          this.friend =false
          this.friendYet = false
          break
        }
      }
    })
    http.get(`feed/list/${this.userId}/`)
    .then((res)=>{this.feedNum = res.data.length})
    http.get(`beer/${this.userId}/review/`)
    .then((res)=>{this.reviewNum = res.data.length})
  },
  data() {
    return {
      user : "",
      nickName : "",
      isYourPage : (this.$store.getters.getUserId === this.userId) ? true : false,

      friend: false,
      friendAdd : false,
      friendYet : true,

      feedNum : "",
      reviewNum : "",
      friendNum : "",

      feedShow : true,
      reviewShow : false,
      badgeShow : false,
      friendShow : false,

    }
  },
  mounted(){

  },
  methods: {
    showFeed(){
      this.feedShow = true
      this.reviewShow = false
      this.badgeShow = false
      this.friendShow = false
      // document.getElementById("menuReviewTitle").style.color="black"
      // document.getElementById("menuBadgeTitle").style.color="black"
      // document.getElementById("menuFriendTitle").style.color="black"
      // document.getElementById("menuFeedTitle").style.color="#784A04"
    },
    showReview(){
      this.feedShow = false
      this.reviewShow = true
      this.badgeShow = false
      this.friendShow = false
      // document.getElementById("menuBadgeTitle").style.color="black"
      // document.getElementById("menuFeedTitle").style.color="black"
      // document.getElementById("menuFriendTitle").style.color="black"
      // document.getElementById("menuReviewTitle").style.color="#784A04"


    },
    showBadge(){
      // this.feedShow = false
      // this.reviewShow = false
      // this.badgeShow = true

      // document.getElementById("menuFeedTitle").style.color="black"
      // document.getElementById("menuReviewTitle").style.color="black"
      // document.getElementById("menuBadgeTitle").style.color="#784A04"
      alert('뱃지는 선택 사항이라 아직 개발 중입니다')

    },
    showFriend(){
      this.feedShow = false
      this.reviewShow = false
      this.badgeShow = false
      this.friendShow = true
      // document.getElementById("menuFriendTitle").style.color="#784A04"
      // document.getElementById("menuFeedTitle").style.color="black"
      // document.getElementById("menuReviewTitle").style.color="black"
      // document.getElementById("menuBadgeTitle").style.color="black"

    },
    clickDeleteFriendBtn(){
      http.delete(`user/from/${this.$store.getters.getUserId}/to/${this.userId}/delete/`)
      .then(()=>{
        this.friend = false; this.friendAdd = false; this.friendYet= true
      })
    },
    clickCancleFriendBtn(){
      const ans = confirm('친구 신청을 취소하겠습니까?')
      if (ans){
        this.friend = false; 
        this.friendAdd = false; 
        this.friendYet= true
        http.delete(`user/from/${this.$store.getters.getUserId}/to/${this.userId}/delete/`)
        alert('취소 되었습니다.')
        this.$router.go()
      }
    },
    clickFriendBtn(){
      if(this.$store.getters.getUserID !== this.userId){
        http.get(`user/from/${this.$store.getters.getUserId}/to/${this.userId}/`)
        .then(()=>{
            this.friend = false; this.friendAdd = true; this.friendYet= false
            alert('친구 신청이 완료되었습니다.')
            this.$router.go()
          }
        )}
      }
  },
}
  
</script>

<style scoped>
  .warp{
    position: relative;
    width: 100%;
    height: 100%;
  }
  main{
    position: relative;
    width: auto;
    height: 100vh;
    margin-left: 15%;
    background-color: #F3F3F3;
    height: 100%;
    margin-bottom: 5%;
  }
  #profilePart{
    height: 20%;
    padding: 1% 7.5%;
    display: grid;
    grid-template-columns: 1fr 1.2fr 4fr;
    align-items: center;
  }
  #profileImage{
    display: flex;
    width: 65%;
    aspect-ratio: 1;
    border-radius: 50%;
    background-color: gray;
  }
  #profileNickName{
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    /* align-items: center; */
  }
  #profileNickName > span{
    font-size: 2.5em;
    margin-bottom: 2%;
    font-weight: bolder;
  }
  #friendBtn{
    width: 30%;
    outline: none;
    border: none;
    border-radius: 5px;
    /* background-color: #86D1DC; */
    height: 3.5vh;
    color:white;
    box-shadow: 0 3px 2px black;
    margin: 0 5%;
  }
  #profileInfoPart{
    display: flex;
    flex-direction: column;
  }
  #profileInfo{
    font-size: 1.5em;
    margin-bottom: 1.5%;
    cursor: pointer;
  }
  #friendNum{
    /* margin-top: 5px; */
  }
  #menu{
    display: flex;
    justify-content: center;
    margin: 3% 0;
    font-size: 2em;
    font-weight: bolder;
    text-align: center;
    
  }
  .menu-item{
    margin: 0 4%;
    cursor: pointer;
  }
  #menuFeedTitle{
    color : #784A04;
  }
  #profileContent{
    margin-bottom: 5%;
  }
  #profileContent > hr {
    width: 80%;
    border: solid 1px gray;
    margin: 0 10%;
  }

  @media screen and (max-width: 768px) {
    main{
      width: 100%;
      height: 100%;
      margin: 0;
      font-size: 0.8rem;
    }

  }
  @media screen and (max-width: 360px) {
    main {
      font-size: 0.25rem;
    }
  }

</style>