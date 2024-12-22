import ProjectItem from '../components/ProjectItem'
import { projects } from '../utils/get-project-data'
import './Project.css'

const Project = () => {



  return (
    <div className="Project">
      <div className='project_title'>
        <a href="https://github.com/JUMINAHN/Deposit_Recommendation_Zip"><h1>💲SSAFY 금융 관통 프로젝트 : 예적금 맛ZIP💲</h1></a>
        <p>🌟관통 프로젝트 우수상🌟</p>
      </div>
      <div className='project_wrap'>
        {
          projects.map((item) => 
            <div className='project_detail'
            key={item.title}>
              <ProjectItem 
              {...item}/>
            </div>
          )
        }
      </div>
    </div>
  )
}

export default Project