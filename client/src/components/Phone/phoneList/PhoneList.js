import React, { useEffect, useState } from 'react';
import { getPhoneNumbers, markAsSpam } from '../../../api';
import { useNavigate } from 'react-router-dom';
import './phoneList.scss'; // Importing the SCSS file

const PhoneList = () => {
    const [phoneNumbers, setPhoneNumbers] = useState([]);
    const [searchTerm, setSearchTerm] = useState('');
    const navigate = useNavigate(); // Use the navigate hook

    useEffect(() => {
        const fetchPhoneNumbers = async () => {
            const response = await getPhoneNumbers();
            setPhoneNumbers(response.data.data);
        };

        fetchPhoneNumbers();
    }, []);

    const handleMarkAsSpam = async (phone_no) => {
        const response = await markAsSpam({ phone_number: phone_no });
        if (response.data.status) {
            alert(response.data.message);
            const updatedResponse = await getPhoneNumbers();
            setPhoneNumbers(updatedResponse.data.data);
        } else {
            alert(response.data.message);
        }
    };

    const handleAddPhone = () => {
        navigate('/add-phone');
    };

    const filteredPhoneNumbers = phoneNumbers.filter(phone =>
        phone.phone_no.includes(searchTerm)
    );

    return (
        <div className="phone-list-container">
            <button className="add-phone-btn" onClick={handleAddPhone}>
                Add Phone Number
            </button>
            <input 
                type="text" 
                className="search-bar" 
                placeholder="Search by phone number..." 
                value={searchTerm} 
                onChange={(e) => setSearchTerm(e.target.value)} 
            />
            <table className="phone-list-table">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Phone Number</th>
                        <th>Spam Likelihood</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {filteredPhoneNumbers.map((phone) => (
                        <tr key={phone.phone_no}>
                            <td>{phone.name}</td>
                            <td>{phone.phone_no}</td>
                            <td>{phone.spam_percentage}%</td>
                            <td>
                                <button 
                                    className="mark-spam-btn" 
                                    onClick={() => handleMarkAsSpam(phone.phone_no)}
                                >
                                    Mark as Spam
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default PhoneList;
