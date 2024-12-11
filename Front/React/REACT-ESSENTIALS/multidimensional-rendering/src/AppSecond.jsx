import Score from "./components/Score"

const App = () => {
  const students = [
    ["이름", "수학", "영어", "과학"],
    ["홍길동", 85, 90, 80],
    ["김영희", 78, 88, 95],
    ["박철수", 92, 85, 89]
  ]

  return (
    <div>
      <Score 
      students={students}/>
    </div>
  )
}

export default App
