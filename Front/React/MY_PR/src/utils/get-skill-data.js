// import django from '/src/assets/skillImg/django.png'
// import react from '/src/assets/skillImg/react.png'
// import vue from '/src/assets/skillImg/vue.webp'
// import vuetify from '/src/assets/skillImg/vuetify.jpg'
// import css from '/src/assets/skillImg/css.png'
// import bootstrap from '/src/assets/skillImg/bootstrap.png'
// import notion from '/src/assets/skillImg/notion.png'
// import jira from '/src/assets/skillImg/jira.jpeg'
// import git from '/src/assets/skillImg/git.png'
// 파일 쉼표로 에러

import bootstrap from '/src/assets/skillImg/bootstrap.svg'
import css from '/src/assets/skillImg/css.svg'
import django from '/src/assets/skillImg/django.svg'
import git from '/src/assets/skillImg/git.svg'
import jira from '/src/assets/skillImg/jira.svg'
import vuetify from '/src/assets/skillImg/vuetify.svg'
import vue from '/src/assets/skillImg/vue.svg'
import react from '/src/assets/skillImg/react.svg'
import notion from '/src/assets/skillImg/notion.svg'


export const skills = [
  // framework
  {title : 'Vue', 
  description : 'SSAFY에서 금융 프로젝트 예적금 맛ZIP을 만든 경험을 바탕으로 v-model, onMounted, computed를 활용할 수 있습니다.', 
  img : vue },  
  {title : 'React', 
  description : '리액트 스터디 활동에서 감정 일기장을 만든 경험을 바탕으로 ContextAPI, useReducer, useState를 활용할 수 있습니다.',
  img : react},
  {title : 'Django', 
  description : 'SSAFY에서 금융 프로젝트 예적금 맛ZIP을 관리하며 DB ORM, Auth, Serializer를 활용할 수 있습니다.', 
  img : django},

  // desgin
  {title : 'Vuetify', description : '데이터베이스, 페이지네이션, 카드 컴포넌트 등의 디자인을 사용할 수 있습니다.', img : vuetify },
  {title : 'Css', description : '간단한 레이아웃, 버튼 등 기본적인 CSS를 구현할 수 있습니다.', img : css },
  {title : 'Bootstrap', description : '레이아웃, 버튼, 입력창, 네비게이션 바 등의 디자인을 사용할 수 있습니다.', img : bootstrap},

  //협업툴
  {title : 'Notion', description : '아이디어 아이데이션 활동을 중심으로 툴을 사용하며 프로젝트를 진행했습니다.', img : notion},
  {title : 'Jira', description : '일정 관리, 아이디어 회의, 기록물 관리 중심으로 툴을 사용해 프로젝트를 관리했습니다.', img : jira},
  {title : 'Git', description : 'add, commit, pull, push, branch를 활용한 프로젝트 코드 관리를 하며 툴을 학습했습니다.', img : git},
]
