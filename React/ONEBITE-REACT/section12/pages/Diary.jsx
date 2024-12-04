import { useParams } from "react-router-dom"

const Diary = () => {
  //params 저장
  const params = useParams() //params 값
  console.log(params)

  return (
    <div>
      <h1>Diary</h1>
      <h2>{params.id}번째 diary입니다.</h2>
    </div>
  ) 
}

export default Diary    