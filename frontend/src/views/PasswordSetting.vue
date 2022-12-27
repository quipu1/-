<template>
  <div class="warp">
    <main>
      <div>
        <v-container >
          <v-row style="display:flex;justify-content:center;">
            <v-col cols="12" xs="5" lg="7" >
              <v-card
                class="mx-auto py-5 px-5"
                tile
                id="card"
              >
                <v-text-field
                  v-model="user_pw"
                  :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                  :rules="[rules.required, rules.min]"
                  :type="show1 ? 'text' : 'password'"
                  name="input-1"
                  label="새 비밀번호 입력"
                  hint="이전과 다른 비밀번호를 입력해주세요"
                  counter
                  @click:append="show1 = !show1"
                ></v-text-field>
                <v-text-field
                  v-model="user_pw_chk"
                  :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                  :rules="[rules.required, rules.min]"
                  :type="show2 ? 'text' : 'password'"
                  name="input-2"
                  label="비밀번호 확인"
                  hint="위와 똑같이 입력해주세요"
                  counter
                  @click:append="show2 = !show2"
                ></v-text-field>
                <br>
                <v-btn color="primary" @click="pwchange">완료</v-btn>
              </v-card>
            </v-col>
          </v-row>
        </v-container>
      </div>
    </main>
  </div>
</template>
<script>
export default ({
  name: 'PasswordSetting',
  data() {
    return {
      show1: false,
      show2: false,
      password: '',
      rules: {
        required: value => !!value || 'Required.',
        min: value => value.length >= 8 || 'Min 8 characters',
      }
    }
  },
  methods: {
    pwchange() {
      
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
  #signupForm{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    /* filter: drop-shadow(0px 4px 4px rgba(0, 0, 0, 0.25)); */
    font-size: 1.2em;
  }
  @media screen and (max-width: 768px){
    main{
      width: 100%;
      margin: 0;
    }
  }
</style>