import { useState } from 'react';

function App() {
  const [nowState, setNowState] = useState("not Connect");

  const onClickBtn = () => {
    setNowState("로딩 중...");
    //여기서 
    setTimeout(() => {
      //여기서 바로 try
      try {
        console.log('접속 진행중');

        // 여기서 에러가 발생할 수 있는 작업을 수행합니다.
        // 예를 들어, API 호출 시 에러가 발생할 수 있습니다.
        // 아래 코드는 오류를 시뮬레이션 하기 위해 임의로 throw를 사용한 것입니다.
        // 실제 API 호출 코드로 대체할 수 있습니다.
        const simulatedError = true; // true로 설정하면 에러 시뮬레이션

        if (simulatedError) {
          throw new Error("서버 오류 발생!") //여기서 오류 발생하면 던질 것
          //서버에서 에러가 발생한다고 가정하기 떄문에 Error를 여기서 만들어서 던지는 것
        }

        setNowState('접속 완료') // 접속 완료
      } catch (error) {
        console.error(error) // 에러 로그 출력
        setNowState('접속 실패, 에러 발생') // 에러 상태로 변경
      }
    }, 3000); // 3초 뒤
  }

  return (
    <div>
      <h1>교차 State 실습</h1>
      <button onClick={onClickBtn}>활성화 버튼</button>
      <h5>현재 상태 : {nowState}</h5>
    </div>
  );
}

export default App;