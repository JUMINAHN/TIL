// ClothingComponent.jsx
const ClothingComponent = ({ title, itemCount, salePercentage }) => {
  return (
    <div>
      <h2>{title}</h2>
      <p>총 {itemCount}개의 의류 제품이 있습니다.</p>
      <p>전 품목 {salePercentage}% 할인 중!</p>
    </div>
  )
}

export default ClothingComponent