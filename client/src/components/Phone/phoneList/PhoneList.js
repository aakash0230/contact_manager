import React, { useEffect, useState } from 'react';
import { getPhoneNumbers, markAsSpam, unmarkAsSpam } from '../../../api';
import './phoneList.scss';

const PhoneList = () => {
    const [phoneNumbers, setPhoneNumbers] = useState([]);
    const [searchQuery, setSearchQuery] = useState('');

    useEffect(() => {
        const fetchPhoneNumbers = async () => {
            const response = await getPhoneNumbers({query : searchQuery});
            setPhoneNumbers(response.data.data);
        };

        fetchPhoneNumbers();
    }, [searchQuery]);

    const handleMarkAsSpam = async (phone_no) => {
        const response = await markAsSpam({ phone_number: phone_no });
        if (response.data.status) {
            alert(response.data.message);
            refreshPhoneList();
        } else {
            alert(response.data.message);
        }
    };

    const handleUnmarkAsSpam = async (phone_no) => {
        const response = await unmarkAsSpam({ phone_number: phone_no });
        if (response.data.status) {
            alert(response.data.message);
            refreshPhoneList();
        } else {
            alert(response.data.message);
        }
    };

    const refreshPhoneList = async () => {
        const response = await getPhoneNumbers({query : searchQuery});
        setPhoneNumbers(response.data.data);
    };

    return (
        <div className="phone-list-container">
            <div className="phone-list-actions">
                <button onClick={() => window.location.href = '/add-phone'}>Add Phone Number</button>
                <input
                    type="text"
                    className="search-bar"
                    placeholder="Search by phone number or name"
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)} // Update the search query
                />
            </div>
            
            <table className="phone-list-table">
                <thead>
                    <tr>
                        <th>Phone Number</th>
                        <th>Name</th>
                        <th>Spam Count</th>
                        <th>Spam Likelihood</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    {phoneNumbers.map((phone) => (
                        <tr key={phone.phone_no}>
                            <td>{phone.phone_no}</td>
                            <td>{phone.name}</td>
                            <td>{phone.spam_count}</td>
                            <td>{phone.spam_percentage}%</td>
                            <td>
                                {phone.marked_as_spam ? (
                                    <button 
                                        className="unmark-spam-btn" 
                                        onClick={() => handleUnmarkAsSpam(phone.phone_no)}
                                    >
                                        Unmark as Spam
                                    </button>
                                ) : (
                                    <button 
                                        className="mark-spam-btn" 
                                        onClick={() => handleMarkAsSpam(phone.phone_no)}
                                    >
                                        Mark as Spam
                                    </button>
                                )}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default PhoneList;
