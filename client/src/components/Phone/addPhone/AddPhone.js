import React, { useState } from 'react';
import { addPhoneNumber } from '../../../api';
import './addPhone.scss';

const AddPhone = () => {
    const [phoneNumber, setPhoneNumber] = useState('');
    const [name, setName] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        await addPhoneNumber({ phone_number: phoneNumber, name });
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
