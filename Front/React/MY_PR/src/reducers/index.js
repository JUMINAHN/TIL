

import { combineReducers } from '@reduxjs/toolkit'

// 여기에 개별 리듀서를 import하세요
// import someReducer from './someReducer'
const initialState = {
  data: "초기 데이터" //초기 state값 => data로 전달해주고
}


function dataReducer(state = initialState, action) {
  return state // 지금은 상태를 변경하지 않습니다
}

const rootReducer = combineReducers({
  data: dataReducer, //data로 reducer 자체를 전달해주고
})

export default rootReducer
