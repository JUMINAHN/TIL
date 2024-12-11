//매개변수로 받아올 값

//count 자체를 받아옴
const Viewer = ({count}) => {
  //알맞게 출력되는 것 확인
  return (
    <>
      <div>현재 카운트</div>
      <h1>{count}</h1>
    </>
  )
}

export default Viewer