import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';

function App() {
  useEffect(() => {
    fetch("/flaskSV").then(
      // response 객체의 json() 이용하여 json 데이터를 객체로 변화
      res => res.json()
    ).then(
      // 데이터를 콘솔에 출력
      data => console.log(data)
    )
  },[])

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React222
        </a>
      </header>
    </div>
  );
}

export default App;