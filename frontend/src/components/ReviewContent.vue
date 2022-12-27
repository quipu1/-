<template>
  <div id="ReviewContent">
    <div
      class="review"
      v-for="(review, idx) in reviews"
      :key="idx"
      @click="goToBeerDetailPage(review.beer)"
    >
      <div class="beer-image-container">
        <img v-bind:src="require(`@/assets/맥주이미지모음/${photoPath[idx]}.png`)" alt="" class="beerImage">
      </div>
      <div class="review-head">
        <p>{{beerName[idx]}}</p>
        <i class="fas fa-star"
          v-for="(idx) in review.score"
          :key="idx"
        ></i>
      </div>
      <div class="review-body">
        {{review.content}}
      </div>
    </div>
  </div>
</template>

<script>
import http from '@/util/http-common.js'

export default {
  name : "ReviewContent",
  props : ['user_id'],
  data(){
    return {
      reviews : [],
      photoPath : [],
      beerName : [],
    }
  },
  created(){
    http.get(`beer/${this.user_id}/review/`)
    .then((res)=>{
      this.reviews =res.data
      // console.log(this.reviews)
      for(let i = 0; i < res.data.length;i++){
        http.get(`beer/${res.data[i].beer}/`)
        .then((res)=>{
          this.photoPath.push(res.data.beerPhotoPath)
          this.beerName.push(res.data.beer_kor_name)
        })
      }
    })
    
  },
  methods : {
    goToBeerDetailPage(beerName){
      this.$router.push({name : "BeerDetail", params : {"beer_id" : beerName}})
    }
  }
}
</script>

<style scoped>
 #ReviewContent{
   padding: 0 10%;
   /* height: 100%; */
 }
 .review{
   position: relative;
   display: flex;
   justify-content: space-around;
   align-items: center;
   /* animation: fadein 5s ease 3s; */
   /* width: 100%; */
   /* height: 10%; */
   /* height: 300px; */
   background-color: white;
   border-radius: 15px;
   cursor: pointer;
   margin-bottom: 5%; 
   overflow: auto;
 }
 .beer-image-container{
   width: 20%;
   height: 100px;

   display: flex;
   justify-content: center;
   align-items: center;
 }
 .beerImage{
   height: 100%;
 }
 .review-head{
   width: 30%
 }
 .review-body{
   width: 50%;
 }
 @keyframes fadein {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
  }
.review-image-container{
  width: 100px;
  aspect-ratio: 1;
} 
.review-image-container > img{
  width: 100%;
}
.review-head {
  margin: 0 5%;
}
.review-head > p{
  font-size: 1.3em;
  margin: 0;
}
.review-head > i{
  color : rgb(228, 175, 1)
}
.review-body {
  font-size: 1.1em;
}

</style>