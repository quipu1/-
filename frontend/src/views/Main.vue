<template>
  <div class="warp">
    <main>
      <div id="mainBackground">
        <div>
          <img :src="mainBackground" alt="" id="mainBackgroundImage">
        </div>
        <span id="mainBackgroundText">YOUR CHOICE IS SIMPLE</span>
      </div>
      <!-- <div id="mainInfoBackground">
        <div class="info-container">
          <i class="fas fa-user fa-3x"></i>
          <span class="info-number">{{todayVisitors}}</span>
          <span class="info-description">TODAY</span>
        </div>
        <div class="info-container">
          <i class="fas fa-beer fa-3x" id="beerIcon"></i>
          <span class="info-number">{{totalBeers}}</span>
          <span class="info-description">TOTAL BEERS</span>
        </div>
        <div class="info-container">
          <i class="fas fa-user-friends fa-3x"></i>
          <span class="info-number">{{totalMembers}}</span>
          <span class="info-description">TOTAL MEMBERS</span>
        </div>
        <div class="info-container">
          <i class="fas fa-car fa-3x"></i>
          <span class="info-number">X</span>
          <span class="info-description">음주운전은 안돼요!</span>
        </div>
      </div> -->
      <BeerList
        v-for="(cls, idx) in beerListTitle"
        :title= "cls.title"
        :ad="cls.address"
        :color="idx"
        :key="idx"
      />
    </main>
  </div>
</template>

<script>
import BeerList from '@/components/BeerList.vue'
import mainBackground from '@/assets/main-background.png'

export default {
  name : 'Main',
  components: {
    BeerList
  },
  data(){
    return {
      mainBackground : mainBackground,
      beerListTitle : [
        {title : "리뷰가 많이 있는 맥주", address : "review"},
        {title : "점수가 가장 높은 맥주", address :"score"},
        {title : "찜이 많은 맥주",  address : "like"},
        // {title : "내가 좋아할 만한 맥주",  address : "like"},
        // {title : "내 친구들이 좋아하는 맥주",  address : "like"},
      ],
      // todayVisitors : 189,
      // totalBeers : 120,
      // totalMembers : 10,
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
    background-color: #F3F3F3;
    padding-bottom: 5%;
  }
  #mainBackground{
    position: relative;
    display: flex;
    justify-content: center;
    align-items: center;
    text-align: center;
    overflow: hidden;
    width: 100%;
    height: auto;
    margin-bottom: 1%;
  }
  #mainBackgroundImage{
    position: relative;
    width: 100%;
    height: 100%;
    margin: 0;
    width: stretch;
  }
  #mainBackgroundText{
    position: absolute;
    font-size: 4em;
    font-weight: bolder;
    color:white;
  }
  #mainInfoBackground{
    position:relative;
    background-color: black;
    width: 100%;
    height: 20vh;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .info-container{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 0 2.5%;
  }
  .info-container > i {
    color: rgb(255, 166, 0);
    text-align: center;
  }
  .info-number{
    font-size: 2em;
    font-weight: bolder;
    color:white;
  }
  .info-description{
    font-size: 1em;
    color:rgb(255, 166, 0);
  }
  @media screen and (max-width: 768px){
    *{
      font-size: 11px;
    }
    main {
      width: 100%;
      margin: 0;
    }
    .info-number{
      font-size: 2em;
    }
    .info-container > i {
      font-size: 5em;
    }
    #beerIcon{
      margin-left: 15%;
    }
    .info-description{
      font-size: 1.5em;
    }
    #mainBackgroundImage{
      height: 200px;
    }
  }

</style>