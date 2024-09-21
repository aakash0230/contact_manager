import axios from 'axios';

// Base API instance
const api = axios.create({
    baseURL: 'http://localhost:5000',
});

api.interceptors.request.use((config) => {
    const token = localStorage.getItem('authToken');
    if (token && !['/auth/getOtp', '/auth/verifyOtp', '/auth/createPassword', '/auth/login'].includes(config.url)) {
        config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
}, (error) => {
    return Promise.reject(error);
});

// API Calls
export const getOtp = (data) => api.post('/auth/getOtp', data);
export const verifyOtp = (data) => api.post('/auth/verifyOtp', data);
export const createPassword = (data) => api.post('/auth/createPassword', data);
export const login = (data) => api.post('/auth/login', data);
export const addPhoneNumber = (data) => api.post('/userPhone/addNumber', data);
export const getPhoneNumbers = () => api.post('/userPhone/getNumber');
export const markAsSpam = (data) => api.post('/phoneSpam/markSpam', data);
export const markAsUnspam = (data) => api.post('/phoneSpam/markUnSpam', data);
