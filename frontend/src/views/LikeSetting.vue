<template>
  <div>
    <v-card
      class="mb-12"
      style="display:flex; align-items:center; background-color:transparent;"
      color="lighten-1"
      height="auto"
    >
      <v-container
        style="display:flex; align-items:center; height:100%; justify-content:center"
      >
        <v-btn-toggle  multiple id="beerTasteSelectionContainer"> 
          <!-- v-model="multiple" -->
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
              <v-btn v-bind="attrs" v-on="on" min-width="100" min-height="100">페일에일</v-btn>
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
    <div>
      <div>
        <v-row align="center" justify="center">
          <v-btn color="primary">수정</v-btn>
          <v-btn color="grey" @click="goBack">뒤로가기</v-btn>
        </v-row>
      </div>
    </div>
  </div>
</template>
<script>

export default ({
  name: 'LikeSetting',
  methods: {
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
    background-color: #F3F3F3;
    margin-bottom: 5%;

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
  @media screen and (max-width: 768px){
    main{
      width: 100%;
      margin: 0;
    }
  }
</style>
