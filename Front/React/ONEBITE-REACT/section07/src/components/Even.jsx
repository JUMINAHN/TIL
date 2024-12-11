import { useEffect } from "react"

const Even = () => {
  useEffect(()=>{
    //콜백함수가 반환해주는 것 클린업, 정리 함수 == 끝날때 실행, []
    return () => {
      console.log('unmount')
    } 
  }, [])
  return <div>짝수입니다.</div>
}

export default Even