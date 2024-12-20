// store 자체를 만든다.
import { configureStore } from '@reduxjs/toolkit'
import rootReducer from './reducers'

const store = configureStore({ 
  reducer: rootReducer
});

export default store //store 자체를 반환
