import {useGetDataApi} from "hooks/useApi";

export function useGetTypes(){
    const [ d, loading, error, loadFn ] = useGetDataApi('/template/type')
    const types = d || []
    return types;
}
export function useGetTopics(){
    const [ d, loading, error, loadFn ] = useGetDataApi('/topic')
    const topics = d || []
    return topics;
}
export function useGetQuestions(topicid: string){
    const [ d, loading, error, loadFn ] = useGetDataApi(`/template/questions/${topicid}`)
    const questions = d || []
    return questions;
}

function useGetTemplate(type: string){
    const topics = useGetTopics();
    const questions = useGetQuestions(type);
    return { topics, questions }
}

export default useGetTemplate;