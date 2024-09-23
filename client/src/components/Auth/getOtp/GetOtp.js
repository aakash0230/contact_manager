import React, { useState } from 'react';
import { getOtp } from '../../../api';
import { useNavigate } from 'react-router-dom';
import './getOtp.scss';  

const GetOtp = () => {
    const [email, setEmail] = useState('');
    const [name, setName] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await getOtp({ name, email });
        if(response.data.status){
            alert(response.data.message)
            navigate('/verify-otp', {state : {email}})
        }
        else{
            alert(response.data.message)
        }
    };

    return (
        <form onSubmit={handleSubmit} className="get-otp-form">
            <input 
                type="text" 
                placeholder="Enter your name" 
                value={name} 
                onChange={(e) => setName(e.target.value)} 
                className="input-field"
            />
            <input 
                type="email" 
                placeholder="Enter your email" 
                value={email} 
                onChange={(e) => setEmail(e.target.value)} 
                className="input-field"
            />
            <button type="submit" className="submit-btn">Get OTP</button>
        </form>
    );
};

export default GetOtp;
