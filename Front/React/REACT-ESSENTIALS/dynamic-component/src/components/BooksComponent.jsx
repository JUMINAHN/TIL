const BooksComponent = ({ title, itemCount, bestSeller }) => {
  return (
    <div>
      <h2>{title}</h2>
      <p>총 {itemCount}권의 도서가 있습니다.</p>
      <p>이번 주 베스트셀러: {bestSeller}</p>
    </div>
  )
}

export default BooksComponent

