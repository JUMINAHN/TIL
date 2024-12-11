const clockTitle = document.querySelector('.js-clock');
const body = document.querySelector('body');

const Christmas = new Date('2024-12-25T00:00:00'); //T 날짜와 시간을 구분해줌 `T` 중요
const newDate = new Date(); //오늘 날짜 기준

// diffDate를 계쏙 계싼해야 함
const updateCountdown = () => {
  const now = new Date(); //오늘 => 이 날짜는 맨날 바뀌니까
  let diffDate = Christmas - now;

  //그리고 날짜가 초과했는지 확인해야 함 => 현재 getTime() 형식으로 UTC원칙에 따라 진행되고 있음
  if (diffDate < 0) {
    // 크리스마스가 지남
    return;
  }
  let countDay = Math.floor(diffDate / (24 * 60 * 60 * 1000));
  let countHour = Math.floor(
    (diffDate % (24 * 60 * 60 * 1000)) / (60 * 60 * 1000)
  );
  let countMinute = Math.floor((diffDate % (60 * 60 * 1000)) / (60 * 1000));
  let countSeconds = Math.floor((diffDate % (60 * 1000)) / 1000);
  let result = `${countDay}d ${countHour}h ${countMinute}m ${countSeconds}s`;
  clockTitle.innerText = result;
};

//updateCount 초기 세팅
updateCountdown();
//1초마다 업데이트 -> count계속 세고 1초마다 셈
setInterval(updateCountdown, 1000);
