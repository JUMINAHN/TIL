import { useState } from 'react'
import Header from './components/Header'
import Editor from './components/Editor';
import List from './components/List';
import './App.css'

//일단 UI/UX 먼저

function App() {
  return (
    <div className='App'>
      <Header />      
      <Editor />      
      <List />      
    </div>
  )
}

export default App
