import './ProjectItem.css'

const ProjectItem = ({title, gif, descriptions}) => {
  return (
    <div className="ProjectItem">
      <section className='info_section info_title'>
        <p>{title}</p>
      </section>
      <section className='img_section'>
        <img src={gif} alt="" />
        {/* gif도 정상작동하는 것을 볼 수 있음 */}
      </section>
      <section className='info_section info_content'>
        <p>{descriptions}</p>
      </section>
    </div>
  )
}

export default ProjectItem