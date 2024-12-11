import { useEffect } from "react"



const usePageTitle = (title) => {
  useEffect(()=> { //신기
    const $title = document.getElementsByTagName("title")[0]
    //페이지 타이틀 태그
    //dom요소 저장하는 요소 만들떄 $로 만든다
    $title.innerText = title
  }, [])
}

export default usePageTitle