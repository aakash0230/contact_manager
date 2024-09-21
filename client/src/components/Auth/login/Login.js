import React, { useState } from 'react';
import { login } from '../../../api';
import { useNavigate } from 'react-router-dom';
import './login.scss';

const Login = () => {
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await login({ email, password });
        if (response.data.status) {
            alert(response.data.message);
            localStorage.setItem('authToken', response.data.data.token);
            navigate('/phone-list');
        } else {
            alert(response.data.message);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="login-form">
            <input 
                type="email" 
                placeholder="Enter your email" 
                value={email} 
                onChange={(e) => setEmail(e.target.value)} 
                className="input-field"
            />
            <input 
                type="password" 
                placeholder="Enter your password" 
                value={password}
                onChange={(e) => setPassword(e.target.value)} 
                className="input-field"
            />
            <button type="submit" className="submit-btn">Login</button>
        </form>
    );
};

export default Login;
