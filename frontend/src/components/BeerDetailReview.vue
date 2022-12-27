<template>
  <div id="beerReviews">
    <div
      class="review"
    >
      <div class="review-info">
        <span>{{nickName}}</span>
        <div class="star-rating" v-if="isUserReview">
        <input type="radio" id="5-stars" name="rating" value="5" v-model="userReviewScore"/>
        <label for="5-stars" class="star">&#9733;</label>
        <input type="radio" id="4-stars" name="rating" value="4" v-model="userReviewScore"/>
        <label for="4-stars" class="star">&#9733;</label>
        <input type="radio" id="3-stars" name="rating" value="3" v-model="userReviewScore"/>
        <label for="3-stars" class="star">&#9733;</label>
        <input type="radio" id="2-stars" name="rating" value="2" v-model="userReviewScore"/>
        <label for="2-stars" class="star">&#9733;</label>
        <input type="radio" id="1-star" name="rating" value="1" v-model="userReviewScore"/>
        <label for="1-star" class="star">&#9733;</label>
      </div>
        <!-- <div v-else class="review-star">
          <i class="fas fa-star"
            v-for="(idx) in parseInt(userReviewScore)"
            :key="idx"
          ></i>
        </div> -->
      </div>
      <div class="review-comment">
        <input v-if="isUserReview" v-model="userReviewComment" type="text" id="userReivewCommentForm" @keyup.enter="onCreateReview">
        <span v-else style="font-size:1.2em;">{{userReviewComment}}</span>
      </div>
      <div class="review-button">
        <button @click="onCreateReview" style="background-color: #4C73FD; border-radius:15px; width: 73px; color:white;">등록</button>
      </div>
    </div>
    <div
      v-for="(review, idx) in reviews"
      :key="idx"
      class="review"
    > 
    <div class="review-info">
      <span>{{review.nickname}}</span>
      <div class="review-star">
        <label for="5-stars" class="star" v-for="(idx) in review.score"
          :key="idx">&#9733;</label>
      </div>
    </div>
    <div  class="review-comment">
      {{review.content}}
    </div>
    <div v-if="nickName == review.nickname" class="review-buttons">
      <!-- <button @click="onEditReview" style="background-color: #f0ad4e; border-radius:15px; width:45%; color:white;">수정</button> -->
      <button @click="onDeleteReview(review.id, idx)" style="background-color: #d9534f; border-radius:15px; width: 73px; color:white;">삭제</button>
    </div>
    </div>
  </div>
</template>

<script>
import http from '@/util/http-common.js'

export default {
  name : 'BeerDetailReview',
  props : {
    beer_id : Number,
    beer_eng_name : String,
  },
  created() {
    http.get(`beer/${this.beer_id}/review/`)
    .then((res)=>{
      
      this.reviews = res.data.sort(function(a,b){
        if(a.id > b.id){
          return -1;
        }
        if(a.id < b.id){
          return 1
        }
        return 0
      })
      
      for(let i = 0; i< this.reviews.length;i++){
        if(this.$store.getters.getUserID == this.reviews[i].userID){
          this.aleadyReview = true
          this.userIdx = this.reviews[i].id
        }
      }
      
    })
  },
  data() {
    return {
      reviews : "",
      nickName : this.$store.getters.getNickName,
      isUserReview : true,
      userReviewScore : "",
      userReviewComment : "",

      aleadyReview : "",
      userIdx : "",
    
    }
  },
  computed : {
    // nickName() {
    //   return this.$store.getters.getNickName()
    // },
  },
  methods : {
    onCreateReview(){
      if(this.userReviewScore <= 0){alert('점수를 입력해 주세요'); return}
      if(!this.userReviewComment){alert('리뷰 내용을 입력해주세요'); return}
      if(this.aleadyReview){
        const value = confirm('기존에 있던 리뷰를 삭제하고 새로 작성하시겠습니까?')
        if(value){
          http.delete(`beer/${this.beer_id}/review/${this.userIdx}/delete/`)
          const Form = new FormData();
          const score = parseInt(this.userReviewScore)
          Form.append("score", score)
          Form.append("content", this.userReviewComment)
          Form.append("userID", this.$store.getters.getUserId)

          http.post(`beer/${this.beer_id}/review/create/`, Form)
          .then(()=>{
            this.$router.go()
          })
          this.isUserReview = !this.isUserReview
        }else{
          alert('리뷰 작성이 취소되었습니다.')
        }
      } else{
        const Form = new FormData();
        const score = parseInt(this.userReviewScore)
        Form.append("score", score)
        Form.append("content", this.userReviewComment)
        Form.append("userID", this.$store.getters.getUserId)

        http.post(`beer/${this.beer_id}/review/create/`, Form)
        .then(()=>{
          this.$router.go()
        })
        this.isUserReview = !this.isUserReview
      }
      
    },
    // onEditReview(){
    //   const Form = new FormData();
    //   Form.append("title", "")
    //   Form.append("content", this.userReviewComment)
    //   Form.append("userID", this.$store.getters.getUserId)
    //   http.post(`beer/${this.beer_id}/review/create/`)
    //   this.isUserReview = !this.isUserReview
    // },
    onDeleteReview(idx, start){
      const value = confirm('삭제 하시겠습니까?')
      if (value){
        http.delete(`beer/${this.beer_id}/review/${idx}/delete/`)
        .then(()=>{
          alert('삭제되었습니다.'); 
          this.isUserReview = !this.isUserReview; 
          this.userReviewComment=""; 
          this.userReviewScore= ""
          this.reviews.pop(start)
          this.$router.go()
        })}
    }
  }
}
</script>

<style scoped>
  #beerReviews{
    margin-top: 10%;
    height: 50%;
    overflow: auto;
  }
  .review-create {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: white;
    width: 40vw;
    height: 15%;
    border-radius: 15px;
    margin-bottom: 5%;
  }
  .review-button{
    width: 20%;
    display: flex;
    justify-content: center;
  }
  .review{
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: white;
    width: 70vw;
    height: auto;
    border-radius: 15px;
    margin-bottom: 5%;
    padding: 1% 5%;
  }
  .review-image{
    display: block;
    width: 10%;
    aspect-ratio: 1;
    border-radius: 50%;
    background-color: gray;
  }
  .review-info{
    display: flex;
    /* flex-direction: column; */
    /* justify-content: center; */
    /* align-items: flex-start; */
    width: 30%;
    font-size: 1.5rem;
    margin: 0;
  }
  .review-info > span {
    margin-right: 10%;
  }
  .review-star {
    /* font-size: 1rem; */
    color:rgb(228, 175, 1);;
  }
  .review-comment{
    width: 40%;
    font-size: 1.2rem;
  }
  .review-buttons{
    width: 20%;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
  }
  #userReivewCommentForm{
    border: 1px solid black;
    font-size: 1.2rem;
    border-radius: 5px;
  }
  #userReivewStarRatingForm{
    border: 1px solid black;
    font-size: 1rem;
    border-radius: 5px;
    width: 30%;
  }
  @media screen and (max-width: 768px){
    .review-info > i {
      font-size: 0.1em;
    }
  }
  @media screen and (max-width: 360px) {
    
  }
/* component */

.star-rating {
  display:flex;
  flex-direction: row-reverse;
  font-size:1em;
  justify-content:space-around;
  padding:0 .2em;
  text-align:center;
  width:5em;
}

.star-rating input {
  display:none;
}

.star-rating label {
  color:#ccc;
  cursor:pointer;
}

.star-rating :checked ~ label {
  color:#f90;
}

.star-rating label:hover,
.star-rating label:hover ~ label {
  color:#fc0;
}

/* explanation */

article {
  background-color:#ffe;
  box-shadow:0 0 1em 1px rgba(0,0,0,.25);
  color:#006;
  font-family:cursive;
  font-style:italic;
  margin:4em;
  max-width:30em;
  padding:2em;
}
</style>