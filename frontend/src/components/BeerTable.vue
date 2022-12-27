<template>
  <div id="table">
    <h1>"{{title}}"</h1>
    <div id="tableBody">
      <div 
        v-for="(beer, idx) in beerList"
        :key="idx"
        class="table-item"
        @click="goToBeerDetail(beer.id)"
      >
        <img style="width:auto; height:150px;" v-if="beer.beerPhotoPath" v-bind:src="require(`@/assets/맥주이미지모음/${beer.beerPhotoPath}.png`)">
        <img style="width:auto; height:150px;" v-else src="@/assets/beer.png">
        <span style="width:auto;">{{beer.beer_kor_name}}</span>
      </div>
    </div>
  </div>
</template>

<script>
import http from '@/util/http-common.js'

import beer_image from '@/assets/beer.png'

export default {
  name : 'BeerTable',
  props : {
    title: String,
    classNum: Number, 
  },
  created() {
    http.get(`beer/list/에일/`)
    .then((res)=>{
      this.beerList = res.data
      console.log(this.beerList)
    })
  },
  watch: {
    title: function() { 
      this.getBeerList();
    }
  },
  data(){
    return {
      beer_image : beer_image,
      beerList : "",
    }
  },
  methods:  {
    getBeerList(){
      http.get(`beer/list/${this.title}/`)
      .then((res)=>{
        this.beerList = res.data
      })
    },
    goToBeerDetail(beer_id){
      this.$router.push(`beer/${beer_id}`)
    }
  },
}
</script>

<style scoped>
  #table {
    margin: 5% 0;
    width: 80%;
  }
  #table > h1 {
    text-align: center;
    margin-bottom: 10%;
    font-size: 2.5em;
    font-weight: bolder;
  }
  #tableBody{
    width: 100%;
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    justify-content: center;
    align-items: center;
  }
  .table-item{
    width: auto;
    aspect-ratio: 1;
    border: 1px solid black;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: white;
    cursor: pointer;
  }
  .table-item > img{
    height: 100%;
  }
  .table-item > span{
    font-size: 1em;
  }

  @media screen and (max-width: 768px){
    #table{
      width: 90%;
    }
    .table-item{

    }
  }

</style>