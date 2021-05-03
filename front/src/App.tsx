import React from 'react';
import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import TopPage from "container/TopPage";
import TempleteStuPage from "container/TempleteStuPage";
import RecordPage from "container/RecordPage";
import SelectPage from "container/SelectPage";
import DiaryPage from "container/DiaryPage";
function App() {
  return (
    <div className="App">
      <Router>
              <div>
                <Route exact path="/" component={TopPage} />
                <Route path="/template" component={TempleteStuPage} />
                <Route path="/record_sound" component={RecordPage} />
                <Route path="/user" component={SelectPage}/>
                <Route path="/diary" component={DiaryPage}/>
              </div>
      </Router>
    </div>
  );
}

export default App;
