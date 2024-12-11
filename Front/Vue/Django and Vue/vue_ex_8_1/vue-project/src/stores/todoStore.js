import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'


export const useTodoStore = defineStore('todo', () => {
  const todoData = ref([

  ]) //이걸 보여줄것이기 때문에
  //api link활용을 위해 여기 넣자
  // console.log('todoData', todoData.value)
  const API_URL = 'http://127.0.0.1:8000/api/v1'

  //BASE_URL을 정의한다.
  //API서버 요청시 사용될 base_url => django에 있는거 이야기인가?
  const getTodos = function() {
    axios({ //axios에서 데이터를 가져와서 보여줄 것
      method : 'get',
      url: `${API_URL}/todos/`, //todos 정보
    })
    .then((res) => {
      console.log(res) //res !!!!
      //errordata를 밖에 낼것이니까
      console.log(res.data) //data맞게 받아오는 것 확인됨

      todoData.value = res.data //확인해봐야 함
      console.log('todoData check', todoData.value) //value자체로 들어옴
    })
    .catch((err) => {
      console.log(err)
    })
  }
  return { getTodos, todoData }
}, { persist: true })
