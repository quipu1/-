<template>
  <div class="warp">
    <main>
      <h1>'{{keyword}}'에 대한 유저 검색 결과</h1>
      <div style="display:flex; justify-content:center; flex-direction:column; align-items:center;">
        <div
          class="user-row"
          v-for="(user, idx) in userData"
          :key="idx"
        >
          <div @click="goToUserPage(user.userID)" style="cursor:pointer;" class="user-image" v-if="user.nickname != '검색하신 유저가 존재하지 않습니다.'"></div>
          <div class="user-info" v-if="user.nickname != '검색하신 유저가 존재하지 않습니다.'">
            <span @click="goToUserPage(user.userID)"  style="cursor:pointer;">닉네임 : {{user.nickname}}</span>
          </div>
          <div class="user-button" v-if="user.nickname!= '검색하신 유저가 존재하지 않습니다.'">
            <!-- <button @click="sendFriendReq" id="friendBtn">친구 신청</button> -->
          </div>
          <div v-else class="user-row" style="display:flex; justify-content:center; align-items:center; font-size: 1.5rem;">
            <span>검색하신 유저가 존재하지 않습니다.</span> 
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import http from '@/util/http-common.js'

export default {
  name : 'UserSearchPage',
  props : {
    keyword: String
  },
  data(){
    return {
      userData : [
        {"nickname" : "검색하신 유저가 존재하지 않습니다.",},
      ]
    }
  },
  created(){
    http.get(`user/search/${this.keyword}/`)
    .then((res)=>{
      this.userData = res.data
      if(res.data.length===0){this.userData = [{"nickname" : "검색하신 유저가 존재하지 않습니다."}]}
    })
    .catch(()=>{
      this.userData = [{"nickname" : "검색하신 유저가 존재하지 않습니다."}]
    })
  },
  watch : {
    keyword : function() {
      this.getUserList();
    },
  },
  methods : {
    getUserList(){
      http.get(`user/search/${this.keyword}/`)
      .then((res)=>{
        this.userData = res.data
      })
      .catch(()=>{
        this.beerData = [{"nickname" : "검색하신 유저가 존재하지 않습니다."}]
      })
    },
    goToUserPage(userId){
      this.$router.push({name : "Mypage", params:{userId : userId}})
    },
    // sendFriendReq(){
    //   http.get(`user/from/${this.$store.getters.getUserId}/to/${this.userId}/`)
    //   .then(()=>{
    //     alert('친구 신청을 보냈습니다.')
    //   })
    // },
  },
}
</script>

<style scoped> 
  .warp {
    position: relative;
    width: 100%;
    height: 100%;
  }
  main {
    position: relative;
    width: 85%;
    height: 100%;
    margin-left: 15%;
    background-color: #F3F3F3;
    margin-bottom: 5%;

  }
  main > h1 {
    padding: 5% 0;
    text-align: center;
  }
  .user-row{
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: white;
    width: 80vw;
    height: 20%;
    border-radius: 15px;
    margin-bottom: 5%;
    padding: 0 5%;
  }
  .user-image {
    display: block;
    width: 10%;
    aspect-ratio: 1;
    border-radius: 50%;
    background-color: gray;
  }
  .user-info{
    width: 50%;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    flex-direction: column;
  }

</style>