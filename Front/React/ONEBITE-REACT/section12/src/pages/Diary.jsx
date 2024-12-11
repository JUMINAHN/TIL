import { useParams } from "react-router-dom"


const Diary = () => {
  const params = useParams()
  return (
    <div>
      <h1>Diary</h1>
      <h3>{params.id}번 일기</h3>
    </div>
  )
}

export default Diary