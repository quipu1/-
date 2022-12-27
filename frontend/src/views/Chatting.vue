<template>
  <div class="warp">
    <main>
      <div>
        <v-container>
          <v-row>
            <v-col cols="12" sm="8">
              <v-sheet
                class="py-5 px-5"
                rounded="lg"
                min-height="100%"
                style="background:white;"
                elevation="6"
                align-center
              >
                <!-- <Message-Form v-on:submitMessage="sendMessage" class="msg-form"></Message-Form> -->
              </v-sheet>
            </v-col>
            <!-- <v-col cols="12" sm="4">
              <v-sheet
                rounded="lg"
                min-height="500px"
                style="background:white;"
                elevation="6"
              >
                오른쪽 사이드컴포넌트
              </v-sheet>
            </v-col> -->
          </v-row>
        </v-container>
      </div>
    </main>
  </div>
</template>

<script>
// import MessageForm from '@/components/MessageForm.vue'

export default {
  name :'Chatting',
  components: {
    // 'Message-Form' : MessageForm,
  },
  methods: {
    sendMessage(msg) {
      this.pushMsgData({
        from: {
          name: '나',
        },
        msg,
      });
      this.$sendMessage({
        name: this.$route.params.username,
        msg,
      });
    }
  }
}
</script>

<style scoped>
  .msg-form {
    bottom: -28px;
    left: 0;
    right: 0;
  }
  .msg-list {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 60px;
    overflow-x: scroll;
  }
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