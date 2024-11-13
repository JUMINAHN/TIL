import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'


export const useCounterStore = defineStore('counter', () => {
  //임시데이터 => 게시글 역할을 할 수 있는 데이터 두개
  const articles = ref([ //비어져야함 
  //   {id : 1, title : 'article 1', content : 'content1'},
  //   {id : 2, title : 'article 2', content : 'content2'},
  ])
  //action이 작성되어야 함 => drf에게 전체 요청을 줘!라고 전체 요청을 하는 action
  //axios => 해당 데이터를 채워주고 화면을 그려야 함
  //drf의 기본주소는
  const API_URL = 'http://127.0.0.1:8000' //장고 주소 자체 => 장고는 뒤 주소만 알면 됨
  //component에서 사용할 수도 있음 API_URL을 쓰기 위해서 보내준다.

  //drf로 전체 게시글 요청을 보내고 응답을 받아 articles에 저장하는 함수 => 배열을 채워줌
  const getArticles = function() {
    //비동기 => 기다리지 않는다. (동기적 생각X) => 즉 미리 처리해야한다.

    axios({ //전체 게시글 조회 => 다른 컴포넌트로 접근해서 getarticles호출
      method : 'get',
      url : `${API_URL}/api/v1/articles/`, //전체 게시글 조회 ==> postman 으로 보낸 것 요청 다시 
    }) //promise 구조 특징 => 요청 결과가 성공 / 실패 
    //각각 콜백함수 인자 == 비동기 처리를 위함
    .then((res) => {
      console.log(res)
      //res의 배열을 => articles에 저장해주면 된다.
      articles.value = res.data //장고가 준 데이터로 저장 => 전체 게시글 조회
    }) 
    .catch((err) => {
      console.log(err)
    })

  }


  return { articles, getArticles, API_URL }
}, { persist: true })
