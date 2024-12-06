import { useParams } from "react-router-dom"


const Edit = () => {
  const params = useParams()
  console.log(params) //params는 id값을 가진다.

  return (
    <div>
      <h1>Edit</h1>
      <p>{params.id}번 Edit입니다.</p>
    </div>
  )
}

export default Edit