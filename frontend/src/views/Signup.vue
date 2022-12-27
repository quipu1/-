<template>
  <div class="wrap">
    <div id="loginBeer">
      <div class="right">
        <v-stepper v-model="e1">
          <v-stepper-header>
            <v-stepper-step
              :complete="e1 > 1"
              step="1"
            >
              연령대, 성별
            </v-stepper-step>
            <v-divider></v-divider>
            <v-stepper-step
              :complete="e1 > 2"
              step="2"
            >
              맥주 취향
            </v-stepper-step>
            <v-divider></v-divider>
            <v-stepper-step step="3">
              마셔본 맥주 평가
            </v-stepper-step>
          </v-stepper-header>
          <v-stepper-items>
            <v-stepper-content step="1">
              <v-card
                class="mb-12"
                color="lighten-1 transparent"
                style="display:flex; align-items:center;"
                height="700px"
              >
                <div class="container">
                  <v-row>
                    <v-col
                      cols="12"
                      sm="12"
                      class="py-2"
                    >
                    </v-col>
                    <v-col
                      cols="12"
                      sm="12"
                      class="py-2"
                    >
                      <v-btn-toggle v-model="age" mandatory> 
                        <v-btn>
                          20
                        </v-btn>
                        <v-btn>
                          30
                        </v-btn>
                        <v-btn>
                          40
                        </v-btn>
                        <v-btn>
                          50
                        </v-btn>
                        <v-btn>
                          60대 이상
                        </v-btn>
                      </v-btn-toggle>
                    </v-col>
                    <v-col>
                      <v-btn-toggle v-model="gender" mandatory>
                        <v-btn>
                          남자
                        </v-btn>
                        <v-btn>
                          여자
                        </v-btn> 
                      </v-btn-toggle>
                    </v-col>
                  </v-row>  
                </div>
              </v-card>
              <v-btn
                style="background-color:primary;"
                color="primary"
                @click="e1 = 2"
              >
                다음
              </v-btn>
            </v-stepper-content>
            <v-stepper-content step="2">
              <v-card
                class="mb-12"
                style="display:flex; align-items:center; background-color:transparent;"
                color="lighten-1"
                height="700px"
              >
                <v-container
                  style="display:flex; align-items:center; height:100%; justify-content:center text-align:center; flex-direction:column;"
                > 
                
                  <h1 style="margin-bottom:20%;">좋아하는 종류 3가지를 선택해주세요</h1>
                  <div>
                    <v-btn-toggle v-model="beerClass" multiple id="beerTasteSelectionContainer"> 
                      <v-tooltip top>
                        <template v-slot:activator="{ on, attrs }">
                          <v-btn v-bind="attrs" v-on="on" min-width="100" min-height="100">에일</v-btn>
                        </template>
                        <span>
                          색이 진하고 탄산이 적으며 과일향이나 꽃향기와 같은 풍부한 향을 가지는 맥주입니다. <br>
                          기네스, 호가든, 파울라너 등이 있습니다.
                        </span>
                      </v-tooltip>
                      <v-tooltip top>
                        <template v-slot:activator="{ on, attrs }">
                          <v-btn v-bind="attrs" v-on="on" min-width="100" min-height="100" >페일에일</v-btn>
                        </template>
                        <span>
                          에일의 한 종류로 영국에서 처음 제조되었고 전체적으로 밝은 빛을 띄며 쓴 맛과 풍부한 향이 특징입니다. <br>
                          대강 페일에일, 강서맥주 등이 있습니다.
                          (여기서 '페일'은 밝은색이라는 의미를 가집니다.)
                        </span>
                      </v-tooltip>
                      <v-tooltip top>
                        <template v-slot:activator="{ on, attrs }">
                          <v-btn v-bind="attrs" v-on="on" min-width="100" min-height="100">IPA</v-btn>
                        </template>
                        <span>
                          인디안 페일 에일(Indian Pale Ale)의 약자로 홉이 많이 들어가 맛과 향이 매우 강한 페일에일의 한 종류입니다.
                        </span>
                      </v-tooltip>
                      <v-tooltip top>
                        <template v-slot:activator="{ on, attrs }">
                          <v-btn v-bind="attrs" v-on="on" min-width="100" min-height="100">드라이</v-btn>
                        </template>
                        <span>
                          가볍고 부드럽다고 느낄 수 있는 맥주로 청량감이라는 분명한 특징이 있지만 사람에 따라서 밍밍하다고 느낄 수도 있는 맥주입니다.<br>
                          대표적으로 아사히 드라이 맥주가 있습니다.
                        </span>
                      </v-tooltip>
                      <v-tooltip top>
                        <template v-slot:activator="{ on, attrs }">
                          <v-btn v-bind="attrs" v-on="on" min-width="100" min-height="100">라거</v-btn>
                        </template>
                        <span>
                          투명한 황금빛과 가볍고 밋밋한 향 하지만 강한 탄산감이 특징인 맥주입니다. <br>
                          라거는 종류가 많지만 대표적으로 카스, 하이트, 칭따오, 하얼빈 등 여러가지가 있습니다.
                        </span>
                      </v-tooltip>
                      <v-tooltip top>
                        <template v-slot:activator="{ on, attrs }">
                          <v-btn v-bind="attrs" v-on="on" min-width="100" min-height="100">밀맥주</v-btn>
                        </template>
                        <span>
                          밀맥주는 보리와 밀을 섞어서 만드는 맥주로 홉을 독특하게 쓰기에 특유의 향이 나며, 세부분류는 바이젠, 위트비어로 나뉩니다. <br>
                          에델바이스, 파울라너, 바바리아, 블랑1664, 프란치스카너 등이 있습니다.
                        </span>
                      </v-tooltip>
                      <v-tooltip top>
                        <template v-slot:activator="{ on, attrs }">
                          <v-btn v-bind="attrs" v-on="on" min-width="100" min-height="100">흑맥주</v-btn>
                        </template>
                        <span>
                          맛이 강할거같지만 실제로는 맛이 부드럽고 거품이 풍부해서 목넘김이 좋습니다.<br>
                          대표적으로는 기네스, 파울라너 둔켈이 있습니다.
                        </span>
                      </v-tooltip>
                      <v-tooltip top>
                        <template v-slot:activator="{ on, attrs }">
                          <v-btn v-bind="attrs" v-on="on" min-width="100" min-height="100">필스너</v-btn>
                        </template>
                        <span>
                          라거의 한 종류로 투명한 황금빛과 시원한 청량감에 더해 홉의 쌉싸름한 맛과 풍미가 강조된 것이 특징입니다. 일반 라거에 비해 더욱 강한 쓴맛과 깊은 풍미가 있습니다.<br>
                          대표적으로 필스너우르겔이 있습니다.
                        </span>
                      </v-tooltip>
                      <v-tooltip top>
                        <template v-slot:activator="{ on, attrs }">
                          <v-btn v-bind="attrs" v-on="on" min-width="100" min-height="100">무알코올</v-btn>
                        </template>
                        <span>
                          국내법상 알코올 함량을 별도로 표기하지 않은 도수 1% 미만의 음료 <br>
                          많이 보이는 밀러 라이트와 하이트 제로 정도의 맥주가 있습니다.
                        </span>
                      </v-tooltip>
                      <v-tooltip top>
                        <template v-slot:activator="{ on, attrs }">
                          <v-btn v-bind="attrs" v-on="on" min-width="100" min-height="100">과일</v-btn>
                        </template>
                        <span>
                          과일맛이 나는 맥주로 대표적으론 라들러, 피치, 청포도, 자몽 등 과일이름이 들어간 맥주들을 편의점에서 쉽게 찾아볼 수 있습니다.
                        </span>
                      </v-tooltip>
                      <v-tooltip top>
                        <template v-slot:activator="{ on, attrs }">
                          <v-btn v-bind="attrs" v-on="on" min-width="100" min-height="100">기타</v-btn>
                        </template>
                        <span>기타 다른 맥주들</span>
                      </v-tooltip>
                      <v-tooltip top>
                        <template v-slot:activator="{ on, attrs }">
                          <v-btn v-bind="attrs" v-on="on" min-width="100" min-height="100">모름</v-btn>
                        </template>
                        <span>아직 잘 모르시는 분들은 이걸 선택해주세요.</span>
                      </v-tooltip>
                    </v-btn-toggle>
                  </div>
                </v-container>
                <div style="float: right bottom;">
                  <v-dialog
                    v-model="dialog"
                    scrollable
                    max-width="400px"
                  >
                    <template v-slot:activator="{ on, attrs }">
                      <v-btn color="primary" dark v-bind="attrs" v-on="on">
                        <v-icon small>mdi-help</v-icon>
                      </v-btn>
                    </template>
                    <v-card>
                      <v-card-title>맥주정보</v-card-title>
                      <v-divider></v-divider>
                      <v-card-text style="height: 300px;">
                        1. 에일: 색이 진하고 탄산이 적으며 과일향이나 꽃향기와 같은 풍부한 향을 가지는 맥주입니다. <br>
                        기네스, 호가든, 파울라너 등이 있습니다.<br><br>

                        2. 페일에일: 에일의 한 종류로 영국에서 처음 제조되었고 전체적으로 밝은 빛을 띄며 쓴 맛과 풍부한 향이 특징입니다. <br>
                        대강 페일에일, 강서맥주 등이 있습니다.<br><br>

                        3. IPA: 인디안 페일 에일(Indian Pale Ale)의 약자로 홉이 많이 들어가 맛과 향이 매우 강한 페일에일의 한 종류입니다.<br><br>

                        4. 드라이: 가볍고 부드럽다고 느낄 수 있는 맥주로 청량감이라는 분명한 특징이 있지만 사람에 따라서 밍밍하다고 느낄 수도 있는 맥주입니다.<br>
                        대표적으로 아사히 드라이 맥주가 있습니다.<br><br>

                        5. 라거: 투명한 황금빛과 가볍고 밋밋한 향 하지만 강한 탄산감이 특징인 맥주입니다. <br>
                        라거는 종류가 많지만 대표적으로 카스, 하이트, 칭따오, 하얼빈 등 여러가지가 있습니다.<br><br>

                        6. 밀맥주: 밀맥주는 보리와 밀을 섞어서 만드는 맥주로 홉을 독특하게 쓰기에 특유의 향이 나며, 세부분류는 바이젠, 위트비어로 나뉩니다. <br>
                        에델바이스, 파울라너, 바바리아, 블랑1664, 프란치스카너 등이 있습니다.<br><br>

                        7. 흑맥주: 맛이 강할거같지만 실제로는 맛이 부드럽고 거품이 풍부해서 목넘김이 좋습니다.<br>
                        대표적으로는 기네스, 파울라너 둔켈이 있습니다.<br><br>

                        8. 필스너: 라거의 한 종류로 투명한 황금빛과 시원한 청량감에 더해 홉의 쌉싸름한 맛과 풍미가 강조된 것이 특징입니다. 일반 라거에 비해 더욱 강한 쓴맛과 깊은 풍미가 있습니다.<br>
                        대표적으로 필스너우르겔이 있습니다.<br><br>

                        9. 무알코올: 국내법상 알코올 함량을 별도로 표기하지 않은 도수 1% 미만의 음료 <br>
                        많이 보이는 밀러 라이트와 하이트 제로 정도의 맥주가 있습니다.<br><br>

                        10 과일: 과일맛이 나는 맥주로 대표적으론 라들러, 피치, 청포도, 자몽 등 과일이름이 들어간 맥주들을 편의점에서 쉽게 찾아볼 수 있습니다.<br><br>
                      </v-card-text>
                    </v-card>
                  </v-dialog>
                </div>
              </v-card>
              <v-btn
                color="primary"
                @click="getBeerList"
              >
                맥주 선택 완료
              </v-btn>
              <!-- <v-btn
                color="primary"
                 @click="e1 = 3"
              >
                다음
              </v-btn> -->
              <v-btn 
                text
                @click="e1 = 1"
              >
                뒤로가기
              </v-btn>
            </v-stepper-content>
            <v-stepper-content step="3" style="text-align:center;">
              <h1>둘 중에 더 마음에 드는 맥주를 선택해 주세요</h1> 
              <v-card
                class="mb-12"
                style="display:flex; justify-content:space-around;"
                color="lighten-1"
                height="750px"
              >
                <v-container
                  style="display:flex; 
                         flex-direction:column; 
                         justify-content:space-around;"
                >
                  <v-btn-toggle 
                    class="beerSelectionPart"
                    v-for="(game, idx) in beerWorldCup"
                    :key="idx"
                  >
                    <div class="beerSelection">
                      <span>{{game.beer1.beer_name}}</span>
                      <img :src="require(`@/assets/맥주이미지모음/${game.beer1.imgSrc}.png`)" alt="">
                      <v-btn min-width="25" @click="beerWin(game.beer1.beer_id, idx)"><i class="fas fa-check"></i></v-btn>
                    </div>
                    <div class="beerSelection">
                      <span>{{game.beer2.beer_name}}</span>
                      <img :src="require(`@/assets/맥주이미지모음/${game.beer2.imgSrc}.png`)" alt="">
                      <v-btn min-width="25" @click="beerWin(game.beer2.beer_id, idx)"><i class="fas fa-check"></i></v-btn>
                    </div>
                  </v-btn-toggle>
                </v-container>
              </v-card>
              <v-btn
                color="success"
                @click="submit"
              >
                완료
              </v-btn>
               <v-btn 
                text
                @click="e1 = 2"
              >
                뒤로가기
              </v-btn>
            </v-stepper-content>
          </v-stepper-items>
        </v-stepper>
      </div>
    </div>
  </div>
</template>

<script>

import drink2 from '@/assets/drink2.gif'
import http from '@/util/http-common.js'
  export default {
    name: 'Signup',
    data () {
      return {
        drink2 : drink2,
        e1: 1,
        text: 'center',
        icon: 'justify',
        toggle_none: null,
        toggle_one: 0,
        toggle_exclusive: null,
        toggle_multiple: [],
        beerData : [],
        winBeer : [],
        age : "",
        gender : "",
        dialog : "",

        beerClass : [],
        beerWorldCup : [],
        win : [null, null, null]


      }
    },
    methods : {
      submit() {
        if(this.win[0] && this.win[1] && this.win[2]) {
        this.$router.push('/main')
        const Form = new FormData();

        if(this.age == 0){Form.append("age", 20)}
        if(this.age == 1){Form.append("age", 30)}
        if(this.age == 2){Form.append("age", 40)}
        if(this.age == 3){Form.append("age", 50)}
        if(this.age == 4){Form.append("age", 60)}
        http.post(`user/${this.$store.getters.getUserId}/update/age/`, Form)
        if(this.gender==0){Form.append("gender", 0)}
        if(this.gender==1){Form.append("gender", 1)}
        http.post(`user/${this.$store.getters.getUserId}/update/gender/`, Form)

        const form = new Set(this.win)
        const arrayform = Array.from(form)

        for (let i = 0; i< arrayform.length; i++){
          const review = new FormData();
          review.append("score", 5)
          review.append("content", "")
          review.append("userID", this.$store.getters.getUserId)
          // const review = {"score" : 5, "userID" : this.$store.getters.getUserId, "content": ""}
          http.post(`beer/${arrayform[i]}/review/create/`, review)
        }
        this.$router.push({name: "Main"})
        }else{
          alert('모든 승부를 결정해 주세요')
        }
        
      },
      beerWin(id, idx) {

        this.win[idx] = id
        console.log(this.win)
      },
      select(e) {
        console.log(e)
      },
      getBeerList(){
        this.beerData = []
        if(this.beerClass.length === 3){
        for (let i = 0; i < this.beerClass.length; i++){
          switch (this.beerClass[i]){
            case 0:
              this.beerData.push({"beer_name" : "제주 펠롱 에일", "imgSrc" : "제주펠롱에일", "beer_id" : 75})
              break
            case 1:
              this.beerData.push({ "beer_name" : "광화문", "imgSrc" :"광화문", "beer_id" : 3})
              break
            case 2:
              this.beerData.push({ "beer_name" : "구스 아일랜드 IPA", "imgSrc" : "구스아일랜드IPA", "beer_id" : 6})
              break
            case 3:
              this.beerData.push({ "beer_name" : "기네스 드라우트", "imgSrc" : "기네스드라우트", "beer_id" : 15})
              break
            case 4:
              this.beerData.push({"beer_name" : "카스 프레쉬", "imgSrc" : "카스", "beer_id" : 78})
              break
            case 5:
              this.beerData.push({ "beer_name" : "1664블랑", "imgSrc" :"블랑", "beer_id" : 1})
              break
            case 6:
              this.beerData.push({ "beer_name" : "코젤 다크", "imgSrc" : "코젤다크", "beer_id" : 82})
              break
            case 7:
              this.beerData.push({ "beer_name" : "필스너 우르켈", "imgSrc" : "필스너우르켈", "beer_id" : 106})
              break
            case 8:
              this.beerData.push({ "beer_name" : "하이트 제로", "imgSrc" :"하이트제로", "beer_id" : 114})
              break
            case 9:
              this.beerData.push({ "beer_name" : "써머스비 애플", "imgSrc" : "써머스비애플", "beer_id" : 54})
              break
            case 10:
              this.beerData.push({ "beer_name" : "구스 아일랜드 썸머 타임", "imgSrc" : "구스아일랜드썸머타임", "beer_id" : 11})
              break
            case 11:
              this.beerData.push({ "beer_name" : "기네스 드라우트", "imgSrc" : "기네스드라우트", "beer_id" : 15})
              break
          }
        }
        this.beerWorldCup = []
        for(let i = 0; i < this.beerData.length-1; i++){
          for (let j = i+1; j < this.beerData.length; j++ ){
            this.beerWorldCup.push({"beer1" : this.beerData[i], "beer2": this.beerData[j]})
          }
        }  
        this.e1 = 3;

      }else{
        alert('3개 까지 선택해주세요')
      }
      
      },

    }
  }
</script>
<style scoped>
.warp{
  position: relative;
}
#loginBeer{
  width : 100vw;
  height : 100vh;
  background-image: url("../assets/drink2.gif");
  background-repeat: no-repeat;
  background-size: cover;
}
.right{
  width: 50%;
  height: 100%;
  float: right;
  background: white;
  /* display: flex;
  justify-content: center;
  flex-direction: column; */
  /* align-items: center; */
}
.text-center{
  text-align: center;
}
#title{
  font-size: 56px;
  margin-top: 30%;
  margin-bottom: 5%;
}
#subTitle{
  font-size: 24px;
  margin-bottom: 20%;
}
#loginBtn{
  display: flex;
  justify-content: center;
  /* margin-bottom: 10%; */
  cursor: pointer;
}
#btnImage{
  width: 250px;
}
.beerSelectionPart{
  display: flex;
  justify-content: space-between;
  align-items: center;
  height: 20%;
}

.beerSelection {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  width: 150px;
  height: 100px;
}
.beerSelection > img{
  width: 100px;

}
.beerSelectionPart > v-btn{
  margin: 0 5%;
  width: 10px;
}

.beerSelectionPart > div > img {
  /* width: 100px; */
  width: auto;
  height: 100%;
  object-fit: cover;
}

#beerTasteSelectionContainer{
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  align-items: center;
  gap: 1%;
}
#beerTasteSelectionContainer > v-btn{
  border-radius: 25%;
}

@media screen and (max-width : 768px) {
  .right{
    width: 100%;

    height: auto;
  }

}

</style>