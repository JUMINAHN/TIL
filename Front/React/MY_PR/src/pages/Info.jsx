import InfoItem from "./InfoItem"
import './Info.css'

// info item들 전달하기 => redux 사용해보기..?


const Info = () => {
  return(
    <div className="Info">
      <h1>My profile</h1>
      <InfoItem />
    </div>
  )
}

export default Info