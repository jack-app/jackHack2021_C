import {useGetDataApi, usePostDataApi} from "hooks/useApi";

type Props = {
    content: string;
    userId: string;
    timestamp: string;
}

export function usePostDiary(params: Props){
    const [ d, loading, error, loadFn ] = usePostDataApi(`api/v1/diary`, params);
}

function useGetDiary(userId: string){
    const [ d, loading, error, loadFn ] = useGetDataApi(`api/v1/diary/${userId}`);
    const diary = d || [];
    return diary;
}
export default useGetDiary;