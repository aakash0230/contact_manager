import React, { useState } from 'react';
import { addPhoneNumber } from '../../../api';
import './addPhone.scss';
import { useNavigate } from 'react-router-dom';

const AddPhone = () => {
    const [phoneNumber, setPhoneNumber] = useState('');
    const [name, setName] = useState('');
    const navigate = useNavigate()

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response  = await addPhoneNumber({ phone_number: phoneNumber, name });
        alert(response.data.message)
        navigate('/phone-list')

    };

    return (
        <div className="add-phone-container">
            <form onSubmit={handleSubmit} className="add-phone-form">
                <input 
                    type="text" 
                    placeholder="Enter your name" 
                    value={name} 
                    onChange={(e) => setName(e.target.value)} 
                    className="name-input"
                />
                <input 
                    type="text" 
                    placeholder="Enter phone number" 
                    value={phoneNumber} 
                    onChange={(e) => setPhoneNumber(e.target.value)} 
                    className="phone-input"
                />
                <button type="submit" className="add-phone-button">
                    Add Phone Number
                </button>
            </form>
        </div>
    );
};

export default AddPhone;
