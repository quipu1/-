<template>
  <div id="FriendContent">
    <h1 v-if="isYourPage" style="margin-bottom: 2.5%;">친구 신청 목록</h1>
    <div
      v-for="(friend, idx) in friendsAddList"
      :key="idx"
      class="friend-row"
    >
      <div v-if="isYourPage" class="friend-image-container">
        <div class="friend-image"></div>
        <!-- <img :src="`http://j5c205.p.ssafy.io/api/django/api/config${friend.profilePhotoPath}`" alt=""> -->
        <!-- <img :src="`http://localhost:8000/api/django/api/config${friend.profilePhotoPath}`" alt=""> -->
      </div>
      <div v-if="isYourPage" class="friend-info">
        <a :href="`http://localhost:3000/mypage/${friend.userID}/`">{{friend.nickname}}</a>
        <!-- <a :href="`http://j5c205.p.ssafy.io/mypage/${friend.userID}/`">{{friend.nickname}}</a> -->
      </div>
      <div v-if="isYourPage" class="friend-btns">
        <button id="friendBtn" @click="clickAddFriendBtn(friend.userID)"  style="background-color:#2ECC40;">친구수락</button>
      </div>
    </div>
    <div
      class="friend-row"
      style="height:100px;"
      v-if="friendsAddList.length===0 && isYourPage"
    >
      <h3 v-if="isYourPage">신청한 친구가 없습니다.</h3>
    </div>
    <h1 style="margin-bottom: 2.5%;">친구 목록</h1>
    <div 
      v-for="(friend, idx) in friendsList"
      :key="idx"
      class="friend-row"
    >
      <div class="friend-image-container">
        <div class="friend-image"></div>
        <!-- <img :src="`http://j5c205.p.ssafy.io/api/django/api/config${friend.profilePhotoPath}`" alt=""> -->
        <!-- <img :src="`http://localhost:8000/api/django/api/config${friend.profilePhotoPath}`" alt=""> -->
      </div>
      <div class="friend-info">
        <a :href="`http://localhost:3000/mypage/${friend.userID}/`">{{friend.nickname}}</a>
        <!-- <a :href="`http://j5c205.p.ssafy.io/mypage/${friend.userID}/`">{{friend.nickname}}</a> -->

      </div>
      <div class="friend-btns">
        <button v-if="isYourPage" id="friendBtn" @click="clickDeleteFriendBtn(friend.userID)"  style="background-color:#F96565;">친구끊기</button>
      </div>
    </div>
    <div
      v-if="friendsList.length===0"
      class="friend-row"
      style="height:100px;"
    >
      <h3>친구가 없습니다.</h3>
    </div>
  </div>
</template>

<script>
import http from '@/util/http-common.js'

export default {
  name : "FriendContent",
  props : ["user_id"],
  mounted(){},
  created(){
    http.get(`user/${this.user_id}/friends/`)
    .then((res)=>{
      for(let i= 0; i < res.data.length; i++){
        http.get(`user/${res.data[i]}/detail/`)
        .then((res)=>{
          this.friendsList.push(res.data)
        })
      }
    })

    http.get(`user/${this.user_id}/friends/add/`)
    .then((res)=>{
      for(let i = 0; i < res.data.length; i++){
        http.get(`user/${res.data[i]}/detail/`)
        .then((res)=>{
          this.friendsAddList.push(res.data)
        })
      }
    })

    this.isYourPage = (this.$store.getters.getUserId === this.user_id) ? true : false
  },
  data(){
    return {
      friendsList : [],
      friendsAddList : [],
      isYourPage : "",
    }
  },
  methods: {
    clickAddFriendBtn(name){
      const value = confirm('친구 수락하시겠습니까?')
      if (value){
        http.get(`user/from/${this.$store.getters.getUserId}/to/${name}/`)
        .then(()=>{
          this.$router.go()
        })
      }
    },
    clickDeleteFriendBtn(name){
      const value = confirm('친구에서 삭제하시겠습니까?')
      if (value){
        http.delete(`user/from/${this.$store.getters.getUserId}/to/${name}/delete/`)
        .then(()=>{
          this.$router.go()
        })
      }
    },
  }
  
}
</script>

<style scoped>
  #FriendContent{
    padding: 0 10%;
  }
  .friend-row {
   position: relative;
   display: flex;
   justify-content: space-around;
   align-items: center;

   background-color: white;
   border-radius: 15px;
   margin-bottom: 5%;

  }
  .friend-image-container{
    width: 20%;
    display: flex;
    justify-content: center;
    align-items: center;

  } 
  .friend-image{
    width: 100px;
    aspect-ratio: 1;
    border-radius: 50%;
    background-color: gray;
  }
  .friend-info{
    width: 30%;
  }
  .friend-btns{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 50%;
  }
  #friendBtn{
    display: flex;
    color: white;
    width: 15%;
    height: 80%;
    border-radius: 15px;
    text-align: center;
    justify-content: center;
  }
</style>