import { useLocation } from "react-router-dom";

type Params = {
  [key: string]: string;
};

function useSearchParams() {
  const location = useLocation();
  const { search, pathname } = location;
  const strParams = search.slice(1);
  const entries = strParams.length > 0 ? strParams.split("&").map((s) => s.split("=")) : null;
  const params: Params | null = entries ? Object.fromEntries(entries) : null;
  return {
    path: pathname,
    params: params ? params : {},
  };
}

export default useSearchParams;
