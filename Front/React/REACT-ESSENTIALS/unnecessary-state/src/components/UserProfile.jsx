// UserProfile.js

import { useState } from "react";

//자체 상태관리

function UserProfile() {
  //근데 이것도 input값을 객체로 만드는게 낫지 않는지..? 계산 로직에서
  const [firstName, setFirstName] = useState("")
  const [lastName, setLastName] = useState("")

  const fullName = `${firstName}${lastName}`

  const onChangeFirst = (e) => {
    setFirstName(e.target.value)
  }

  const onChangeLast = (e) => {
    setLastName(e.target.value)
  }

  return (
    <div>
      <h1>User Profile</h1>
      <input type="text" name="" id=""
      value={firstName}
      onChange={onChangeFirst} />
      <input type="text" name="" id="" 
      value={lastName}
      onChange={onChangeLast}/>
      <h2>Check your Full Name! : {fullName}</h2>
    </div>
  );
}

export default UserProfile;