//명언들을 배열로 만든다. -> 일반 텍스트와 다름
const quotes = [
  {
  quote: 'I never dreamed about success, I worked for it',
  author: 'Estee Lauder'
  },
  {
  quote: 'Do not try to be original, just try to be good.',
  author: 'Paul Rand'
  },
  {
  quote: 'Do not be afraid to give up the good to go for the great',
  author: 'John D. Rockefeller'
  },
  {
  quote: 'If you cannot fly then run. If you cannot run, then walk. And if you cannot walk, then crawl, but whatever you do, you have to keep moving forward.',
  author: 'Martin Luther King Jr.'
  },
  {
  quote: 'Our greatest weakness lies in giving up. The most certain way to succeed is always to try just one more time.',
  author: 'Thomas Edison'
  },
  {
  quote: 'The fastest way to change yourself is to hang out with people who are already the way you want to be',
  author: 'REid Hoffman'
  },
  {
  quote: 'Money is like gasoline during a road trip. You do not want to run out of gas on your trip, but you are not doing a tour of gas stations',
  author: 'Tim O Reilly'
  },
  {
  quote: 'Some people dream of success, while other people get up every morning and make it happen',
  author: 'Wayne Huizenga'
  },
  {
  quote: 'The only thing worse than starting something and falling.. is not starting something',
  author: 'SEth Godin'
  },
  {
  quote: 'If you really want to do something, you will find a way. If you do not, you will find an excuse.',
  author: 'Jim Rohn'
  },
  ];

const quote = document.querySelector("#quote span:first-child"); //1번째
const author = document.querySelector("#quote span:last-child"); //2번째

//따라서 해당 명언들에 random한 접근을 위해서는 function을 사용해야 함
//즉 현재 0부터 현재 개수 -1만큼에 랜덤하게 접근해야 함
//Math.module사용
//Math.random()*10 //0부터 10사이의 숫자를 무작위로 얻을 수 있음
//단 소수점은 필요가 없음
//round는 반올림, ceil은 올림, floor은 버림
const todayQuote = quotes[Math.floor(Math.random()*quotes.length)] //명언의 길이만큼

//이제 해당 내용을 화면에 보이게 한다
quote.innerText = todayQuote.quote;
author.innerText = todayQuote.author;




//무작위성 randomness
//만약 첫번째 명언에 접근하려면?
//console.log(quotes[quotes.length-1]); //python과 다르게 -1 변수는 접근하기 어려움