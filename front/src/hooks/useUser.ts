import {useGetDataApi} from "hooks/useApi";

function useUser(){
    const [ d, loading, error, loadFn ] = useGetDataApi(`api/v1/diary/users`);
    const [ userId, username ] = d || [];
    return username;
}
export default useUser;