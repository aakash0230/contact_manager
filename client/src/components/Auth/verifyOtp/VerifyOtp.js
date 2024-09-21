import React, { useState } from 'react';
import { verifyOtp } from '../../../api';
import { useLocation } from 'react-router-dom';
import { useNavigate } from 'react-router-dom';
import './verifyOtp.scss';

const VerifyOtp = () => {
    const [otp, setOtp] = useState('');
    const location = useLocation();
    const navigate = useNavigate();
    const { email } = location.state || {};

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await verifyOtp({ email, otp });
        if(response.data.status){
            alert(response.data.message);
            navigate('/create-password', {state : {email}});
        }
    };

    return (
        <div className="verify-otp-container">
            <h1 className="verify-otp-title">Verify OTP</h1>
            {email && <p className="otp-info">OTP has been sent to: {email}</p>}
            <form onSubmit={handleSubmit} className="verify-otp-form">
                <input 
                    type="text" 
                    placeholder="Enter your OTP" 
                    value={otp} 
                    onChange={(e) => setOtp(e.target.value)} 
                    className="input-field"
                />
                <button type="submit" className="submit-btn">Verify OTP</button>
            </form>
        </div>
    );
};

export default VerifyOtp;
