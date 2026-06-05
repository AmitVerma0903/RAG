import axios from "axios"

const baseURL =
  process.env.NODE_ENV === "production"
    ? "https://rag-production-9052.up.railway.app"
    : "http://localhost:8000"

const axiosInstance = axios.create({
  baseURL,
})

export default axiosInstance