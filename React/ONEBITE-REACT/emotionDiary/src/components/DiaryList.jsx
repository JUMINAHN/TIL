import Button from './Button'
import DiaryListItem from './DiaryListItem'
import './DiaryList.css'


//DiaryList에서 최신순에 대한 데이터 정렬 진행
//새 일기쓰기 컴포넌트 연결
//수정하기 컴포넌트 연결
//click시 다이어리 component연결

const DiaryList = ({data}) => {
  return (
// div 태그 구조 => CSS 설정의 어려움
// div를 사용했으면 일관된 구조로 계속 영역을 나눌 것
  <div className="DiaryList">
    <div className='menu_bar'>
      <select>
        {/* Q. 여기는 왜 value=""로 사용하면 안되는지? */}
        <option value={"latest"}>최신순</option>
        <option value={"oldest"}>오래된 순</option>
      </select>
      <Button text={"새 일기쓰기"}
      type={"POSITIVE"}/>
    </div>
    {/* Q> 언제 div로 묶는지, 묶지 않는지에 대한 감각이 부족한 것 같음 */}

    <div className='list_wrapper'>
      {data.map((item) => 
      //item 자체를 다 줄 것이기 때문에
      <DiaryListItem 
      key={item.id}
      {...item}/>)}
    </div>
  </div>
  )
}

export default DiaryList