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
              <div>
                <Feeditem
                  :feed="feed"
                  :feed_id="feed_id"
                />
              </div>
              <div style="float:right; margin-bottom: 10px;">
                <!-- 해당 피드를 작성한유저/현재 로그인중인 유저 -->
                <!-- {{this.feed.userID}}/{{this.$store.getters.getUserId}} -->
                <!-- <v-btn v-if="this.feed.userID == this.$store.getters.getUserId" color="primary" @click="feedupdate">수정</v-btn> -->
                <v-btn v-if="this.feed.userID == this.$store.getters.getUserId" color="error" @click="feeddelete">삭제</v-btn>
              </div>
            <!-- </v-sheet> -->
          </v-col>
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
  name : "FeedDetail",
  props : {
    feed_id : String,
  },
  methods : {
    feedupdate() {
      this.$router.push({
        name: 'FeedCreate',
        params: {
          contentId: this.feed_id,
        }
      })
    },
    feeddelete() {
      http.delete(`feed/${this.feed_id}/delete/`)
      .then(()=>{
        alert('삭제 되었습니다.')
        this.$router.go(-1)
      })
    }
  },

  data(){
    return {
      feed : {
        // userID : "1",
        // id : "",
      },
    }
  },
  created(){
    // this.$store.dispatch('SET_FEED_ID')
    // .then(()=>{
    //   http.get(`feed/${this.$store.getters.getFeedId}`)
    //   .then((res)=>{
    //     this.feed = res.data
    //   })
    // })
    http.get(`feed/${this.feed_id}/`)
    .then((res)=>{
      this.feed = res.data
    })

  },
  components: {
    Feeditem,
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
</style>