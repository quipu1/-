<template>
  <div class="warp">
    <main>
      <div id="recommendContainer">
        <h1>회원님을 위한 추천 맥주</h1>
        <div v-if="beerData.length > 0" id="recommendBeers">
          <div 
            v-for="(beer, idx) in beerData"
            :key="idx"
            class="beer"    
            @click="goToBeerDetail(beer.id)"
          >
            <div class="beer-image-container"><img v-bind:src="require(`@/assets/맥주이미지모음/${beer.beerPhotoPath}.png`)" alt=""></div>
            <div class="beer-info">
              <div class="beer-title">{{idx+1}}등 {{beer.beer_kor_name}}</div>
            </div>
          </div>
        </div>
        <div v-else>
          <h1>추천을 받기 위해서는 리뷰를 작성해 주세요</h1>
        </div>
      </div>

      <div id="userRecommendContainer">
        <h1 style="margin:5.5% 0 25%;">회원님과 취향이 비슷한 유저</h1>
        <div id="recommendUsers">
          <div
            class="row"
            v-for="(user, idx) in userData"
            :key="idx"
          >
            <span @click="goToProfilePage(user.userID)" style="cursor:pointer;">{{user.nickname}}</span>
            <button id="Btn" @ style="background-color:#F1C40F;">
              <a style="text-decoration:none; color:white;" :href="`http://j5c205.p.ssafy.io/api/chat/${user.userID}/?username=${nickname}`">채팅 하기</a>
            </button>
          </div>
        </div>
        <div v-if="userData.length == 0">
          <h1 class="user-recommend-container-h1">아직 추천할 만한 유저가 없습니다.</h1>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import http from '@/util/http-common.js'


export default {
  name : 'Recommend',
  components: {

  },
  data() {
    return {
      beerData : [],
      percent : [],
      userData : [],
      nickname : "",
    }
  },
  created(){
    console.log(this.$store.getters.getNickName)
    this.nickname = this.$store.getters.getNickName
    http.get(`recommend/${this.$store.getters.getNickName}`)
    .then((res)=>{
      this.beerData = res.data.beers.slice(0,9)
      this.percent = res.data.predict.slice(0,9)
    })
    http.get(`recommend/similar/${this.$store.getters.getNickName}`)
    .then((res)=>{
      console.log(res.data)
      this.userData = res.data.userlist
    })
  },
  methods : {
    goToBeerDetail(idx){
      this.$router.push(`/beer/${idx}`)
    },
    goToProfilePage(userId){
      this.$router.push({name : "Mypage", params : {userId : userId}})
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
  width: 85%;
  margin-left: 15%;
  padding-top: 5%;
  background-color: #F3F3F3;
  height: 100%;
  margin-bottom: 5%;

  display: flex;

}
#recommendContainer{
  margin-left: 5%;
  margin-right: 5%;
  width: 60%;
  height: 100%;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: white;
  box-sizing: border-box;
}
#recommendContainer > h1{
  position: relative;
  margin: 2% 0 5%;
}
#recommendBeers{
  position: relative;
  display: grid;
  justify-content: center;
  justify-items: center;
  align-items: center;
  width: 100%;
  /* height: 80%; */
  aspect-ratio: 1;
  grid-template-columns: repeat(3, 30%);
  gap: 5%;
  box-sizing: border-box;
}
.beer {
  display: flex;
  position: relative;
  justify-content: center;
  flex-direction: column;
  margin: 5%;
  align-items: center;
  /* height: 15%; */
  width: 100%;
  height: 100%;
  cursor: pointer;

  /* box-sizing: border-box; */
}
.beer-image-container{
  width: 75%;
  aspect-ratio: 1;
  border-radius: 50%;
  background-color:gray;
  display: flex;
  justify-content: center;
  align-items: center;

}
.beer-image-container > img{
  height: 100%;
  object-fit: cover;

}
.beer-info{
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  /* align-items: center; */

}
.beer-title {
  font-size: 1.25em;
  font-weight: bolder;

}
#userRecommendContainer{
  /* margin-left: 5%; */
  margin-right: 5%;
  width: 30%;
  height: 100%;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: white;
  box-sizing: border-box;
}
#userRecommendContainer > h1{
  position: relative;
  margin: 2% 0 5%;
  font-size: 1.2em;
}
.user-recommend-container-h1{
  font-size: 1.2em;
}
#recommendUsers{
  display: flex;
  justify-content: center;
  flex-direction: column;
  align-items: center;

  width: 80%;
  height: 40%;

  /* overflow: auto; */
}
.row{
  width: 100%;
  height: 100%;
  background-color: lightgray;
  border-radius: 15px;
  margin-bottom: 5%;
  display: flex;
  justify-content: space-around;
  align-items: center;
}
.row > span{
  width: 40%;
  margin: 0;
  text-align: center;
}
#Btn{
    width: 30%;
    outline: none;
    border: none;
    border-radius: 5px;
    /* background-color: #86D1DC; */
    /* height: 50%; */
    color:white;
    box-shadow: 0 3px 2px black;
    margin: 0 5%;
    font-size: 1em;
    text-align: center;
}
@media screen and (max-width: 768px){

  main{
    width: 100%;
    margin: 0;
  }
  #recommendContainer{
    width: 90%;
  }
  #recommendBeers{
    grid-template-columns: repeat(2, 1fr);
  }
  .beer-info{
    font-size: 0.7em;
  }

}
</style>