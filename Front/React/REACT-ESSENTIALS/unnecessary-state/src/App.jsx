// App.js
import React from 'react';
//불필요한 더하기 => 반응이 느림
import UserProfile from './components/UserProfile';
// import UserProfile from './components/UserProfile3';

//확실히 반응이 빠름
function App() {
  return (
    <div>
      <UserProfile />
    </div>
  );
}

export default App;