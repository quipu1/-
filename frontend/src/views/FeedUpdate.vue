<template>
  <div class="warp">
    <main>
      <v-row justify="center">
        <v-col cols="12" sm="6">
          <v-card>
            <div class="py-5 px-5">
              <form>
                <v-file-input label="File input" filled prepend-icon="mdi-camera" @change="FileSelected"></v-file-input>
                <v-textarea name="text-input" filled label="내용" auto-grow value="" v-model="FeedContent"></v-textarea>
                <v-btn class="mr-4 blue" dark @click="FeedUpload">완료</v-btn>
              </form>
            </div>
          </v-card>
        </v-col>
      </v-row>
    </main>
  </div>
</template>
<script>
import http from '@/util/http-common.js'

export default ({
  name: 'FeedCreate',
  data: () => ({
    FeedContent: "",
    ImageFile: null,
  }),

  methods: {
    // FeedUpload() {
    //   // this.$store.dispatch("FeedUpload", {FeedContent: this.FeedContent, image: this.ImageFile})
    //   const Form = new FormData();
    //   Form.append("feedPhotoPath",this.ImageFile)
    //   Form.append("content", this.FeedContent)
    //   Form.append("userID", this.$store.getters.getUserId)
    //   http.post("feed/update/", Form)
    //   .then((res)=>{
    //     console.log(res)
    //     this.$router.push('/feed')
    //   })
      // if (this.ImageFile == null) {
      //   this.redirect();
      // } else {
      //   setTimeout(() => {
      //     this.redirect();
      //   }, 3000);
      // }
    // },
    FileSelected(file) {
      this.ImageFile = file;
    }
  }
})
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