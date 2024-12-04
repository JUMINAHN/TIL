import { useParams } from "react-router-dom"

const Edit = () => {
  const params = useParams()
  return (
    <div>
      <h1>Edit</h1>
      <h5>{params.id}번 일기 입니다.</h5>
    </div>
  )
}

export default Edit