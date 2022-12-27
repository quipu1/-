<template>
  <div class="wrap">
    <div id="loginBeer">
      <div class="right">
        <v-card
          class="mb-12"
          style="display:flex; justify-content:space-around;"
          color="lighten-1"
          height="800px"
        >
          <v-container
            style="display:flex; 
                    flex-direction:column; 
                    justify-content:space-around;"
          >
            <v-btn-toggle 
              class="beerSelectionPart"
              v-for="(game, idx) in this.beerWorldCup"
              :key="idx"
            >
              <div class="beerSelection">
                <span>{{game.beer1.beer_name}}</span>
                <img :src="require(`@/assets/맥주이미지모음/${beer.beer1.imgSrc}.png`)" alt="">
                <v-btn min-width="50" @click="beerWin(beer.beer1.beer_name)"><i class="fas fa-check"></i></v-btn>
              </div>
              <div class="beerSelection">
                <span>{{beer.beer2.beer_name}}</span>
                <img :src="require(`@/assets/맥주이미지모음/${beer.beer2.imgSrc}.png`)" alt="">
                <v-btn min-width="50" @click="beerWin(beer.beer2.beer_name)"><i class="fas fa-check"></i></v-btn>
              </div>
            </v-btn-toggle>
          </v-container>
        </v-card>
        <v-btn
          color="success"
          @click="submit"
        >
          완료
        </v-btn>
      </div>
    </div>
  </div>
</template>

<script>
// import drink2 from '@/assets/drink2.gif'
// import http from '@/util/http-common.js'

export default {
  name : 'WorldCup',
  data(){
    return {
      beerWorldCup : this.$store.getters.getWorldCup
    }
  }

}
</script>

<style scoped>
.warp{
  position: relative;
}
#loginBeer{
  width : 100vw;
  height : 100vh;
  background-image: url("../assets/drink2.gif");
  background-repeat: no-repeat;
  background-size: cover;
}
.right{
  width: 50%;
  height: 100%;
  float: right;
  background: white;
  /* display: flex;
  justify-content: center;
  flex-direction: column; */
  /* align-items: center; */
}
</style>