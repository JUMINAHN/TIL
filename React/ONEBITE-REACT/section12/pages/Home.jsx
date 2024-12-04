import { useSearchParams } from "react-router-dom"
//queryString을 왜 home에서 진행하는 것? == searchString
//뭐 예를 네이버로 생각했을떄 메인 검색화면에 뜨게 될텐데 그런걸 생각해봤을떄 임시로 test?


const Home = () => {
  //searchParams는 [sth, set] 구조로
  const [params, setParams] = useSearchParams()
  console.log(params.get('value'))
  //?value=hello로 알맞게 전달받을 수 있음 => value로된 것을 가져온다는의미?
  return (
    <h1>Home</h1>
  )
}

export default Home