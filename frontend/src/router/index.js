import Vue from 'vue'
import VueRouter from 'vue-router'

import Login from '../views/Login.vue'
import SignupUser from '../views/SignupUser.vue'
import Signup from '../views/Signup.vue'
import WorldCup from '../views/WorldCup.vue'


import Main from '../views/Main.vue'
import Feed from '../views/Feed.vue'
import FeedDetail from '../views/FeedDetail.vue'
import FeedCreate from '../views/FeedCreate.vue'
import MyPage from '../views/MyPage.vue'
import Recommend from '../views/Recommend.vue'
import BeerList from '../views/BeerList.vue'
import BeerDetail from '../views/BeerDetail.vue'
import BeerLike from '../views/BeerLike.vue'
import Setting from '../views/Setting.vue'
import BeerSearchPage from '../views/BeerSearchPage.vue'
import UserSearchPage from '../views/UserSearchPage.vue'
import ProfileSetting from '../views/ProfileSetting.vue'
import PasswordSetting from '../views/PasswordSetting.vue'
import LikeSetting from '../views/LikeSetting.vue'
import Exit from '../views/Exit.vue'


import CameraDetection from '../views/CameraDetection.vue'
import Chatting from '../views/Chatting.vue'
import BeerParty from '../views/BeerParty.vue'
import Snack from '../views/Snack.vue'


import PageNotFound from '../views/PageNotFound.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Login', // login
    component: Login,
    meta: {hideHeader : true, hideSideBar: true},
  },
  {
    path: '/signup/user',
    name: 'SignupUser', // login
    component: SignupUser,
    meta: {hideHeader : true, hideSideBar: true},
  },
  
  {
    path: '/signup',
    name: 'Signup', // signup
    component: Signup,
    meta: {hideHeader : true, hideSideBar: true},
  },
  {
    path: '/signup/worldcup',
    name: 'WorldCup', // login
    params : [],
    component: WorldCup,
    meta: {hideHeader : true, hideSideBar: true},
  },



  {
    path: '/main',
    name: 'Main', // Main 헤더와 사이드 바는 컴포로
    component: Main
  },
  {
    path: '/feed', // /feed
    name: 'Feed', // Main
    component: Feed
  },
  {
    path: '/feed/detail/:feed_id', // /feed
    name: 'FeedDetail', // Main
    component: FeedDetail,
    props : true

  },
  {
    path: '/feedcreate/:contentId?', // /feedcreate
    name: 'FeedCreate', // Main
    component: FeedCreate

  },
  {
    path: '/mypage/:userId', // /profile, /
    name: 'Mypage', // Main
    component: MyPage,
    props : true
  },
  {
    path: '/recommend', // 
    name: 'Recommend', // Main
    component: Recommend
  },
  {
    path: '/beerlist', // 
    name: 'BeerList', // Main
    component: BeerList
  },
  {
    path: '/beer/like', // 
    name: 'BeerLike', // Main
    component: BeerLike
  },
  {
    path: '/beer/:beer_id', // 맥주 상세 보기
    name: 'BeerDetail', // Main
    component: BeerDetail,
    props: true,
  },
  {
    path: '/beer/search/:keyword', // 맥주 검색 결과 페이지
    name: 'BeerSearchPage', // Main
    component: BeerSearchPage,
    props : true
  },
  {
    path: '/user/search/:keyword', // 유저 검색 결과 페이지
    name: 'UserSearchPage', // Main
    component: UserSearchPage,
    props : true
  },


  {
    path: '/camera_detection', // 카메라 인식
    name: 'CameraDetection', // Main
    component: CameraDetection
  },
  {
    path: '/chat', // 채팅 페이지
    name: 'Chatting', // Main
    component: Chatting
  },
  {
    path: '/beer_party', // 맥주팟
    name: 'BeerParty', // Main
    component: BeerParty
  },
  {
    path: '/snack', // 안주
    name: 'Snack', // Main
    component: Snack
  },
  {
    path: '/setting', // 설정
    name: 'Setting', // 설정
    component: Setting
  },
  {
    path: '/setting/profile', // 프로필 설정
    name: 'ProfileSetting', // 설정
    component: ProfileSetting
  },
  {
    path: '/setting/password', // 비밀번호 변경
    name: 'PasswordSetting', // 설정
    component: PasswordSetting
  },
  {
    path: '/setting/like', // 선호도 수정
    name: 'LikeSetting', // 설정
    component: LikeSetting
  },
  {
    path: '/exit', // 회원탈퇴
    name: 'Exit', // 회원탈퇴
    component: Exit
  },



  {
    path: '/pagenotfound',
    name: "404",
    component: PageNotFound,
    meta: {hideHeader : true, hideSideBar: true},
  },
  {
    path: '*',
    redirect: '/pagenotfound'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
