import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import './bootstrap.min.css'
import store from './store'
import {Provider} from 'react-redux'
ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById('root')
);

