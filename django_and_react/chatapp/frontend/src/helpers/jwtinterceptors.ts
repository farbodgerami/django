import axios, { AxiosInstance } from "axios";
import { useNavigate } from "react-router-dom";
import { BASEURL } from "../config";

const API_BASE_URL = BASEURL;

const useAxioswithinterceptor = (): AxiosInstance => {
  const jwtAxios = axios.create({ baseURL: API_BASE_URL });
  const navigate = useNavigate();
  jwtAxios.interceptors.response.use(
    (response) => {
      return response;
    },
    async (error) => {
      const originalRequest = error.config;
      if (error.response?.status === 403) {
        const goRoot = () => navigate("/test");
        goRoot();
      }
    }
  );
  return jwtAxios;
};

export default useAxioswithinterceptor;
