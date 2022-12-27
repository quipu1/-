<template>
  <div class="wrap">
    <main>
      <v-file-input
        label="찾고자 하는 맥주 이미지를 입력해주세요"
        filled
        ref="searchImage"
        accept="image/*"
        type="file"
        prepend-icon="mdi-camera"
      ></v-file-input>
      <v-btn color="primary" @click="findbeer()">찾아보기</v-btn>
    </main>
    <main>
      결과가 나올 공간
    </main>
  </div>
</template>

<script src="https://developers.kakao.com/sdk/js/kakao.js" type="text/javascript"></script>
<script>
export default {
  name :'CameraDetection',
  data() {
    input: {
      image: ''
    }
  },
  methods : {
    findbeer() {
      this.input.image = this.$refs.searchImage.file
      console.log("this.input.image")
    }
  }
}
</script>

<style scoped>
  .warp{
  position: relative;
  width: 100%;
  height: 100%;
  }
  main{
  position: relative;
  display: flex;
  justify-content: space-around;
  align-items: center;
  width: 85%;
  height: 100%;
  margin-left: 15%;
  background-color: #F3F3F3;
  margin-bottom: 5%;
  padding: 0 5%;
  }
</style>
