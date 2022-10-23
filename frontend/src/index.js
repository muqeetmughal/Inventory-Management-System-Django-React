import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.less';
import App from './App';
// import reportWebVitals from './reportWebVitals';
import { QueryClientProvider, QueryClient } from 'react-query'
import { Routes, Route } from 'react-router-dom';

import CustomRouter from './components/CustomRouter';
import customHistory from './common/custom_history';

import { ReactQueryDevtools } from 'react-query/devtools'
const query_client = new QueryClient()

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <QueryClientProvider client={query_client}>


      <CustomRouter history={customHistory}>



        {/* <ConfigProvider> */}
        <Routes>

          <Route path='/*' element={<App />} />
        </Routes>
        {/* </ConfigProvider> */}
      </CustomRouter>
      <ReactQueryDevtools initialIsOpen={false} position="bottom-right" />
    </QueryClientProvider>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
// reportWebVitals();
