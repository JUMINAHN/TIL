const ElectronicsComponent = ({ title, itemCount, featuredBrand }) => {
  return (
    <div>
      <h2>{title}</h2>
      <p>총 {itemCount}개의 전자제품이 있습니다.</p>
      <p>이번 주 특가 브랜드: {featuredBrand}</p>
    </div>
  )
}

export default ElectronicsComponent