import React, { useState } from "react";
import useAxioswithinterceptor from "../helpers/jwtinterceptors";
import { BASEURL } from "../config";

interface IuseCrud<T> {
  fetchData: () => Promise<void>;
  dataCRUD: T[];
  error: Error | null ;
  isLoading:boolean
}
export const useCruds = <T>(initialData: T[], apiUrl: string): IuseCrud<T> => {
  const [dataCRUD, setDataCrud] = useState<T[]>(initialData);
  const [error,setError]=useState<Error | null >(null)
  const [isLoading,setIsloading]= useState(false)
  const jwtAxios = useAxioswithinterceptor();
  const fetchData = async () => {
    setIsloading(true)
    try {
      const response = await jwtAxios.get(`${BASEURL}${apiUrl}`, {});
      setDataCrud(response.data)
      // console.log(response.data)
      setError(null)
      setIsloading(false)
      return response.data
    } catch (error: any) {
      if(error.response && error.response.status===400){
        setError(new Error("400"))
      }
      setIsloading(false)
      throw error
    }
  };
  return {fetchData,dataCRUD,error,isLoading};
};

export default useCruds;
