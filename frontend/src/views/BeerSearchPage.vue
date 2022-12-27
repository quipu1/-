<template>
  <div class="warp">
    <main>
      <h1>'{{keyword}}'에 대한 맥주 검색 결과</h1>
      <div style="display:flex; justify-content:center; flex-direction:column; align-items:center;">
        <div
          class="beer-row"
          v-for="(beer, idx) in beerData"
          :key="idx"
        > 
          <img 
            v-if="beer.beer_kor_name != '해당하는 맥주가 없습니다.'" 
            class="beer-image" 
            @click="goToBeerDetailPage(beer.id)" 
            style="cursor:pointer;" 
            v-bind:src="require(`@/assets/맥주이미지모음/${beer.beerPhotoPath}.png`)" 
            alt="" 
            id="beerImage">
          <div class="beer-info" v-if="beer.beer_kor_name != '해당하는 맥주가 없습니다.'">
            <span @click="goToBeerDetailPage(beer.id)" style="cursor:pointer;">이름 : {{beer.beer_kor_name}}</span>
            <span>평점 : {{beer.score.toFixed(1)}}</span>
            <span>생산국가 : {{beer.country}}</span>
          </div>
          <div class="beer-button" v-if="beer.beer_kor_name != '해당하는 맥주가 없습니다.'">
            <button id="beerDataLikeBtn" @click="clickLikeBtn" :class="{blue : isblue, green : isgreen}">찜하기</button>
          </div>
          <div v-else class="beer-row" style="display:flex; justify-content:center; font-size: 1.5rem;">
              <span>해당하는 맥주가 없습니다.</span>  
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
import http from '@/util/http-common.js'

export default {
  name : "BeerSearchPage",
  props : {
    keyword : String,
  },
  data(){
    return {
      beerData : [
        {"beer_kor_name" : "해당하는 맥주가 없습니다."}
      ],
      isblue: true,
      isgreen : false,
    }
  },
  created(){
    http.get(`beer/search/${this.keyword}`)
    .then((res)=>{
      console.log(res.data)
      this.beerData = res.data
    })
    .catch(()=>{
      this.beerData = [{"beer_kor_name" : "해당하는 맥주가 없습니다."}]
    })
  },
  watch:  {
    keyword : function(){
      this.getBeerList();
    }
  },
  methods : {
    getBeerList(){
      http.get(`beer/search/${this.keyword}/`)
      .then((res)=>{
        console.log(res.data)
        this.beerData = res.data
        if(res.data.length===0){this.beerData = [{"beer_kor_name" : "해당하는 맥주가 없습니다."}]}
      })
      .catch(()=>{
        this.beerData = [{"beer_kor_name" : "해당하는 맥주가 없습니다."}]
      })
    },
    clickLikeBtn(){
      const likeBtn = document.getElementById('beerDataLikeBtn')
      if (this.isblue == true) {
        this.isblue = false; 
        this.isgreen = true
        likeBtn.innerText = "찜했음"
      }else{
        this.isblue = true; 
        this.isgreen= false
        likeBtn.innerText = "찜하기"
      }
    },
    goToBeerDetailPage(idx) {
      this.$router.push(`/beer/${idx}`)
    }
  },

}
</script>

<style scoped>
.blue {
  background-color: #4C73FD;
}
.green{ 
  background-color: #4CFD68;
}
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
  main > h1{
    padding: 5% 0;
    text-align: center;
  }
  .beer-row{
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
  .beer-image {
    display: block;
    width: 10%;
    aspect-ratio: 1;
    border-radius: 50%;
    background-color: gray;
  }
  .beer-info{
    width: 50%;
    display: flex;
    justify-content: center;
    align-items: flex-start;
    flex-direction: column;
  }
  .beer-button{
    width: 10%;
    height: 100%;
  }
  #beerDataLikeBtn{
    background-color: #4C73FD;
    color: white;
    border-radius: 5px;
    width: 100%;
    /* height: 100%; */
    font-size: 1.1em;
  }
  @media screen and (max-width : 768px) {
    main {
      margin :0;
      width: 100%;
    }
  }
</style>