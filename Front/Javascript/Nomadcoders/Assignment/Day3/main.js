const colors = [
  '#ef5777',
  '#575fcf',
  '#4bcffa',
  '#34e7e4',
  '#0be881',
  '#f53b57',
  '#3c40c6',
  '#0fbcf9',
  '#00d8d6',
  '#05c46b',
  '#ffc048',
  '#ffdd59',
  '#ff5e57',
  '#d2dae2',
  '#485460',
  '#ffa801',
  '#ffd32a',
  '#ff3f34',
];
const bodyTag = document.querySelector('body');
// let intervalId; // setInterval의 ID를 저장할 변수
bodyTag.style.backgroundImage = `linear-gradient(to right, ${colors[0]}, ${colors[1]})`;

const btn = document.querySelector('button');
const clickBtn = () => {
  const random1 = colors[Math.floor(Math.random() * colors.length)];
  let random2 = colors[Math.floor(Math.random() * colors.length)];

  while (random1 === random2) {
    random2 = colors[Math.floor(Math.random() * colors.length)];
  }
  bodyTag.style.backgroundImage = `linear-gradient(to right, ${random1}, ${random2})`;
};

// 클릭 이벤트에 콜백 함수 전달
btn.addEventListener('click', clickBtn);
