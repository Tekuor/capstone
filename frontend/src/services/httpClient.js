import axios from 'axios';

const httpClient = axios.create({
    baseURL: 'http://127.0.0.1:5000/',
    timeout: 5000,
    headers: {
        "Content-Type": "application/json",
    }
});

const getAuthToken = () => `Bearer ${localStorage.getItem('token')}`;

const authInterceptor = (config) => {
    config.headers['Authorization'] = getAuthToken();
    return config;
}

httpClient.interceptors.request.use(authInterceptor);

httpClient.interceptors.request.use(request => {
    return request
})

export default httpClient;