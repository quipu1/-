<template>
  <div class="warp">
    <main>
      <div id="map"></div>
      <div id="getGeoForm">
        <h1>맥주팟 구하기</h1>
        <button id="onMyLocationBtn" @click="onMyLocation">내 주변 친구 찾기</button>
        <div style="display:flex;justify-content:space-around;align-items:center; flex-direction: column;width: 100%;"> 
          <div id="sendMyLocationForm">
            <span>위치 정보 제공 동의</span><input type="checkbox" v-model="sendMyLocation" @click="checkMyLocation">
          </div>
          <div id="deleteMyLocationForm">
            <span>위치 정보 제거 하기</span><input type="checkbox" v-model="delMyLocation" @click="deleteMyLocation">
          </div>      
        </div>
      </div>
    </main>
  </div>
</template>

<script type="text/javascript" src="//dapi.kakao.com/v2/maps/sdk.js?appkey=3f0209d163b7148dd630a50607d3dc8f"></script>
<script>
import http from '@/util/http-common.js'

export default {
  name :'BeerParty',
  data(){
    return {
      sendMyLocation : false,
      delMyLocation : false,
      data : "",
      latitude: '',
      longitude: '',
      textContent: '',
      map : null,
      userList : "",
      markers : [],
      infowindow : [],

    }
  },
  created(){
    // http.get(`user/${this.$store.getters.getUserId}/where/`)
    // .then((res)=>{
    //   userList = res.data
    // })
    // this.initMap();
  },
  mounted(){
    if (window.kakao && window.kakao.maps) {
      if(!("geolocation" in navigator)) {
        this.textContent = 'Geolocation is not available.';
        return;
      }
      navigator.geolocation.getCurrentPosition(pos => {
        this.latitude = pos.coords.latitude;
        this.longitude = pos.coords.longitude;
        // this.initMap(this.latitude, this.longitude);
        this.initMap(35.1595454, 126.8526012)
      }, err => {
        this.textContent = err.message;
      })
    } else {
      const script = document.createElement("script");
      script.onload = () => kakao.maps.load(this.initMap);
      script.src = "//dapi.kakao.com/v2/maps/sdk.js?autoload=false&appkey=3f0209d163b7148dd630a50607d3dc8f";
      document.head.appendChild(script);
    }
  },
  update : {

  },
  methods : {
    initMap(latitude, longitude) {
      const container = document.getElementById("map");
      const options = {
        center: new kakao.maps.LatLng(latitude, longitude),
        level: 3,
      };
      var map = new kakao.maps.Map(container, options);
      this.map = map
    },
    checkMyLocation(){

    },
    onMyLocation(){
      if(!this.sendMyLocation){alert('위치 정보 제공에 동의해주세요');return;}
      navigator.geolocation.getCurrentPosition(pos => {
        this.latitude = pos.coords.latitude;
        this.longitude = pos.coords.longitude; 
        this.map.panTo(new kakao.maps.LatLng(this.latitude, this.longitude));

        let latitudeForm = new FormData();
        latitudeForm.append("latitude", this.latitude) 
        http.post(`user/${this.$store.getters.getUserId}/update/latitude/`, latitudeForm)

        let logitudeForm = new FormData();
        logitudeForm.append("logitude", this.longitude) 
        http.post(`user/${this.$store.getters.getUserId}/update/logitude/` , logitudeForm)

        http.get(`user/${this.$store.getters.getUserId}/where/`)
        .then((res)=>{

          for (let i = 0 ; i < res.data.length ; i++) {
            const longitude = res.data[i].latitude
            const latitude = res.data[i].logitude

            var imgSrc = require(`@/assets/beer2.png`)
            var imageSize = new kakao.maps.Size(50, 50);

            var markerImage = new kakao.maps.MarkerImage(imgSrc, imageSize)
            var markerPosition  = new kakao.maps.LatLng(longitude,latitude);   
            var marker = new kakao.maps.Marker({map : this.map, position: markerPosition, clickable : true, image : markerImage})
            marker.setMap(this.map);
            var content = 
            '<div style="background-color:white; width: 200px; height:40px; display:flex; justify-content:center; align-items:center; flex-direction: column;">' + 
            '   <div style="width: 150px;display:flex; justify-content:space-around;">' +
            // '     <div style="width: 30%; aspect-ratio: 1; border-radius: 50%; background-color: gray;"></div>' +
            // `     <a href="https://localhost:3000/mypage/${res.data[i].user_id}">${res.data[i].nickname}</a>`  +
            `     <a href="https://j5c205.p.ssafy.io/mypage/${res.data[i].user_id}">${res.data[i].nickname}</a>`  +
            // `     <a href="https://localhost:3000/api/chat/${res.data[i].user_id}/?username=${this.$store.getters.getNickName}">채팅하기</a>`  +
            `     <a href="https://j5c205.p.ssafy.io/api/chat/${res.data[i].user_id}/?username=${this.$store.getters.getNickName}">채팅하기</a>`  +
            '   </div>' +
            '</div>';
            var infowindow = new kakao.maps.InfoWindow({
              content: content,   
              position: marker.getPosition(),
              removable : true,
            });

            function makeOverListener(map, marker, infowindow) {
              return function() {
                infowindow.open(map, marker);
              };
            }
            kakao.maps.event.addListener(marker, 'click', makeOverListener(this.map, marker, infowindow));
        }
        })
      })

    },
    deleteMyLocation(){
      const value = confirm('맥주팟의 맵에서 자신을 제거하시겠습니까?')
      if(value){
        let latitudeForm = new FormData();
        latitudeForm.append("latitude", 0) 
        http.post(`user/${this.$store.getters.getUserId}/update/latitude/`, latitudeForm)

        let logitudeForm = new FormData();
        logitudeForm.append("logitude", 0) 
        http.post(`user/${this.$store.getters.getUserId}/update/logitude/` , logitudeForm)
        alert('삭제되었습니다.')
        this.$router.go()
      }
    },
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
  /* #mapContainer{
    display: flex;
    justify-content: space-around;
    align-items: center;
  } */
  #map {
    width: 60%;
    height: 500px;
  }
  #getGeoForm{
    width: 30%;
    height: 400px;
    background-color: lightgray;
    border-radius: 15px;

    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;

  }
  #onMyLocationBtn{
    width: 50%;
    height: 20%;
    border-radius: 15px;
    background-color: white;
    border: 1px solid black;
  }
  #sendMyLocationForm{
    width: 60%;
    display: flex;
    justify-content: space-around;
    align-items: center;
  }
  #deleteMyLocationForm{
    width: 60%;
    display: flex;
    justify-content: space-around;
    align-items: center;
}
</style>