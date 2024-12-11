import Price from "./components/Price";


const App = () => {
  const products = [
    ["상품명", "가격", "재고"],
    ["티셔츠", 20000, 50],
    ["청바지", 40000, 30],
    ["운동화", 60000, 20],
  ];
  

  return (
    <div>
      <Price 
      products={products}/>
    </div>
  )
}

export default App
