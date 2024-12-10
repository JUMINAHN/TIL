import Schedule from "./components/Schedule";


const App = () => {
  // 시간표 데이터: 5일 (월~금), 각 요일마다 4개의 수업
  const classes = [
    ["수학", "과학", "체육", "미술"],    // 월요일
    ["영어", "역사", "체육", "음악"],    // 화요일
    ["물리", "화학", "수학", "역사"],    // 수요일
    ["미술", "체육", "영어", "수학"],    // 목요일
    ["체육", "과학", "화학", "음악"],    // 금요일
  ];

  return (
    <div>
      <h1>학교 시간표</h1>
      <Schedule classes={classes} />
    </div>
  );
};

export default App;
