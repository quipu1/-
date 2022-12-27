<template>
  <v-card
    class="mx-auto mb-5 pb-2"
    color="#CDA27D"
    dark
    max-width="700"
    @click="goToFeedDetailPage(feed.id)"
  >
    <v-card-title>
      <v-list-item class="grow">
        <v-list-item-avatar color="grey darken-3">
          <v-img
            class="elevation-6"
            alt=""
            @click="goToFeedDetailPage(feed.id)"
            src="https://avataaars.io/?avatarStyle=Transparent&topType=ShortHairShortCurly&accessoriesType=Prescription02&hairColor=Black&facialHairType=Blank&clotheType=Hoodie&clotheColor=White&eyeType=Default&eyebrowType=DefaultNatural&mouthType=Default&skinColor=Light"
          ></v-img>
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title @click="goToProfilePage(feed.userID)">{{feed.nickname}}</v-list-item-title>
          <v-list-item-title>{{feed.created_at}}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-card-title>
    <!-- <v-img 
      max-height="400" max-width="500"
      style="margin:auto"
      src="@/assets/drink2.gif">
    </v-img> -->
    <v-card-text class="text-h5 font-weight-bold" style="color:white; cursor:pointer; margin: 20px">
      {{feed.content}}
    </v-card-text>
    <v-card-actions>
      <v-list-item class="grow">
        <v-row
          align="center"
          justify="end"
        >
          <!-- <v-btn light>
            <v-icon class="mr-1">
            mdi-heart
            </v-icon>
            <v-icon color="red" class="mr-1">
            mdi-heart
            </v-icon>
            <span class="subheading mr-2">256</span>
          </v-btn>
          
          <span class="mr-1">·</span> -->
          <v-row v-if="$route.name=='Feed'" justify="end" class="mr-2">
            <v-icon color="black" class="mr-1">
              mdi-message
            </v-icon>
            <!-- 댓글개수 -->
            <!-- <span>2</span> -->
            <span>{{ comments.count }}</span>
          </v-row>
          <v-expansion-panels v-if="$route.name=='FeedDetail'" flat>
            <v-expansion-panel
              v-for="(item, i) in 1"
              :key="i"
              style="background:#CDA27D;"
            >
              <v-expansion-panel-header>
                <v-row justify="end" class="mr-2">
                  <v-icon color="black" class="mr-1">
                    mdi-message
                  </v-icon>
                  <!-- 댓글개수 -->
                  <!-- <span>{{comments.length}}</span> -->
                </v-row>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                <Comment
                  v-for="(comment, idx) in comments"
                  :key="idx"
                  :comment="comment"
                  :feed_id="feed_id"
                />
                <!-- <p>김아무개: 이건 댓글 예시입니다. - [작성일자]</p> -->
                <CommentCreate
                  :feed_id="feed_id"
                />
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
          <!-- <v-btn light>
            <v-icon color="primary" class="mr-1">
              mdi-message
            </v-icon>
            <span class="subheading">6</span>
          </v-btn> -->
        </v-row>
      </v-list-item>
    </v-card-actions>
  </v-card>
</template>
<script>
import Comment from '../components/Comment.vue'
import CommentCreate from '../components/CommentCreate.vue'
import http from '@/util/http-common.js'

export default {
  name : "Feeditem",
  components : {
    Comment,
    CommentCreate
  },
  props : ['feed', 'feed_id'],
  data(){
    return {
      comments : "",
    }
  },
  created() {
    if (this.feed_id !== undefined) {
      http.get(`feed/${this.feed_id}/comment/`)
    .then((res)=>{
      this.comments = res.data
      })
    }
    // http.get(`feed/${this.feed_id}/comment/`)
    // .then((res)=>{
    //   this.comments = res.data
    // })
  },
  methods : {
    goToFeedDetailPage(idx){
      this.$router.push(`/feed/detail/${idx}`)
    },
    goToProfilePage(name){
      this.$router.push(`mypage/${name}/`)
    },
  },
}
</script>

<style>

</style>