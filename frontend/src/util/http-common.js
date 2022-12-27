import axios from "axios"

const API_BASE_URL = "https://j5c205.p.ssafy.io/api/"
// const API_BASE_URL = "http://localhost:8000/api/"


export default axios.create({
  baseURL: API_BASE_URL,
  headers: {
    // "Content-type": 'application/json;charset=utf-8',
    "Content-type": 'multipart/data-form',

    // 'Access-Control-Allow-Origin' : '*',
    // 'Access-Control-Allow-Methods' : 'GET, POST, PATCH, PUT, DELETE, OPTIONS',
    // "Access-Control-Allow-Headers": "Origin, Content-Type",
    // "access-token": localStorage.getItem("access-token")
  }
});


