import { useState } from 'react';

function App() {
  // 잘못된 방식의 상태 관리
  const [isLoading, setIsLoading] = useState(false);
  const [isSuccess, setIsSuccess] = useState(false);
  const [isError, setIsError] = useState(false);

  // 올바른 방식의 상태 관리
  const [fetchStatus, setFetchStatus] = useState('idle');

  const handleBadFetch = () => {
    // 잘못된 방식의 상태 변경
    setIsLoading(true);

    setTimeout(() => {
      // 이런 상황에서 실수로 둘 다 true가 될 수 있음
      setIsLoading(false);
      setIsSuccess(true);
      setIsError(true); // 논리적 모순 발생!
    }, 2000);
  };

  const handleGoodFetch = () => {
    // 올바른 방식의 상태 변경
    setFetchStatus('loading');

    setTimeout(() => {
      // 한 번에 하나의 상태만 가능
      setFetchStatus('success');
      // 또는 setFetchStatus('error');
    }, 2000);
  };

  return (
    <div style={{ padding: '20px' }}>
      <h2>교차 State 실습</h2>

      <div style={{ marginBottom: '40px' }}>
        <h3>잘못된 방식</h3>
        <button onClick={handleBadFetch}>데이터 가져오기</button>
        <p>로딩 중: {isLoading.toString()}</p>
        <p>성공: {isSuccess.toString()}</p>
        <p>에러: {isError.toString()}</p>
      </div>

      <div>
        <h3>올바른 방식</h3>
        <button onClick={handleGoodFetch}>데이터 가져오기</button>
        <p>현재 상태: {fetchStatus}</p>
      </div>
    </div>
  );
}

export default App;
