<template>
  <div class="warp">
    <main id="beerDetailContainer">
      <div id="beerImageContainer"><img v-bind:src="require(`@/assets/맥주이미지모음/${beerData.beerPhotoPath}.png`)" alt="" id="beerImage"></div>
      <h3 id="beerTitle">{{beerData.beer_kor_name}}</h3>
      <div id="beerInfo">
        <p style="margin: 0; margin-bottom: 5%">평점 {{beerData.score.toFixed(1)}} / 종류 : {{beerData.beer_type}} / 생산지 : {{beerData.country}}</p>
        <h3>설명</h3>
        <div style="margin: 0 10%">{{beerData.description}}</div>

        <div style="display:flex; margin:5%; justify-content: space-evenly;">
          <div class="aroma" id="scores"><p>향</p><p>{{beerData.aroma.toFixed(1)}}</p></div>
          <div class="appearance" id="scores"><p>외관</p><p>{{beerData.appearance.toFixed(1)}}</p></div>
          <div class="flavor" id="scores"><p>맛</p><p>{{beerData.flavor.toFixed(1)}}</p></div>
          <div class="mouthfeel" id="scores"><p>마우스필</p><p>{{beerData.mouthfeel.toFixed(1)}}</p></div>
        </div>
      </div>
      <button id="beerDataLikeBtn" @click="clickLikeBtn" :class="{blue : isblue, green : isgreen}">찜하기</button>
      <BeerDetailReview
       :beer_id="beerData.id"
       :beer_eng_name="beerData.beer_eng_name"
      />
    </main>
  </div>
</template>

<script>
import BeerDetailReview from '@/components/BeerDetailReview.vue'
import http from '@/util/http-common.js'

import ho from '@/assets/맥주이미지모음/호가든.png'
import goose from '@/assets/구스아일랜드ipa.png'
import cass from '@/assets/카스.png'
import blanc from '@/assets/맥주이미지모음/블랑.png'

export default {
  name : 'BeerDetail',
  props: {
    beer_id : String,
  },
  created(){
    http.get(`beer/${this.beer_id}/`)
    .then((res)=>{
      this.beerData = res.data
    })
    http.get(`beer/like/${this.$store.getters.getUserId}/`)
    .then((res)=>{
      for (let i = 0 ; i < res.data.length; i ++){
        if (this.beer_id == res.data[i].id){
          const likeBtn = document.getElementById('beerDataLikeBtn')
          this.isblue = false; 
          this.isgreen = true
          likeBtn.innerText = "찜했음"
        }
      }
    })


  },
  components: {
    BeerDetailReview,
  },
  data() {
    return {
      blanc : blanc,
      ho : ho,
      goose : goose,
      cass : cass,
      beerData : "",
      beerImage : "",
      isblue: true,
      isgreen : false,
    }
  },
  mounted () {
  },
  methods : {
    clickLikeBtn(){
      http.get(`beer/${this.beer_id}/like/${this.$store.getters.getUserId}/`)
      .then(()=>{
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
      })
    }
  }

}
</script>

<style scoped>
  .warp{
    position: relative;
    width: 100%;
    height: 100%;
  }
.blue {
  background-color: #4C73FD;
}
.green{ 
  background-color: #4CFD68;
}
.aroma {
  background-color: #FCD1D1;
}
.appearance {
  background-color: #ECE2E1;
}
.flavor {
  background-color: #D3E0DC;
}
.mouthfeel {
  background-color: #AEE1E1;
}


main {
  position: relative;
  width: 85%;
  margin-left: 15%;
  background-color: #F3F3F3;
  margin-bottom: 5%;

}
#beerDetailContainer{
  height: 100%;
  /* width: 60%; */
  display: flex;
  flex-direction: column;
  align-items: center;

}
#beerImageContainer{
  width: 25%;
  aspect-ratio: 1;
  border-radius: 50%;
  background-color: gray;
  margin: 5% 0 5%;

  display: flex;
  justify-content: center;
  align-items: center;

}
#beerImage{
  width: auto;
  height: 100%;
  object-fit: cover;
}
#beerTitle{
  font-size: 1.5em;
  margin-bottom: 2%;
}
#beerScore {
  margin: 2% 0;
}
#beerInfo{
  text-align: center;

}
#beerScore > i{
  color:  rgb(228, 175, 1);
}
#beerInfo > h3{
  margin-bottom: 2%;
}
#beerInfo > p{
  margin: 10% 0;
}
#scores {
  /* display: flex; */
  margin: 2% 0;
  padding: 2%;
  width: 20%;
  border-radius:10px;
}
#scores > p{
  margin: 0
}
#beerDataLikeBtn{
  background-color: #4C73FD;
  color: white;
  border-radius: 5px;
  width: 98px;
  height: 31px;
  padding: 0.5% 0;
  font-size: 0.9em;
  text-align: center;
  justify-items: center;
}
@media screen and (max-width: 768px){
  main {
    width: 100%;
    margin: 0;
  }
  #beerDataLikeBtn{
    width: 20%;
    font-size: 1em;
  }
}


</style>