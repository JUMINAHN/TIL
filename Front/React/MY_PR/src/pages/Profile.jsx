import React, { useState, useEffect } from 'react';
import './Profile.css';

const Profile = () => {
  // 타이핑되는 텍스트를 저장하는 상태
  const [typedText, setTypedText] = useState('');
  // 두 번째 페이즈(프로필 섹션) 표시 여부를 결정하는 상태
  const [showSecondPhase, setShowSecondPhase] = useState(false);
  // 타이핑될 전체 텍스트
  const fullText = "어제보다 오늘, 오늘보다 내일 더 성장";
  // 타이핑 속도 (밀리초 단위)
  const typingSpeed = 150;

  useEffect(() => {
    let currentText = '';
    let index = 0;
    
    // 타이핑 효과를 위한 인터벌 설정
    const interval = setInterval(() => {
      if (index < fullText.length) {
        // 현재 인덱스까지의 텍스트를 잘라서 설정
        currentText = fullText.slice(0, index + 1);
        setTypedText(currentText);
        index++;
      } else {
        // 타이핑이 완료되면 인터벌 중지
        clearInterval(interval);
        // 1초 후에 두 번째 페이즈 표시
        setTimeout(() => {
          setShowSecondPhase(true);
        }, 1000);
      }
    }, typingSpeed);
  
    // 컴포넌트 언마운트 시 인터벌 정리
    return () => clearInterval(interval);
  }, []);

  // 텍스트 포맷팅 함수: 특정 단어('오늘', '내일')에 하이라이트 효과 적용
  const formatText = (text) => {
    // 빈 문자열일 경우 빈 배열 반환
    if (!text) return [];
    
    return text.split(' ').map((word, index) => {
      // 마지막 단어가 아닐 경우에만 공백 추가
      const space = index === text.split(' ').length - 1 ? '' : ' ';
      // '오늘'이나 '내일' 단어에 하이라이트 클래스 적용
      if (word === '오늘' || word === '내일') {
        return <span key={index} className="highlight">{word}{space}</span>;
      }
      return <span key={index}>{word}{space}</span>;
    });
  };

  return (
    <div className="Profile">
      {/* 타이핑 효과가 표시되는 컨테이너 */}
      <div className={`typing-container ${showSecondPhase ? 'fade-out' : ''}`}>
        <h1>{formatText(typedText)}</h1>
      </div>
      
      {/* 프로필 정보가 표시되는 두 번째 페이즈 */}
      <div className={`second-phase ${showSecondPhase ? 'fade-in' : ''}`}>
        <div className="profile-content">
          <div className="profile-image">
            {/* 프로필 이미지가 들어갈 위치 */}
          </div>
          {/* 프로필 텍스트 */}
          <p className="profile-text">
            어제보다 오늘, 오늘보다 내일 더 성장하고 싶은 FE 개발자 안주민입니다.
          </p>
        </div>
      </div>
    </div>
  );
};

export default Profile;
