const Price = ({products}) => {
  //상품명, 가격, 재고
  //그리고 티셔츠, 청바지, 운동화 첫번쨰 0이 모두 중요한 내용

  return (
    <div>
      <h1>Hello</h1>
      <table>
        <thead>
          <tr>
          {products[0].map((category, cateIdx) =>
            <th key={cateIdx}>{category}</th>
          )}
          </tr>
        </thead>
          {/* 첫번쨰 idx가 굵은 색 */}
        <tbody>
          {products.slice(1).map((row, rowIdx) => 
          <tr key={rowIdx}>
            <th>{row[0]}</th>
            {row.slice(1).map((col, colIdx) => 
            <td key={colIdx}>
              {col}
            </td>
            )}
          </tr>
          )}
        </tbody>
      </table>
    </div>
  )
}

export default Price