import React from 'react';
import {Routes, Route, Navigate } from 'react-router-dom';
import VerifyOtp from './components/Auth/verifyOtp/VerifyOtp';
import CreatePassword from './components/Auth/CreatePassword/CreatePassword';
import AddPhone from './components/Phone/addPhone/AddPhone';
import PhoneList from './components/Phone/phoneList/PhoneList';
import GetOtp from './components/Auth/getOtp/GetOtp';
import Login from './components/Auth/login/Login';

const isAuthenticated = () => !!localStorage.getItem('authToken');

const App = () => {
    return (
          <Routes>
                <Route path="*" Component={Login} />
                <Route path="/get-otp" Component={GetOtp} />
                <Route path="/verify-otp" Component={VerifyOtp} />
                <Route path="/create-password" Component={CreatePassword} />
                <Route
                  path="/add-phone"
                  element={isAuthenticated() ? <AddPhone /> : <Navigate to="/" />}
                />
                  <Route
                   path="/phone-list"
                        element={isAuthenticated() ? <PhoneList /> : <Navigate to="/" />}
                  />
                <Route path="/add-phone" Component={AddPhone} />
                <Route path="/phone-list" Component={PhoneList} />
          </Routes>
    );
};

export default App;
