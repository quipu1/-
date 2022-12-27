<template>
  <div id="FeedContent">
    <v-row>
      <v-col
        v-for="(feed, idx) in feeds"
        :key="idx"
        class="d-flex child-flex"
        cols="2"
        
      >
        <div 
          @click="goToFeedDetailPage(feed.id)"
          class="feed-container"
        >
          {{feed.content}}
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import http from '@/util/http-common.js'

export default {
  name : 'FeedContent',
  data() {
    return {
      feeds : [
      ]
    }
  },
  created(){
    http.get(`feed/list/${this.$store.getters.getUserId}/`)
    .then((res)=>{
      this.feeds = res.data
    })
  },
  mounted () {
    
  },
  methods : {
    goToFeedDetailPage(name) {
      this.$router.push({name : "FeedDetail", params:{ feed_id : name}})
    }
  }

}
</script>

<style scoped>
  #FeedContent{
    padding: 0 10%;
    display: flex;
    justify-content: center;
  }
  v-img {
    cursor: pointer;
  }
  .feed-container{
    width: 100px;
    aspect-ratio: 1;
    display: flex;
    justify-content: center;
    align-items: center;

    background-color: lightgray;

    cursor:pointer;
  }
  @media screen and (max-width: 768px) {
    v-col {
      cols: 6;
    }
  }
  @media screen and (max-width: 360px) {
      
  }
</style>