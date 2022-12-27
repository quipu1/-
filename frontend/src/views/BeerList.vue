<template>
  <div>
    <main>
      <h1 style="text-align:center;">전체 맥주 목록</h1>
      <!-- <v-card class="mb-12" height="auto" width="auto" style="margin-top:5%; background-color:gray; border:none; outline:none;"> -->
        <v-btn-toggle  id="beerTasteClassContainer" > 
          <v-btn class="class-btn" @click="showBeerClass('에일', 1)">
            <span>에일</span>
            <!-- <img class="beer-sample-image" :src="require(`@/assets/beer_types/beer_1.png`)" alt=""> -->
          </v-btn>
          <v-btn class="class-btn" @click="showBeerClass('페일에일',2 )">
            <span>페일에일</span> 
            <!-- <img class="beer-sample-image" :src="require(`@/assets/beer_types/beer_2.png`)" alt=""> -->
          </v-btn>
          <v-btn class="class-btn" @click="showBeerClass('IPA', 3)">
            IPA
            <!-- <img class="beer-sample-image" :src="require(`@/assets/beer_types/beer_3.png`)" alt=""> -->
          </v-btn>
          <v-btn class="class-btn" @click="showBeerClass('드라이', 4)">
            드라이
            <!-- <img class="beer-sample-image" :src="require(`@/assets/beer_types/beer_4.png`)" alt=""> -->
          </v-btn>
          <v-btn class="class-btn" @click="showBeerClass('라거', 5)">
            라거
            <!-- <img class="beer-sample-image" :src="require(`@/assets/beer_types/beer_5.png`)" alt=""> -->
          </v-btn>
          <v-btn class="class-btn" @click="showBeerClass('밀맥주', 6)">
            밀맥주
            <!-- <img class="beer-sample-image" :src="require(`@/assets/beer_types/beer_6.png`)" alt=""> -->
          </v-btn>
          <v-btn class="class-btn" @click="showBeerClass('흑맥주', 7)">
            흑맥주
            <!-- <img class="beer-sample-image" :src="require(`@/assets/beer_types/beer_7.png`)" alt=""> -->
          </v-btn>
          <v-btn class="class-btn" @click="showBeerClass('필스너', 8)">
            필스너
            <!-- <img class="beer-sample-image" :src="require(`@/assets/beer_types/beer_8.png`)" alt=""> -->
          </v-btn>
          <v-btn class="class-btn" @click="showBeerClass('무알코올', 9)">
            무알코올
            <!-- <img class="beer-sample-image" :src="require(`@/assets/beer_types/beer_9.png`)" alt=""> -->
          </v-btn>
          <v-btn class="class-btn" @click="showBeerClass('과일', 10)">
            과일
            <!-- <img class="beer-sample-image" :src="require(`@/assets/beer_types/beer_10.png`)" alt=""> -->
          </v-btn>
          <v-btn class="class-btn" @click="showBeerClass('기타', 11)">
            기타
            <!-- <img class="beer-sample-image" :src="require(`@/assets/beer_types/beer_11.png`)" alt=""> -->
          </v-btn>
        </v-btn-toggle>
        <!-- </v-container> -->
      <!-- </v-card> -->
      <BeerTable
        :title="value"
        :classNum="classNum"
      />
    </main>
  </div>
</template>

<script>
// import http from '@/util/http-common.js'

import BeerTable from '@/components/BeerTable.vue'

export default {
  name : "BeerList",
  components: {
    BeerTable,
  },
  data(){
    return {
      data : '',
      value : '에일',
      classNum : 1,
    }
  },
  methods : {
    showBeerClass(text, classNum){
      this.value = text
      this.classNum = classNum
    }
  }

}
</script>

<style scoped>
  main{
    position: relative;
    width: auto;
    margin-left: 15%;
    margin-top: 0.3%;
    border-top: 1px solid gray;
    padding-top: 5%;
    background-color: #F3F3F3;
    height: 100%;
    display: flex;
    flex-direction: column;
    /* justify-content: center; */
    align-items: center;
    margin-bottom: 5%;

  }
  #beerTasteClassContainer{
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    justify-content: center;
    align-items: center;
    font-size: 1.5em;
    justify-items: center;
    gap: 1%;
    width: 40%;
    /* height: 100%; */
    aspect-ratio: 1;
    margin-top: 5%;
    background-color:transparent;
    
  }
  .class-btn{
    width: 200px;
    height: 100% !important;
    padding: 0;
    font-size: 1em;
    background-color: white;
    font-weight: bolder;
    box-sizing: border-box;
  }
  .v-btn__content{
    width: 10% !important;
  }
  .beer-sample-image{
    margin-left: 5%;
    width: 5%;
  }
  @media screen and (max-width: 768px){
    main{
      width: 100%;
      margin: 0;
    }
    main > h1{
      font-size: 2.5em;
    }
    #beerTasteClassContainer{
      width: 60%;
    }
    #class-btn{
      font-size: 0.5em;
    }

  }
</style>