import {useGetDataApi, usePostDataApi} from "hooks/useApi";

type Props = {
    content: string;
    userId: string;
    timestamp: string;
}

export function usePostDiary(params: Props){
    const [ d, loading, error, loadFn ] = usePostDataApi(`/diary`, params);
}

function useGetDiary(){
    const [ d, loading, error, loadFn ] = useGetDataApi(`/diary`);
    const diary = d || [];
    return diary;
}
export default useGetDiary;