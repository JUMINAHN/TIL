const Score = ({students}) => {
  // console.log(students)

  // 테이블 구조 => row, col
  //배열안의 배열

  return (
    <div>
      <h1>Score</h1>
      <table>
        <thead>
          <tr>
            {students[0].map((title, index) => (
              <th key={index}>{title}</th>
            ))}
          </tr>
        </thead>
        <tbody>
          {students.slice(1).map((row, rowIdx) =>
            <tr key={rowIdx}>
              {row.map((col, colIdx) => 
              <td key={colIdx}>{col}</td>
              )}
            </tr>
          )}
        </tbody>
      </table>
    </div>
  )
}

export default Score