import {useGetDataApi} from "hooks/useApi";

export function useGetTypes(){
    const [ d, loading, error, loadFn ] = useGetDataApi('api/v1/template/type')
    const types = d || []
    return types;
}
function useGetTopics(){
    const [ d, loading, error, loadFn ] = useGetDataApi('api/v1//template/topic')
    const topics = d || []
    return topics;
}
function useGetQuestions(type: string){
    const [ d, loading, error, loadFn ] = useGetDataApi(`api/v1//template/questions/${type}`)
    const questions = d || []
    return questions;
}

function useGetTemplate(type: string){
    const topics = useGetTopics();
    const questions = useGetQuestions(type);
    return { topics, questions }
}

export default useGetTemplate;