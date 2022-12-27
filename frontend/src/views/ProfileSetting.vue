<template>
  <div class="warp">
    <main>
      <v-container >
        <v-row style="display:flex;justify-content:center;">
          <v-col cols="12" xs="5" lg="7" >
            <v-card
              class="mx-auto"
              outlined
            >
              <v-list-item three-line>
                <v-list-item-content>
                  <div class="text-overline mb-4">
                    내 프로필
                  </div>
                  <v-list-item-title class="text-h5 mb-1">
                    <input type="text" v-model="nickName">
                  </v-list-item-title>
                  <v-list-item-subtitle>뱃지리스트가 보이면 좋을듯</v-list-item-subtitle>
                </v-list-item-content>
                <v-list-item-avatar
                  tile
                  size="50%"
                  color="grey"
                > 
                  <div>
                    <input type="text" style="display:none" id="uploadProfileImageForm2" >
                    <img :src=imgSrc alt="프로필" style="width:100%; height:100%;" @click="imageChange">
                    <input type="file" id="uploadProfileImageForm1" accept="image/*" enctype="multipart/form-data">
                  </div>
                </v-list-item-avatar>
              </v-list-item>
              <v-card-actions>
                <v-btn
                  color="primary"
                  @click="onEditProfile"
                >
                  수정완료
                </v-btn>
                <v-btn
                  color="grey"
                  @click="goBack"
                >
                  뒤로가기
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </main>
  </div>
</template>
<script>

export default ({
  name: 'ProfileSetting',
  data() {
    return {
      nickName : "닉네임의 자리",
      imgSrc : require("../assets/astronaut_teemo.jpeg"),
    }
  },
  methods : {
    goBack() {
      this.$router.push('/setting')
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
    padding-top: 5%;
    background-color: #F3F3F3;
  }
  @media screen and (max-width: 768px){
    main{
      width: 100%;
      margin: 0;
    }
  }
</style>
