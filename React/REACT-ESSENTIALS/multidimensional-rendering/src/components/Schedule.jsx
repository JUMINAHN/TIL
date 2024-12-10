// src/components/Schedule.jsx

const Schedule = ({ classes }) => {
  return (
    <table>
      <thead>
        <tr>
          <th>시간</th>
          <th>월요일</th>
          <th>화요일</th>
          <th>수요일</th>
          <th>목요일</th>
          <th>금요일</th>
        </tr>
      </thead>
      <tbody>
        {/* 각 시간대에 대한 수업을 반복해서 렌더링 */}
        {classes.map((day, timeIndex) => (
          <tr key={timeIndex}>
            <td>{`${timeIndex + 1}교시`}</td>
            {day.map((lesson, dayIndex) => (
              <td key={dayIndex}>{lesson}</td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  )
}

export default Schedule
