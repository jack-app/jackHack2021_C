import { useState, useEffect } from 'react';
import axios, { AxiosResponse } from "axios";

const hostname ="http://jackhack-2021-server-1783148408.ap-northeast-1.elb.amazonaws.com"
export function useGetDataApi(
  url: string,
  lazy: boolean = false,
  defaultParams: any = {},
  defaultLoading = !lazy
) {
  const [response, setResponse] = useState<any>(null);
  const [loading, setLoading] = useState<boolean>(defaultLoading);
  const [error, setError] = useState<Error | null>(null);

  const loadFn = (params: any = defaultParams) => {
    setLoading(true);
    axios
      .get(hostname + url, { params })
      .then((res: AxiosResponse<any>) => {
        setResponse(res.data);
        setLoading(false);

      })
      .catch((err: Error) => {
        setError(err);
      });
  };

  useEffect(() => {
    // console.log(hostname + url);
    if (!lazy) loadFn();
  }, [url]);
  return [response, error, loading, loadFn];
};

export function usePostDataApi(
  url: string,
  defaultParams: any = {},
  lazy: boolean = false,
  defaultLoading = !lazy
  ) {
  const [response, setResponse] = useState<any>(null);
  const [error, setError] = useState<Error | null>(null);
  const [loading, setLoading] = useState<boolean>(defaultLoading);
  const loadFn = (params: any) => {
    setLoading(true);
    axios
    .post(hostname + url, params)
    .then((res: AxiosResponse<any>) => {
      setResponse(res.data);
      setLoading(false);
    })
    .catch((err) => {
        console.error(err);
        setError(err);
      });
  };
  useEffect(() => {
    if (!lazy && defaultParams) loadFn(defaultParams);
  }, [url]);
  return [response, error, loadFn];
}