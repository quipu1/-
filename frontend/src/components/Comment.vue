<template>
  <div style="padding-top:5px">
    <v-row>
      <v-col class="col-12" style="font-size:15px;">
        <div style="font-size:13px">
          <router-link :to="`/mypage/${comment.userID}`" style="text-decoration:none; color: white; font-size: 1rem;">
            {{comment.nickname}}
          </router-link>
          <p
            class="deleteP"
            style="float:right;font-size:11px;color:darkgray;margin-left:15px"
            @click="deleteComment"
            v-if="comment.userID==this.$store.getters.getUserId"
          >
            삭제
          </p>
          <p style="float:right;font-size:11px;color:silver">{{ comment.created_at }}</p>
          <br>
          {{ comment.content }}
        </div>
      </v-col>
    </v-row>
  </div>
</template>
<script>
import http from '@/util/http-common.js'

export default {
  name: 'Comment',
  props: {comment : Object, feed_id : String},
  // data: () => ({
  //   date: '',
  //   userName:'',
  // }),
  methods: {
    deleteComment() { //댓글 삭제
      // const commentId=this.$props.commentData.comment_id;
      // console.log(this.$props.commentData);
      // this.$store.dispatch('DeleteComment', commentId);
      // if(this.$props.feedData.commentCount>0) this.$props.feedData.commentCount=this.$props.feedData.commentCount-1;
      // let idx=this.$props.commentInfo.findIndex(function(item){return item.comment_id==commentId});
      // console.log(idx);
      // if(idx>-1)this.$props.commentInfo.splice(idx,1);
      http.delete(`feed/${this.feed_id}/comment/${this.comment.id}/delete/`)
      .then(()=>{
        alert('삭제 되었습니다.')
        this.$router.go()
      })
    },
  },
  // created() {
  //   this.date = this.$props.commentData.comment_date.split('T')[0];
  //   this.userName=localStorage.getItem("userName");
  // },
};
</script>

<style scoped>
.deleteP:hover {
  text-decoration: underline;
}
</style>
