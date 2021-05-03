import {useGetDataApi, usePostDataApi} from "hooks/useApi";

export function usePostUser(username: string){
    const [ d, loading, error, loadFn ] = usePostDataApi(`/user`, {
        name: username
    });
    const userid = d?.id;
    return {userid, loading};
}

function useUser(){
    const [ d, loading, error, loadFn ] = useGetDataApi(`/users`);
    const [ userId, username ] = d || [];
    return username;
}
export default useUser;