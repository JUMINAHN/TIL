import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'


//게시글 조회
export const useArticleStore = defineStore('article', () => {
  const articles = ref([]) //이 곳에 넣으라고 되어있다. => 즉 res.data를 받아온 데이터를 저장한다. => 그걸 보여준다.

  const getArticles = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/articles/'
    })
    .then((res) => {
      console.log(res)
      //여기서 데이터를 확인해보자 일단
      console.log(res.data) //여기서 데이터를 저장해야할 것 같다. 저기에서는 아무리해도 undefined => 실제 받아오는 곳
      articles.value = res.data
  })
  }



  return { articles, getArticles }
})
