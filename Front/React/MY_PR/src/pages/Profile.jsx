import React, { useState, useEffect } from 'react';
import './Profile.css';
import myImg from '../assets/profileImg/profile.jpg'
import myBag from '../assets/mainImg/001.png'
import github from '../assets/profileImg/github.webp'
import linkedin from '../assets/profileImg/linkedin.avif'
import mail from '../assets/profileImg/mail.png'
import til from '../assets/profileImg/til.png'

const Profile = () => {

  return (
    <div className='Profile'>
      {/* container */}
      <div className='Profile_wrapper'>
        <section className='left_section'>
          <div className='image_container'> 
            <img src={myImg} alt="" />
          </div>
          <h1>안주민</h1>
        </section>
        <section className='right_section'>
          <div className='title_container'>
            <p>어제보다 <strong>오늘</strong>, 오늘보다 <strong>내일</strong> 더 </p>
            <p><strong>성장</strong>하고 싶은 FE 개발자 <strong>안주민</strong>입니다.</p>
          </div>
          <hr />
          <div className='link_container'>
            <div className='link_image_container'>
              <a href="https://github.com/JUMINAHN"><img src={github} alt="github" /></a>
            </div>
            <div className='link_image_container'>
              <a href="https://www.linkedin.com/in/jumin-ahn/"><img src={linkedin} alt="linkedin" /></a>
            </div>
            <div className='link_image_container'>
              <a href="https://zoom-in.notion.site/TIL-15ac4eca659c80ed9bb1d075fd64cb75"><img src={til} alt="notion_til" /></a>
            </div>
            <div className='link_image_container'>
              <a href="mailto:jumin9774@naver.com"><img src={mail} alt="mail" /></a>
            </div>
          </div>
        </section>
      </div>
    </div>
  )
};

export default Profile;
