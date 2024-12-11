import { useEffect } from "react"


const usePageTitle = (title) => {
  useEffect(()=>{
    //title 추출
    //반응형 title ==> $로 : DOm요소 저장
    //getElementsByTagName은 html collection을 반환
    // console.log(document.getElementsByTagName("title"))
    const $title = document.getElementsByTagName("title")[0] //TagName == title이라고 가지는 모든 태그 => 지금 head의 감정일기장
    $title.innerText = title
  }, [title])
}

export default usePageTitle