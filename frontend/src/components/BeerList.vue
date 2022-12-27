<template>
  <div class="beer-list">
    <div class="beer-list-title">
      <span>{{title}}</span>
    </div>
    <div class="beer-list-content">
      <div
        v-for="(beer, idx) in beerList"
        :key="idx"
        class="beer-container"
        @click="goToBeerDetailPage($event, beer.id)"
      >
        <img style="margin-bottom: 5px" v-bind:src="require(`@/assets/맥주이미지모음/${beer.beerPhotoPath}.png`)" alt="" height="100px">
        <span class="beer-name">{{beer.beer_kor_name}}</span>
      </div>
      <div class="beer-name-background"></div>
    </div>
  </div>
</template>

<script>
import http from '@/util/http-common.js'

export default {
  name : 'BeerList',
  data() {
    return {
      width: document.body.clientWidth,
      wholeBeerList : [ 
      ],
      beerList: [ 
      ],
      idx : 6,
    }
  },
  props: {
    title : String,
    ad: String,
  },
  computed :  {

  },
  mounted() {
    window.addEventListener('resize', this.handleResize)
    let doms= document.getElementsByClassName("beer-list")
    // let titles= document.getElementsByClassName("beer-list-title")
    for (let i = 0; i < doms.length; i++){
      if (i % 2){
        doms[i].style.backgroundColor="#FFFEF9"
        doms[i].style.borderTop="3px solid #464646"

      }else{
        // titles[i].style.textDecoration="underline"
        doms[i].style.borderTop="3px solid #464646"
        // doms[i].style.backgroundColor="#FFF9E6"
        /* text-decoration: underline;
    text-underline-position:under; */
      }
    }
  },
  created() {
    var width = document.body.clientWidth
    if (width <= 768){
      var temp = this.beers.slice(0,4)
      this.beerList = temp
    } else{
      this.beerList = this.beers
    }
    if (this.ad === "like"){
      http.get(`/beer/list/like/`)
      .then((res)=>{
        this.wholeBeerList = res.data
        this.beerList = res.data.slice(0, this.idx)
      })
    }

    if (this.ad==="score"){
      http.get("beer/best/score/")
      .then((res)=>{
        this.wholeBeerList = res.data
        this.beerList = res.data.slice(0, this.idx)
      })
    }
    if (this.ad==="review"){
      http.get('beer/review/most/')
      .then((res)=>{
        console.log(res)
        this.wholeBeerList = res.data
        this.beerList = res.data.slice(0, this.idx)
      })
    }
  },
  beforeDestory : function() {
    window.removeEventListener('resize', this.handleResize)
  },
  methods : {
    goToBeerDetailPage(ev, idx){
      this.$router.push(`/beer/${idx}`)
    },
    handleResize(){
      this.width = document.body.clientWidth
      if(this.width <= 768){
        var temp = this.beers.slice(0,4)
        this.beerList = temp
      }else{
        this.beerList = this.beers
      }
    }
  }
}
</script>

<style scoped>
  .beer-list{
    display: flex;
    flex-direction: column;
    align-items: center;
    height: auto;
    margin-bottom: 5%;
    box-shadow: 3px 10px 5px 3px grey;
  }
  .beer-list-title{
    padding: 2% 0;
    font-size: 1.7em;
    font-weight: bold;
    /* text-decoration: underline; */
    text-underline-position:under;
  }
  .beer-list-content{
    position: relative;
    width: 100%;
    height: 40%;
    display: flex;
    /* flex-direction: column; */
    justify-content: space-around;
    align-items: center;
    align-content: center;
  }
  .beer-container{
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    width: 20%;
    margin : 1% 0 0;
  }
  .beer-container :hover{
    cursor: pointer;
  }
  .beer-name{
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0;
    /* margin-bottom: 5%; */
    width: 100%;
    z-index: 2;
    text-align: center;
    margin-bottom: 2%;
    color: aliceblue;
  }
  .beer-name-background{
    width: 100%;
    height: 2em;
    background-color: #464646;
    position: absolute;
    bottom: 0;
    z-index: 1;
  }


</style>