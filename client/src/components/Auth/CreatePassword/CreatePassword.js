import React, { useState } from 'react';
import { createPassword } from '../../../api';
import { useNavigate, useLocation } from 'react-router-dom';
import './createPassword.scss';

const CreatePassword = () => {
    const [password, setPassword] = useState('');
    const navigate = useNavigate();
    const location = useLocation();
    const { email } = location.state || {};

    const handleSubmit = async (e) => {
        e.preventDefault();
        await createPassword({ email, password });
        navigate('/');
    };

    return (
        <form onSubmit={handleSubmit} className="create-password-form">
            <input 
                type="password" 
                placeholder="Create a password" 
                value={password} 
                onChange={(e) => setPassword(e.target.value)} 
                className="input-field"
            />
            <button type="submit" className="submit-btn">Create Password</button>
        </form>
    );
};

export default CreatePassword;
