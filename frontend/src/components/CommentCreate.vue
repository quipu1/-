<template>
  <div>
    <v-text-field
      v-model="comment"
      label="댓글을 입력해주세요"
      required
      style="width:90%; float:left;margin:0 20px"
      @keyup.enter="addComment"
    >
    </v-text-field>
    <v-btn
      class="mx-2"
      fab
      x-small
      color="#ccDDff"
      style="margin-top:6px;float:right"
      @click="addComment"
    >
      <v-icon dark>
        mdi-plus
      </v-icon>
    </v-btn>
  </div>
</template>
<script>
import http from '@/util/http-common.js'

export default ({
  data: () => ({
    comment: '',
  }),
  props:{
    feed_id : String
  },
  components:{
  },
  methods:{
    addComment() {
      const Form = new FormData();
      Form.append("userID", this.$store.getters.getUserId)
      Form.append("nickname", this.$store.getters.getNickName)
      Form.append("content", this.comment)

      http.post(`feed/${this.feed_id}/comment/create/`, Form)
      .then(()=>{
        alert('댓글 작성이 완료되었습니다.')
        this.$router.go()
      })
    },
    // async addComment(){ //댓글 추가
    //   if(this.comment=='')return;
    //   let userId=localStorage.getItem('userId');
    //   let feedId=this.$props.feedData.feedId;

    //   this.$store.dispatch("AddComment",{userId:userId,feedId:feedId,commentContent:this.comment})
    //     .then(response=>{
    //         this.$emit("commentChange");  //FeedItem.vue에 이벤트 송신
    //         this.commentNotice(this.$props.feedData.userName,this.comment,this.$props.feedData.feedContent);
    //         this.comment='';  //입력창 초기화 
    //     });      
    // },
    // commentNotice(userName, comment, feedContent) { //댓글 알림  
    //     //userName은 피드를 작성한 유저 네임
    //     let minContent = feedContent.substring(0, 8); //알림에서 피드 내용 앞의 8글자까지만 표시
    //     this.$store.dispatch("CommentNotice", { userName: userName, comment: comment, feedContent: minContent });
    // },
  }
})
</script>
