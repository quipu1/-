<template>
<div class="warp">
  <main>
    <div>
      <v-container >
        <v-row style="display:flex;justify-content:center;">
          <v-col cols="12" xs="5" lg="7" >
            <v-card
              class="mx-auto"
              tile
              id="card"
            >
              <v-list dense>
                <v-subheader>Setting</v-subheader>
                <v-list-item-group
                  v-model="selectedItem"
                  color="primary"
                >
                  <v-list-item
                    v-for="(item, i) in items"
                    :key="i"
                    :to="item.link"
                  >
                    <v-list-item-icon>
                      <v-icon v-text="item.icon"></v-icon>
                    </v-list-item-icon>
                    <v-list-item-content>
                      <v-list-item-title v-text="item.text"></v-list-item-title>
                    </v-list-item-content>
                  </v-list-item>
                </v-list-item-group>
              </v-list>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </div>

  </main>

</div>
</template>
<script>
  export default {
    name: 'Setting',
    data: () => ({
      selectedItem: null,
      items: [
        { text: '프로필 변경', icon: 'mdi-account', link: '/setting/profile'},
        { text: '선호도 수정', icon: 'mdi-heart', link: '/setting/like'},
        // { text: '비밀번호 변경', icon: 'mdi-key', link: '/setting/password'},
        { text: '회원탈퇴', icon: 'mdi-alert', link: '/exit'},
      ],
    }),
    mounted () {
      window.addEventListener('resize', this.handleResize)
    },
    methods : {
      handleResize() {
        let width= document.body.clientWidth
        var card = document.getElementById('card')
        if (width <= 768){ card.style.width="70%"}
      },
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