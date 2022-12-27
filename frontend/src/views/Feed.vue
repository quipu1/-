<template>
  <div class="warp">
    <main>
      <div>
        <v-container>
          <v-row>
            <v-col cols="12" sm="12">
              <!-- <v-sheet
                class="py-5 px-5"
                rounded="lg"
                min-height="100%"
                style="background:white;"
                elevation="6"
                align-center
              > -->
                <div style="float:right;">
                  <v-btn 
                    color="#D7AC87"
                    @click="createfeed"
                    style="z-index:99;"
                  >
                    <i class="fas fa-pen"> 글쓰기</i>
                  </v-btn>
                </div>
                <div>
                  <Feeditem
                    v-for="(feed, idx) in feeds"
                    :key="idx"
                    :feed="feed"
                  />
                </div>
              <!-- </v-sheet> -->
            </v-col>
            <!-- <v-col cols="12" sm="4">
              <v-sheet
                rounded="lg"
                min-height="500px"
                style="background:white;"
                elevation="6"
              >
                오른쪽 사이드컴포넌트
              </v-sheet>
            </v-col> -->
          </v-row>
        </v-container>
      </div>
    </main>
  </div>
</template>

<script>
import Feeditem from "@/components/Feeditem.vue"
import http from '@/util/http-common.js'

export default {
  name : "Feed",
  data(){
    return {
      feeds : "",
    }
  },
  components: {
    Feeditem,
  },
  created() {
    http.get("feed/list/")
    .then((res)=>{
      console.log(res.data)
      this.feeds = res.data
    })
  },
  methods: {
    createfeed () {
      this.$router.push('/feedcreate')
    },

  }
}
</script>

<style scoped>
  .warp {
    position: relative;
    width: 100%;
    height: 100%;
  }
  main{
    position: relative;
    width: 85%;
    height: 100%;
    margin-left: 15%;
    background-color: #F3F3F3;
    margin-bottom: 5%;

  }
  @media screen and (max-width: 768px){
    main{
      width: 100%;
      margin: 0;
    }
  }
</style>