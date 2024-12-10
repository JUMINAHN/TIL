const ContentComponent = ({ componentName, title }) => {
  return (
    <main>
      <h2>{title}</h2>
      <p>이 곳은 {componentName} 영역입니다. 원하는 내용을 자유롭게 추가할 수 있습니다.</p>
    </main>
  )
}

export default ContentComponent