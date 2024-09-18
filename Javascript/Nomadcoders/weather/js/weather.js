//화면에 날씨로 보내줄 것

//api키
const API_KEY = "sth";


function onGeoOK(user) {//user의 데이터를 준다
  console.log(user);
  const lat = user.coords.latitude; //위치 명확하게 잘 쓸 것
  const lng = user.coords.longitude;
  const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lng}&appid=${API_KEY}&units=metric`;
  console.log("You live it", lat, lng);
  console.log(url); //fectch를 통해서 url을 얻을 것
  fetch(url).then((response) => response.json())
  .then((data) => {
    //container에서 span에 날씨를 줄 것
    //const weatherContainer = document.getElementById("weather")
    const weather = document.querySelector("#wether span:first-child");
    const city = document.querySelector("#wether span:last-child");
    city.innerText = data.name;
    weather.innerText = data.weather[0].main;
    console.log(data.name, data.weather[0].main);
  }); //구글 크롬에 network에 가면 wifi에서 어떤일이 일어나는지 확인 가능

}

function onGeError() {
  alert("Can't find you, No weather for you.")
}

//잘되었을 떄, 에러를 발생했을떄로 두번 나눠서 진행해야 함
navigator.geolocation.getCurrentPosition(onGeoOK, onGeError); //브라우저에서 위치 좌표를 줄 것
//따라서 user의 위치를 받을 수 있음