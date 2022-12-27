import Vue from 'vue'
import Vuex from 'vuex'

// import axios from 'axios'
import createPersistedState from "vuex-persistedstate";

import http from '@/util/http-common.js'
// axios.defaults.baseURL = 'http://j5c205.p.ssafy.io/'
Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [ createPersistedState() ],
  state: {
    userId : "",
    nickName : "",
    feedId : "",
    worldcup : "",
  },
  getters : {
    getUserId (state){
      return state.userId
    },
    getNickName(state){
      return state.nickName
    },
    getFeedId(state){
      return state.feedId
    },
    getWorldCup(state){
      return state.worldcup
    }

  },
  mutations: {
    GETUSERINFO(state, data){
      state.userId = data["userID"]
      state.nickName = data["nickname"]
    },
    GETFEEDID(state, data){
      state.feedId = data
    },
    GETWORLDCUP(state, form){
      state.worldcup = form
    }
  },
  actions: {
    async LOG_IN({commit}, data){
      const userID = data.get("userID")
      await http.post("login/", data)
      .then(()=>{
        http.get(`user/${userID}/detail/`)
        .then((res)=>{
          commit("GETUSERINFO", res.data)
        })
      })
    },
    async SIGN_UP({commit}, data){
      const userID = data.get("userID")
      await http.post("register/", data)
      .then(()=>{
        http.get(`user/${userID}/detail/`)
        .then((res)=>{
          commit("GETUSERINFO", res.data)
        })
      })
    },
    async SET_FEED_ID({commit}, data){
      await http.get(`feed/${data}/`)
      .then((res)=>{
         commit("GETFEEDID", res.data.id)
      })
    }
  },
  modules: {
  }
})
