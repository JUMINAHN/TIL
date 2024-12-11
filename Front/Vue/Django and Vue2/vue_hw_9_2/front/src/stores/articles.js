import axios from 'axios'
import { computed, ref } from 'vue'
import { defineStore } from 'pinia'
import { useRouter } from 'vue-router'


export const useArticleStore = defineStore('article', () => {
  //그것을 위해서 token을 통해 계속 인증된 사용자임을 입증하고 주고 받을 수 있도록 token을 담아서 보내줘야 함
  const token = ref(null) //token null값으로 받고

  //하기에는 사용자의 요청에 따라서 서버에 전송하는 것들을 일단 모음
  const articles = ref([])
  const router = useRouter()

  const getArticles = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      headers : { //전체 조회에 사용
        Authorization : `Token ${token.value}`
      }
    })
    .then(res => articles.value = res.data)
  }

  const createArticle = function ({ title, content}) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/articles/', //허가되지 않음
      headers : { //전체 조회에 사용
        Authorization : `Token ${token.value}`
      },
      data: {
        title,
        content
      },
    })
    .then((res) => {
      console.log(res) //데이터 작성 성공
      router.push({name : 'home'}) //홈으로
    })
    .catch((err) =>{
      console.log('error', err) //생성과 관련된 에러 확인
    })
  }

  const signUp = function(payload) {
    //payload를 받아서 이것을 서버로 보내줄 것
    const {username, password1, password2} = payload
    axios({
      method : 'post', //등록
      url : 'http://127.0.0.1:8000/accounts/signup/', //링크 => 계속 에러 발생 : 네트워크 에러 확인 => 네트워크창에서 확인가능
      data : { //파라미터를 받아서 이용할 것 => payload에 있는 아이들 => home에 에러발생 why? => 401: 현재 인증된 사용자가 아니기 떄문
        username,
        password1,
        password2
      }
    })
    .then((res) => {
      //회원 가입 성공!
      console.log('회원 가입 성공') //추후 메인 페이지로 돌려줄 것
      router.push({name : 'home'}) //홈으로
    })
    .catch((err) => {
      console.log('error 발생')
    })
  }

  const logIn = function(payload) {
    //payload를 받아서 이것을 서버로 보내줄 것
    const {username, password} = payload
    axios({
      method : 'post', //등록
      url : 'http://127.0.0.1:8000/accounts/login/', //링크
      data : { 
        username,
        password
      }
    })
    .then((res) => {!
      console.log('로그인 성공') //추후 메인 페이지로 돌려줄 것
      //이때 생길 것
      token.value = res.data.key //여기에 값이 있을 것 
      router.push({name : 'home'}) //홈으로
    })
    .catch((err) => {
      console.log('error 발생')
    })
  }

  //인증 상태 여부에 따라 동작을 구현할 것
  const isLogin = computed(() => { //반복적으로 확인
    if (token.value === null) {
      return false //값이 없음
    } else {
      return true
    }

  })

  return { articles, getArticles, createArticle, signUp, logIn, token, isLogin } 
  
  // 이 기능을 사용하면 스토어의 상태를 브라우저의 저장소(예: localStorage)에 자동으로 저장하고 복원
}, {persist : true})
