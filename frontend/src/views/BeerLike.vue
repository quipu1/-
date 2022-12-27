<template>
  <div class="warp">
    <main>
      <div id="beerLikeListContainer">
        <div id="beerLikeListTitle">
          <span>내가 찜한 맥주</span>
        </div>
        <div id="beerLikeList" v-if="beerData.length > 0">
          <div
            v-for="(beer,idx) in beerData"
            :key="idx"
            class="beer"
            @click="goToBeerDetailPage(beer.id)"          
          >
            <div class="beer-image-container" style="">
              <img v-bind:src="require(`@/assets/맥주이미지모음/${beer.beerPhotoPath}.png`)" alt="">
            </div>
            <div style="position: absolute;">
              <div style="font-weight: bold; font-size: 1.3rem; background-color: lightgray; border-radius: 10px;">{{ beer.beer_kor_name }}</div>
            </div>
          </div>
        </div>
        <div v-else>
          <h1>찜한 목록이 없습니다.</h1>
        </div>
      </div>
    </main>
  </div>
</template>

<script>

import http from '@/util/http-common.js'
export default {
  name : 'BeerLike',
  data() {
    return {
      beerData : "",
    }
  },
  created(){
    http.get(`beer/like/${this.$store.getters.getUserId}/`)
    .then((res)=>{
      console.log(res)
      this.beerData = res.data
    })
  },
  methods : {
    goToBeerDetailPage(idx) {
      this.$router.push(`/beer/${idx}`)
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
  main {
    position: relative;
    width: 85%;
    
    margin-left: 15%;
    background-color: #F3F3F3;
    margin-bottom: 5%;

  }
  #beerLikeListContainer{
    /* width: 90%; */
    height: 100vh;
    background-color: white;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    /* align-items: center; */
  }
  #beerLikeListTitle {
    display: flex;
    justify-content: center;
    width: 100%;
    font-size: 3rem;
    font-weight: bolder;
    margin: 5% 0;
  }
  #beerLikeListTitle > span {
    margin: 0 2%;
  }
  #beerLikeList{
    display: grid;
    width: 80%;
    box-sizing: border-box;
    justify-content: center;
    justify-items: center;
    align-items: center;
    grid-template-columns: repeat(4, 1fr);
  }
  .beer{
    margin: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    width: auto;
  }
  .beer-image-container{
    /* width: 100px; */

    height: 250px;
    aspect-ratio: 1;
    border-radius: 50%;
    background-color: gray;
    cursor: pointer;
    margin: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin-bottom: 5%;
  }
  .beer-image-container > img {
    height: 100%;
    object-fit: cover;
  }
  @media screen and (max-width: 1210px) {
    #beerLikeList{
      grid-template-columns: repeat(4, 1fr);
    }
  }
  @media screen and (max-width: 768px) {
    main {
      width: 100%;
      margin: 0;
    }
    #beerLikeList{
      width: 90%;
      grid-template-columns: repeat(3, 1fr);
    }
    .beer-image-container{
      width: 60%;
    }
  }
  @media screen and (max-width: 768px) {
    #beerLikeListTitle{
      font-size: 1.5rem;
    }
    #beerLikeList{
      grid-template-columns: repeat(2, 1fr);

    }
    .beer-image-container{
      width: 55%;
    }
  }
</style>