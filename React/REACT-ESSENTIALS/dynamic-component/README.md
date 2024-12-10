# [추가] 동적 컴포넌트 실습해보기

날짜: 2024년 12월 10일

# 동적 컴포넌트

---

- `React에서 다양한 컴포넌트를 조건에 따라 렌더링`할 수 있는 유용한 패턴입니다.
- 이 패턴을 사용하면 코드의 재사용성을 높이고, 컴포넌트 구조를 유연하게 유지할 수 있습니다.

## 동적 컴포넌트의 장단점

| 장점 | 설명 |
| --- | --- |
| 1. 코드 재사용성 향상 | 동일한 패턴으로 `다양한 컴포넌트를 재사용`할 수 있어 코드 중복을 줄입니다. |
| 2. 조건부 렌더링 로직 간소화 | 특정 조건에 따라 다른 컴포넌트를 쉽게 렌더링할 수 있어 로직이 단순해집니다. |
| 3. 컴포넌트 구조의 유연성 증가 | 새로운 카테고리나 타입의 컴포넌트를 쉽게 추가할 수 있어 시스템의 유연성을 
높입니다. |

| 단점 | 설명 |
| --- | --- |
| 1. 복잡한 로직의 경우 가독성이 떨어질 수 있음 | 너무 많은 조건부 렌더링이 포함되면 코드의 가독성이 낮아질 수 있습니다. |
| 2. 타입 안정성 확보가 어려울 수 있음 | TypeScript를 사용하지 않는 경우 props의 타입을 자동으로 확인하기 어려워 실수가 발생할 수 있습니다. |
| 3. 디버깅이 더 어려울 수 있음 | `동적으로 렌더링되는 컴포넌트의 경우 어떤 컴포넌트가 렌더링되는지 파악하기 어려워 디버깅`이 힘들 수 있습니다. |

## 동적 컴포넌트의 일반적인 사용 사례

| 사용 사례 | 설명 |
| --- | --- |
| 1. 대시보드나 관리자 패널에서 다양한 위젯 렌더링 | 사용자 요구에 따라 다르게 구성된 위젯을 동적으로 표시할 수 있습니다. |
| 2. 폼 빌더나 설문 조사 도구에서 다양한 입력 필드 렌더링 | `사용자의 선택에 따라 다양한 입력 필드를 동적으로 추가`할 수 있습니다. |
| 3. 콘텐츠 관리 시스템에서 다양한 유형의 콘텐츠 표시 | `특정 콘텐츠 유형`에 따라 적절한 컴포넌트를 렌더링하여 관리 효율성을 높입니다. |
| 4. 데이터 시각화 도구에서 다양한 차트 유형 렌더링 | 데이터의 종류에 따라 적합한 차트 유형을 동적으로 선택하여 표시합니다. |
| 5. 다국어 지원 애플리케이션에서 언어별 컴포넌트 렌더링 | 사용자가 `선택한 언어에 맞춰` 해당 언어로 된 컴포넌트를 렌더링하여 유연성을 
제공합니다. |

## 동적 컴포넌트와 URL 라우팅(SPA 방식) 비교

| 항목 | 동적 컴포넌트 | URL 라우팅 |
| --- | --- | --- |
| **개념** | 사용자 상태나 입력에 따라 다른 컴포넌트를 렌더링 | URL 변경 시 해당 URL에 맞는 컴포넌트를 렌더링 |
| **주요 목적** | 실시간 데이터 반영 및 빠른 UI 업데이트 | 페이지 간 탐색 및 고유 주소 제공 |
| **예시** | **대시보드에서 특정 위젯 표시, 폼 필드 동적 추가** | 각각의 카테고리별 URL로 페이지 이동, 세부 페이지 표시 |
| **성능** | 전체 페이지를 새로 고치지 않고 부분적으로 업데이트 | 페이지 전환 시 전체 페이지를 새로 로드하는 부담 가능 |
| **SEO** | SEO에 제약이 있을 수 있음 (JS 실행 후 콘텐츠 표시) | SEO에 유리함 (각 URL이 고유한 경로를 가짐) |
| **북마크/공유** | 특정 상태를 북마크할 수 없음 (URL이 고정적이지 않음) | **사용자가 URL을 북마크하거나 공유 가능** |
| **사용자 경험** | 즉각적인 반응을 통해 부드러운 UX 제공 | 내비게이션이 직관적이며 기존 웹사이트와 유사 |
| **상태 관리** | 상태 관리가 복잡할 수 있음 (조건부 렌더링 시) | 각 페이지에서 **독립적인 상태 관리 가능** |
| **재사용성** | **동일한 컴포넌트**를 다양한 상태로 재사용 가능 | 페이지가 서로 다르므로 재사용성이 낮을 수 있음 |

## 동적 컴포넌트와 URL 라우팅 사용 사례 비교

| 사용 사례 | 동적 컴포넌트 필요성 | URL 라우팅 필요성 |
| --- | --- | --- |
| **대시보드 애플리케이션** | - 사용자가 여러 개의 위젯을 가진 대시보드를 보고 있음.
- 데이터 필터를 클릭할 때 UI가 즉각적으로 변화해야 함. | - 페이지 간 명확한 구분 필요.
- 각 카테고리 또는 상품 세부 정보 페이지에 고유한 콘텐츠가 있어야 함. |
| **전자상거래 웹사이트** | - 사용자가 특정 데이터를 선택할 때, 즉시 변화하는 UI 필요.
- 예를 들어, 상품 필터링이나 정렬 시. | - 각 카테고리 페이지가 고유한 URL을 가져야 함.
- 사용자가 해당 URL을 북마크하거나 공유할 수 있어야 함. |
| **실시간 데이터 시각화** | - 실시간으로 데이터를 반영하고 즉시 변화하는 시각적 요소 필요.
- 예: 주식 차트, 날씨 업데이트 등. | - 특정 대시보드나 데이터 시각화 페이지를 별도로 표시하고 SEO 최적화 필요. |
| **복잡한 폼 빌더** | - 사용자의 선택에 따라 입력 필드가 동적으로 추가되거나 제거되어야 할 때.
- 예: 결제 정보 입력폼. | - 각 단계가 명확히 구분된 프로세스가 필요할 때.
- 예: 다단계 폼에서 각 단계를 별도의 URL로 관리. |
| **다국어 웹사이트** | - 사용자 선택에 따라 UI 언어를 즉시 변경해야 함.
- 각 언어별 컴포넌트를 동적으로 렌더링 가능. | - 각 언어에 대한 고유한 URL을 통해 SEO 최적화 필요
.- 사용자 북마크 및 공유 기능이 용이함. |

## 결론

- **동적 컴포넌트**는 UI의 변화를 즉각적으로 반영하고 사용자의 상호작용에 맞게 유연하게 구성할 수 있는 장점이 있습니다. **주로 대시보드, 복잡한 폼, 또는 실시간 데이터 표시가 필요한 상황에서 유리**합니다.
- **URL 라우팅**은 페이지 간의 명확한 구분과 SEO, 공유 및 북마크의 용이함을 제공합니다. **사이트 내비게이션이 명확할 필요가 있을 때 유리합니다.**

이 표를 통해 두 개념의 차이를 좀 더 명확하게 이해할 수 있기를 바랍니다. 추가적으로 궁금한 점이 있으시면 언제든지 말씀해 주세요!

# 예시: 온라인 쇼핑몰의 상품 필터 페이지

---

### 1. 상태 관리만 사용하는 경우

이 접근 방식에서는 상태를 사용하여 하나의 컴포넌트에서 **모든 필터를 처리**합니다. 아래는 간단한 React 코드입니다.

```jsx
import React, { useState } from 'react';

const ProductList = () => {
  const [category, setCategory] = useState('All');

  const products = [
    { id: 1, name: 'TV', category: 'Electronics' },
    { id: 2, name: 'Shirt', category: 'Clothing' },
    { id: 3, name: 'Washing Machine', category: 'Electronics' },
    { id: 4, name: 'Pants', category: 'Clothing' },
  ];

  const filteredProducts = category === 'All'
    ? products
    : products.filter(product => product.category === category);

  return (
    <div>
      <h1>Products</h1>
      <select onChange={(e) => setCategory(e.target.value)}>
        <option value="All">All</option>
        <option value="Electronics">Electronics</option>
        <option value="Clothing">Clothing</option>
      </select>
      <ul>
        {filteredProducts.map(product => (
          <li key={product.id}>{product.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default ProductList;

```

### 설명:

- **상태 관리**: 사용자의 선택에 따라 `category` 상태를 업데이트하고, 그에 따라 `filteredProducts` 배열을 반환합니다.
- **한 가지 컴포넌트**에서 모든 로직이 처리되므로 코드가 간단해 보이지만, 필터가 추가될수록 복잡해질 수 있습니다.

---

### 2. 동적 컴포넌트를 사용하는 경우

이 방법에서는 각 카테고리를 위해 별도의 컴포넌트를 만들고, 사용자 선택에 따라 해당 컴포넌트를 렌더링합니다.

```jsx
import React, { useState } from 'react';

const ElectronicsComponent = () => (
  <ul>
    <li>TV</li>
    <li>Washing Machine</li>
  </ul>
);

const ClothingComponent = () => (
  <ul>
    <li>Shirt</li>
    <li>Pants</li>
  </ul>
);

const ProductList = () => {
  const [category, setCategory] = useState('All');

  const renderComponent = () => {
    switch (category) {
      case 'Electronics':
        return <ElectronicsComponent />;
      case 'Clothing':
        return <ClothingComponent />;
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
      <h1>Products</h1>
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

```

### 설명:

- **동적 컴포넌트**: `renderComponent` 함수는 선택된 카테고리에 따라 해당 컴포넌트를 렌더링합니다.
- **모듈화**: 각 카테고리별로 컴포넌트를 나누어 관리하므로, 각 컴포넌트는 자신이 관련된 데이터만 처리합니다. 코드가 더 명확해지고, 새로운 카테고리를 추가할 때도 더 용이합니다.

## 요약

- **상태 관리만 사용하는 경우**: 단순하지만 복잡해지면 가독성이 떨어질 수 있습니다. 모든 로직이 한 곳에 모여 있어 유지보수가 어려울 수 있습니다.
- **동적 컴포넌트를 사용하는 경우**: 각 컴포넌트가 독립적으로 동작하므로 가독성이 높고 유지보수가 용이합니다. 새로운 기능이나 카테고리를 추가할 때 더 수월합니다.

이러한 예시를 통해 각각의 접근 방식이 어떻게 작동하는지, 그리고 어떤 상황에서 더 적합한지를 이해할 수 있기를 바랍니다. 추가적인 질문이나 더 구체적인 설명이 필요하다면 언제든지 말씀해 주세요!

# 실사용 예시 : 학습 해보기

---

1. 각 컴포넌트는 `title` prop을 받아 표시합니다.
2. App 컴포넌트에서 버튼을 클릭하면 다른 컴포넌트로 전환됩니다.
- **App.jsx**
    
    ```jsx
    import { useState } from 'react'
    
    import './App.css'
    import NavbarComponent from './components/NavbarComponent'
    import FooterComponent from './components/FooterComponent'
    import ContentComponent from './components/ContentComponent'
    
    //1. 컴포넌트 매핑 객체 만들기
    const componentMapping = { //component 자체를 Mapping할것이기 떄문에 function이 아닌 객체로
      //Q. 궁금한게 Navbar로만 했는데 ''이거 안붙여도 상관없는지?
      Navbar : NavbarComponent,
      Footer : FooterComponent,
      Content : ContentComponent
    }
    
    //2. 동적으로 컴포넌트 렌더링하기
    //DynamicComponent : 실제 맞는 것을 보여줄 내용
    function DynamicComponent({componentName, ...props}) {// 컴포넌트 이름과, props
      const Component = componentMapping[componentName] //사용자에게 input값으로 받을 내용을 mapping => 키로
      // 컴포넌트 자체를 return 할것이니까 `<>`
      return <Component componentName={componentName} {...props}/> //찾은 컴포넌트 렌더링 == Q. 궁금한게 props가 어떻게 와지는 건지? 뭘 이야기하는 건지? props?
      //그니까 뭐 예를 들면 navbarcomponent에 사용되는 props들을 이야기하는것인지?
      //Q. 그리고 props가 공통적으로 들어가야 되는 부분인지? 모든 일관성을 위해 ...props는 통일 시켜줘야하는 것 아닌지?
      //Q. 굳이 props를 통일할 필요 없이 원하는 매핑을 위해 각 요소에 맞는 props나 속성을 넣으면 되는 것인지?
    }
    
    function App() {
      const [currentComponent, setCurrentComponent] = useState('Navbar') //기본은 navVar로 설정
      //Navbar라고 말하면 네비게이션, Footer라고 말하면 Footer가 나오도록
    
      return (
        <div>
          {/* 공통적으로 사용할 컴포넌트 자체를 작성 */}
          <DynamicComponent  //DynamicComponent를 작성한 위치를 볼 것
          componentName={currentComponent}
          // 지금은 title이라는 component 속성이 각각 존재하고 == 여기는 ...props 기타로 처리해준 것,
          // componentName이라는 속성이 존재함  
          title={`${currentComponent} 제목`}/>
          <button onClick={() => setCurrentComponent('Navbar')}>네비게이션 바</button>
          <button onClick={() => setCurrentComponent('Content')}>콘텐츠</button>
          <button onClick={() => setCurrentComponent('Footer')}>푸터</button>
        </div>
      )
    }
    
    export default App
    
    ```
    
- **Content.jsx**
    
    ```jsx
    import { useState } from 'react'
    
    import './App.css'
    import NavbarComponent from './components/NavbarComponent'
    import FooterComponent from './components/FooterComponent'
    import ContentComponent from './components/ContentComponent'
    
    //1. 컴포넌트 매핑 객체 만들기
    const componentMapping = { //component 자체를 Mapping할것이기 떄문에 function이 아닌 객체로
      //Q. 궁금한게 Navbar로만 했는데 ''이거 안붙여도 상관없는지?
      Navbar : NavbarComponent,
      Footer : FooterComponent,
      Content : ContentComponent
    }
    
    //2. 동적으로 컴포넌트 렌더링하기
    //DynamicComponent : 실제 맞는 것을 보여줄 내용
    function DynamicComponent({componentName, ...props}) {// 컴포넌트 이름과, props
      const Component = componentMapping[componentName] //사용자에게 input값으로 받을 내용을 mapping => 키로
      // 컴포넌트 자체를 return 할것이니까 `<>`
      return <Component {...props}/> //찾은 컴포넌트 렌더링 == Q. 궁금한게 props가 어떻게 와지는 건지? 뭘 이야기하는 건지? props?
      //그니까 뭐 예를 들면 navbarcomponent에 사용되는 props들을 이야기하는것인지?
      //Q. 그리고 props가 공통적으로 들어가야 되는 부분인지? 모든 일관성을 위해 ...props는 통일 시켜줘야하는 것 아닌지?
      //Q. 굳이 props를 통일할 필요 없이 원하는 매핑을 위해 각 요소에 맞는 props나 속성을 넣으면 되는 것인지?
    }
    
    function App() {
      const [currentComponent, setCurrentComponent] = useState('Navbar') //기본은 navVar로 설정
      //Navbar라고 말하면 네비게이션, Footer라고 말하면 Footer가 나오도록
    
      return (
        <div>
          {/* 공통적으로 사용할 컴포넌트 자체를 작성 */}
          <DynamicComponent 
          componentName={currentComponent}
          title={`${currentComponent} 제목`}/>
          <button onClick={() => setCurrentComponent('Navbar')}>네비게이션 바</button>
          <button onClick={() => setCurrentComponent('Content')}>콘텐츠</button>
          <button onClick={() => setCurrentComponent('Footer')}>푸터</button>
        </div>
      )
    }
    
    export default App
    
    ```
    
- **Nav.jsx**
    
    ```jsx
    const NavbarComponent = ({ componentName, title }) => {
      return (
        <nav>
          <h1>{title}</h1>
          <p>{componentName} 컴포넌트입니다.</p>
          <ul>
            <li>홈</li>
            <li>소개</li>
            <li>서비스</li>
            <li>연락처</li>
          </ul>
        </nav>
      )
    }
    
    export default NavbarComponent
    ```
    
- **Footer.jsx**
    
    ```jsx
    // FooterComponent.jsx
    const FooterComponent = ({ componentName, title }) => {
      return (
        <footer>
          <h3>{title}</h3>
          <p>{componentName} 영역입니다. © 2024 내 웹사이트. 모든 권리 보유.</p>
        </footer>
      )
    }
    
    export default FooterComponent
    
    ```
    

이렇게 하면 동적으로 컴포넌트를 전환하는 기본 구조를 만들 수 있습니다. 필요에 따라 각 컴포넌트의 내용과 스타일을 수정하면 됩니다.

## 궁금한점

---

1. 컴포넌트 매핑 객체에 대한 질문:
    
    ```jsx
    const componentMapping = {
      Navbar: NavbarComponent,
      Footer: FooterComponent,
      Content: ContentComponent
    }
    
    ```
    
    A: 'Navbar'와 같이 따옴표를 붙이지 않아도 됩니다. **JavaScript 객체의 키로 사용될 때 자동으로 문자열**로 변환됩니다.
    
2. DynamicComponent 함수에 대한 질문들:
    
    ```jsx
    function DynamicComponent({componentName, ...props}) {
      const Component = componentMapping[componentName]
      return <Component componentName={componentName} {...props}/>
    }
    
    ```
    
    - props는 **부모 컴포넌트(여기서는 App)에서 전달되는 모든 속성들**입니다.
    - ...props는 나머지 모든 props를 전달하는 방식으로, 각 컴포넌트에 필요한 고유한 props를 전달할 수 있게 해줍니다.
    - props를 완전히 `통일할 필요는 없습니다.` **각 컴포넌트에 필요한 props만 전달하면 됩니다.**
    - `componentName은 모든 컴포넌트에 공통으로 전달되고, 나머지 props는 각 컴포넌트의 필요에 따라 사용`될 수 있습니다.

1. App 컴포넌트 내 DynamicComponent 사용에 대한 설명:
    
    ```jsx
    <DynamicComponent
      componentName={currentComponent}
      title={`${currentComponent} 제목`}
    />
    
    ```
    
    - DynamicComponent는 App 컴포넌트 내에서 사용되고 있습니다.
    - componentName과 title이라는 두 가지 props가 전달되고 있습니다.
    - title prop은 ...props를 통해 각 컴포넌트로 전달됩니다.
    - componentName은 DynamicComponent 내에서 명시적으로 전달되고 있습니다.

이렇게 구성함으로써, 동적으로 컴포넌트를 렌더링하면서 각 컴포넌트에 필요한 props를 유연하게 전달할 수 있습니다.

# 관련 실습

---

<aside>
💡

실습 문제: 동적 컴포넌트를 사용한 제품 카테고리 페이지 만들기

목표:

1. 전자제품, 의류, 도서 카테고리에 대한 컴포넌트를 만듭니다.
2. 동적 컴포넌트를 사용하여 사용자가 선택한 카테고리에 따라 다른 컴포넌트를 렌더링합니다.
3. 각 카테고리 컴포넌트는 공통 props와 카테고리별 특정 props를 받습니다.
</aside>

단계별 가이드:

1. 세 개의 카테고리 컴포넌트를 만듭니다:

```jsx
// ElectronicsComponent.jsx
const ElectronicsComponent = ({ title, itemCount, featuredBrand }) => (
  <div>
    <h2>{title}</h2>
    <p>총 {itemCount}개의 전자제품이 있습니다.</p>
    <p>이번 주 특가 브랜드: {featuredBrand}</p>
  </div>
);

// ClothingComponent.jsx
const ClothingComponent = ({ title, itemCount, salePercentage }) => (
  <div>
    <h2>{title}</h2>
    <p>총 {itemCount}개의 의류 제품이 있습니다.</p>
    <p>전 품목 {salePercentage}% 할인 중!</p>
  </div>
);

// BooksComponent.jsx
const BooksComponent = ({ title, itemCount, bestSeller }) => (
  <div>
    <h2>{title}</h2>
    <p>총 {itemCount}권의 도서가 있습니다.</p>
    <p>이번 주 베스트셀러: {bestSeller}</p>
  </div>
);

```

1. App.jsx 파일에서 동적 컴포넌트를 구현합니다:

```jsx
import { useState } from 'react';
import ElectronicsComponent from './ElectronicsComponent';
import ClothingComponent from './ClothingComponent';
import BooksComponent from './BooksComponent';

const componentMapping = {
  Electronics: ElectronicsComponent,
  Clothing: ClothingComponent,
  Books: BooksComponent,
};

function DynamicComponent({ componentName, ...props }) {
  const Component = componentMapping[componentName];
  return <Component {...props} />;
}

function App() {
  const [currentCategory, setCurrentCategory] = useState('Electronics');

  const categoryProps = {
    Electronics: { featuredBrand: 'Samsung' },
    Clothing: { salePercentage: 20 },
    Books: { bestSeller: 'React 마스터하기' },
  };

  return (
    <div>
      <h1>온라인 쇼핑몰</h1>
      <div>
        <button onClick={() => setCurrentCategory('Electronics')}>전자제품</button>
        <button onClick={() => setCurrentCategory('Clothing')}>의류</button>
        <button onClick={() => setCurrentCategory('Books')}>도서</button>
      </div>
      <DynamicComponent
        componentName={currentCategory}
        title={`${currentCategory} 카테고리`}
        itemCount={100}
        {...categoryProps[currentCategory]}
      />
    </div>
  );
}

export default App;

```

실습 과제:

1. 위의 코드를 실제로 구현해보세요.
2. 각 카테고리 버튼을 클릭할 때마다 해당 카테고리의 컴포넌트가 렌더링되는지 확인하세요.
3. 공통 props (title, itemCount)와 카테고리별 특정 props (featuredBrand, salePercentage, bestSeller)가 올바르게 전달되는지 확인하세요.
4. **새로운 카테고리 (예: 'Food')를 추가해보세요. 이를 위해 새 컴포넌트를 만들고, componentMapping과 categoryProps에 추가해야 합니다.**
5. **DynamicComponent에 에러 처리를 추가해보세요. 예를 들어, 매핑되지 않은 componentName이 전달될 경우 기본 컴포넌트를 렌더링하도록 만들어보세요.**

이 실습을 통해 동적 컴포넌트의 유연성과 재사용성을 직접 경험할 수 있을 것입니다. 실제로 구현해보면서 질문이 생기면 언제든 물어보세요!

## [에러] The requested module '/src/components/BooksComponent.jsx' does not provide an export named 'default'

---

- return 값이 없음

```jsx
const BooksComponent = ({ title, itemCount, bestSeller }) => (
  <div>
    <h2>{title}</h2>
    <p>총 {itemCount}권의 도서가 있습니다.</p>
    <p>이번 주 베스트셀러: {bestSeller}</p>
  </div>
)

export default BooksComponent
```

## [에러] App.jsx:36 Uncaught ReferenceError: props is not defined

---

```jsx
  return (
    <div>
      {/* 일단 dyanmucComponent 자체가 앱이고, 그걸 클릭으로 바꿀 것 */}
      <DynamicComponent
      // 지금 들어가 있는 title로 설정 
      props={props}
      title={title}/>
      <button onClick={() => setTitle('Books')}>책</button>
      <button onClick={() => setTitle('Clothing')}>옷</button>
      <button onClick={() => setTitle('Electronic')}>전자기기</button>
    </div>
  )
```

- 각각 다른 props를 어떻게 넣고 접근해야할지 모르겠음

```jsx
const DynamicComponent = (title, itemCount, {...props}) => {// ProudctName을 기반으로 props 받기
  const Component = Product[title] //Component가 어떠한 컴포넌트인지 잡아오고
  //props 값 활용
  return <Component title={title} itemCount={itemCount} props={...props}
  />
}
```

⇒ 일반적으로 React의 함수형 컴포넌트에서는 `props를 하나의 객체로` 전달받는 것이 일반

## 각각 다른 props에 접근하는 방법

---

```jsx
const DynamicComponent = ({ title, itemCount, ...props }) => {
```

여기서 `props={...props}` 는 잘못된 사용 ⇒ props는 이미 스프레드 문법으로 사용되고 있으므로, 컴포넌트에 전달할 때는 직접 넘겨줘야 합니다. 

```jsx
return <Component title={title} itemCount={itemCount} {...props} />;
```

## [에러] TypeError: Cannot read properties of null (reading 'addEventListener')

---

```jsx
    <div>
      {/* 일단 dyanmucComponent 자체가 앱이고, 그걸 클릭으로 바꿀 것 */}
      <DynamicComponent
      // 지금 들어가 있는 title로 설정 
      title={title}/>
      <button onClick={() => setTitle('Books')}>책</button>
      <button onClick={() => setTitle('Clothing')}>옷</button>
      <button onClick={() => setTitle('Electronic')}>전자기기</button>
    </div>
  )
```

- addEventListner를 읽을 수 없다? :  [https://velog.io/@sorikikikim/Cannot-read-properties-of-null-reading-addEventListener](https://velog.io/@sorikikikim/Cannot-read-properties-of-null-reading-addEventListener)
    - 에러가 로딩되기전에 JS에서 HTML을 참조하기 때문
    - 일반적으로 DOM 요소가 존재하지 않을 때 발생합니다.  === `null` 인 경우
    - **컴포넌트 마운트 시점**: **`useEffect`**를 사용해 컴포넌트가 마운트된 후에 이벤트 리스너를 추가하도록 하는 것이 좋습니다

## [문제] 지금 Books, Clothing, Electronic이라는 Key만 제공하고, 실제 내부 데이터는 아무것도 없는 문제

---

```jsx
const DynamicComponent = ({title, itemCount, ...props}) => {// ProudctName을 기반으로 props 받기
  const Component = Product[title] //Component가 어떠한 컴포넌트인지 잡아오고
  //props 값 활용
  return <Component title={title} itemCount={itemCount} {...props}
  />
} 

function App() {
  //동적으로 바뀔 컴포넌트 앱 => 앱 컴포넌트는 존재하니, 들어갈 매개변수 값들이 바뀔 것
  const [title, setTitle] = useState('Books') //책을 기본값으로 설정

  return (
    <div>
      {/* 일단 dyanmucComponent 자체가 앱이고, 그걸 클릭으로 바꿀 것 */}
      <DynamicComponent
      // 지금 들어가 있는 title로 설정 
      itemCount={itemCount}
      {...props}
      title={title}/>
      <button onClick={() => setTitle('Books')}>책</button>
      <button onClick={() => setTitle('Clothing')}>옷</button>
      <button onClick={() => setTitle('Electronic')}>전자기기</button>
    </div>
  )
}

```

# 실습

---

## 실습 과제: 음식 카테고리 앱

이 앱에서는 사용자가 선택한 음식 카테고리에 따라 해당 카테고리의 음식을 보여주는 동적 컴포넌트를 만들어보세요. 카테고리는 **한식**, **양식**, **중식**으로 구성됩니다.

### 1. 각각의 음식 컴포넌트 생성하기

각 카테고리에 맞는 음식을 보여주는 컴포넌트를 생성하세요.

```jsx
// KoreanFood.jsx
const KoreanFood = () => (
  <ul>
    <li>김치찌개</li>
    <li>불고기</li>
    <li>비빔밥</li>
  </ul>
);

export default KoreanFood;

// ItalianFood.jsx
const ItalianFood = () => (
  <ul>
    <li>파스타</li>
    <li>피자</li>
    <li>라자냐</li>
  </ul>
);

export default ItalianFood;

// ChineseFood.jsx
const ChineseFood = () => (
  <ul>
    <li>짜장면</li>
    <li>탕수육</li>
    <li>볶음밥</li>
  </ul>
);

export default ChineseFood;

```

### 2. 음식 카테고리 컴포넌트 생성하기

`ProductList` 컴포넌트처럼, 음식 카테고리를 선택할 수 있는 메인 컴포넌트를 작성하세요. 여기서 선택된 카테고리에 따라 동적으로 해당 음식을 보여줘야 합니다.

### 3. App 컴포넌트

`App` 컴포넌트에서 `ProductList`를 불러오는 방식으로 구성하세요.

```jsx
import React, { useState } from 'react';
import KoreanFood from './KoreanFood';
import ItalianFood from './ItalianFood';
import ChineseFood from './ChineseFood';

const FoodList = () => {
  const [category, setCategory] = useState("Korean");

  const renderFoodComponent = () => {
    switch (category) {
      case "Italian":
        return <ItalianFood />;
      case "Chinese":
        return <ChineseFood />;
      default:
        return <KoreanFood />;
    }
  };

  return (
    <div>
      <h1>음식 카테고리</h1>
      <select onChange={(e) => setCategory(e.target.value)}>
        <option value="Korean">한식</option>
        <option value="Italian">양식</option>
        <option value="Chinese">중식</option>
      </select>
      {renderFoodComponent()}
    </div>
  );
};

function App() {
  return (
    <div>
      <FoodList />
    </div>
  );
}

export default App;

```

### 4. 코드 실행

위의 컴포넌트들을 모두 작성한 뒤, 한 번 실행해 보세요. 선택된 음식 카테고리에 따라 음식 리스트가 동적으로 변경되는 것을 확인할 수 있을 것입니다.

### 5. 추가 기능 (Optional)

- **스타일링**: CSS를 추가하여 보기 좋게 스타일링 해보세요.
- **상세보기**: 각 음식 항목을 클릭했을 때, 해당 음식을 자세히 설명하는 팝업이나 모달을 구현해보세요.

이 실습 과제를 통해 React의 동적 컴포넌트를 효과적으로 활용해보실 수 있기를 바랍니다. 질문이 있거나 도움이 필요하시면 언제든지 말씀해 주세요!

# [에러] Warning: Functions are not valid as a React child. This may happen if you return a Component instead of <Component /> from render. Or maybe you meant to call this function rather than return it. Error Component Stack

---

- 함수 `()` 누락

## [오류] All 값이 출력되지 않음

---

- default 값이 전체가 아닌가?

```jsx
      case "default" : //모든 카테고리
        return ( //기본 값으로
          <ul>
            <li>김치찌개</li>
            <li>피자</li>
            <li>불고기</li>
            <li>파스타</li>
            <li>탕수육</li>
            <li>비빔밥</li>
            <li>짜장면</li>
            <li>라자냐</li>
            <li>볶음밥</li>
          </ul>
        )
```

⇒ `Case` ALL로 변경하니까 동작함

<aside>
💡

Default 기본 값

</aside>

```jsx
      default : //모든 카테고리
        return ( //기본 값으로
          <ul>
            <li>김치찌개</li>
            <li>피자</li>
            <li>불고기</li>
            <li>파스타</li>
            <li>탕수육</li>
            <li>비빔밥</li>
            <li>짜장면</li>
            <li>라자냐</li>
            <li>볶음밥</li>
          </ul>
        )
```

# ⚠️ [결론] **일반 상태 관리와의 비교**

---

- 일반적인 상태 관리 방식은 데이터가 복잡해질수록 관리하기 어려울 수 있습니다. 다음과 같은 점에서

`useState` 와 React의 동적 컴포넌트 렌더링 방식이 유리합니다:

- **상태를 명확하게 관리**: 특정 상태 값이 변경될 때 어떤 UI가 변경될지를 명확하게 정의할 수 있습니다.
- **구조화된 코드**: 각 데이터나 UI 상태에 대한 처리를 명확하게 구조화할 수 있어, 코드의 유지 보수성이 향상됩니다.

<aside>
💡

이와 같이 동적 컴포넌트는 `사용자의 선택에 따라` 실시간으로 UI를 변경하는 데 유용하고, 
SPA 라우팅은 여러 페이지를 효과적으로 관리할 수 있도록 도와줍니다. 
두 가지 방식을 적절히 활용하면 더욱 효율적이고 사용하기 편리한 애플리케이션을 만들 수 있습니다. 추가로 궁금한 점이 있으시면 언제든지 말씀해 주세요!

</aside>

| **특성** | **동적 컴포넌트 (예: useState 활용)** | **SPA 라우팅 (예: React Router)** |
| --- | --- | --- |
| **사용 용도** | 사용자 선택에 따라 UI 요소(dynamic rendering) 변경 | 페이지 간 내비게이션 및 URL 관리 |
| **상태 관리** | **상태 변화에 따라 동적으로 컴포넌트를 렌더링** | **URL 변화에 따른 컴포넌트 전환** |
| **UI 변경 방식** | 특정 컴포넌트 내에서의 데이터와 UI 변경만 발생 | 페이지 전체가 변경되며 새로운 컴포넌트를 로드 |
| **상태 보존** | 상태가 컴포넌트 내에 저장되므로 같은 컴포넌트 내에서만 유지 | 라우터의 상태 관리 기능을 활용하면 페이지 간 상태 유지 가능 |
| **주요 예** | **드롭다운, 토글 버튼, 필터링 옵션 등 
사용자의 즉각적 상호작용 시** | **여러 페이지를 가진 블로그, 쇼핑몰 등 
내비게이션이 필요한 애플리케이션** |
| **렌더링 성능** | 필요할 때만 특정 컴포넌트를 렌더링함으로써 성능 최적화 가능 | 라우팅 시 전체 페이지를 로드할 수 있어 초기 로딩 속도가 느려질 수 있음 |
| **쿠키/세션 관리** | 상태를 저장하여 UI에서 직접적으로 제어 | URL을 기반으로 경로 관리를 통해 사용자의 위치를 관리하고 세션 유지 가능 |