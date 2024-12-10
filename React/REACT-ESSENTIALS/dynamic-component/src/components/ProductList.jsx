import { useState } from "react";
import Clothing from "./Clothing.jsx";
import Electronic from "./Electronic.jsx";


const ProductList = () => {
  const [category, setCategory] = useState("All");

  const renderComponent = () => {
    switch (category) {
      case "Electronics":
        return <Electronic />;
      case "Clothing":
        return <Clothing />;
      default:
        return (
          <ul>
            <li>TV</li>
            <li>Shirt</li>
            <li>Washing Machine</li>
            <li>Pants</li>
          </ul>
        );
    }
  };

  return (
    <div>
      <h1>ProductList</h1>
      <select onChange={(e) => setCategory(e.target.value)}>
        <option value="All">All</option>
        <option value="Electronics">Electronics</option>
        <option value="Clothing">Clothing</option>
      </select>
      {renderComponent()}
    </div>
  );
};

export default ProductList;
