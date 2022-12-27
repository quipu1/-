<template>
  <div class="warp">
    <main>
      <v-card
        class="mx-auto"
        max-width="344"
      >
        <v-card-text>
          <div>회원탈퇴</div>
          <p class="text-h5 text--primary">
            정말로 탈퇴하실건가요..?
          </p>
          <div class="text--primary">
            아직도 많은 맥주가 당신을 기다리고 있습니다.<br>
            정말로 탈퇴하실건가요...?
          </div>
        </v-card-text>
        <v-card-actions>
          <v-btn
            class="mr-2"
            color="error accent-4"
            @click="reveal = true"
          >
            탈퇴한다
          </v-btn>
          <router-link to="/setting">
            <v-btn
              color="primary"
            >
            다시 생각해볼게요.
            </v-btn>
          </router-link>
        </v-card-actions>

        <v-expand-transition>
          <v-card
            v-if="reveal"
            class="transition-fast-in-fast-out v-card--reveal"
            style="height: 100%;"
          >
            <v-card-text class="pb-0">
              <p class="text-h5 text--primary">
                정말로 탈퇴하시는건가요...?
              </p>
              <p>비어있는 편의점에서 만족할만한 경험을 쌓으시고 이용하셨길 바랍니다.</p>
            </v-card-text>
            <v-card-actions class="pt-0">
              <v-btn
                color="error accent-4"
                @click="exit"
              >
                탈퇴하기
              </v-btn>
              <v-btn
                color="primary accent-4"
                @click="reveal = false"
              >
                뒤로가기
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-expand-transition>
      </v-card>

    </main>

  </div>
</template>
<script>
import http from '@/util/http-common.js'

  export default {
    name: 'Exit',
    data: () => ({
      reveal: false,
    }),
    methods : {
      exit(){{
        http.delete(`/deregister/${this.$store.getters.getUserId}/`)
        .then(()=>{
          localStorage.removeItem("vuex")
          alert('탈퇴 되었습니다.')
          this.$router.push('/')
        })
      }}
    },
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
  .v-card--reveal {
    bottom: 0;
    opacity: 1 !important;
    position: absolute;
    width: 100%;
  }
  @media screen and (max-width: 768px){
    main{
      width: 100%;
      margin: 0;
    }
  }
</style>