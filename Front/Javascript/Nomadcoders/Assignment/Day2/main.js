const form = document.querySelector('form');
form.addEventListener('submit', (e) => e.preventDefault()); //prevent Default

//stateCount = 0 : 카운트 상태
let stateCount;
// count_number input 요소 선택
const countNumber = document.querySelector('#count_number');
countNumber.addEventListener('input', (e) => {
  // console.log(e.target.value, '현재 count');
  stateCount = e.target.value;
  console.log(stateCount, 'count'); //동적요소 전달되는가? :
});
let correctNumber;
function getRandom(min, max) {
  return Math.ceil(Math.random() * (max - min + 1) + min);
}

// let tryCount = 0; //시도 횟수
let playerNumber;
//만약 사용자가 틀릴 경우, 맞출 경우
const playGame = document.querySelector('#play_game');
playGame.addEventListener('input', (e) => {
  playerNumber = e.target.value;
  console.log(playerNumber, 'player');
});

const playBtn = () => {
  if (stateCount > 0) {
    correctNumber = getRandom(0, stateCount); //정답 넘버
    console.log(correctNumber);
  }
  const resultSection = document.querySelector('#result');
  resultSection.innerHTML = '';
  const pTag = document.createElement('p');
  const p2Tag = document.createElement('p');
  pTag.innerHTML = `you chose :${playerNumber}, the machine chose :${correctNumber}`;
  if (parseInt(playerNumber) === correctNumber) {
    p2Tag.innerHTML = 'You won!';
  } else {
    // tryCount ++
    p2Tag.innerHTML = 'You lost!';
  }
  resultSection.appendChild(pTag);
  resultSection.appendChild(p2Tag);
  // 계속 추가되면 안됨.. => while문
};

//여기서 submit 이벤트가 실행될경우 innerHtml로 나타나는 것
const btn = document.querySelector('.btn');
btn.addEventListener('click', playBtn);
