import React, { useState, useEffect, memo } from 'react';
import { Typography, Button, Grid, Modal, makeStyles } from "@material-ui/core";
import { Link, useHistory } from "react-router-dom";
import ContentWrapper from "components/atoms/ContentWrapper";
import {useGetTopics, useGetQuestions} from "hooks/useGetTemplate";
import { Content } from 'antd/lib/layout/layout';
import axios, { AxiosResponse } from "axios";

const useStyles = makeStyles((theme) => ({
  button: {
      width: "100px",
      height: "100px",
      borderRadius: "20px",
      backgroundColor: "red",
      fontWeight: "bold",
      color: "#FFF"
  },
  text: {
      margin: "30px 0",
      fontWeight: "bold"
  },
  buttonSection: {
      marginTop: "60px"
  },
  modal: {
      width: "300px",
      minHeight: "200px",
      backgroundColor: "#FFF",
      margin: "50px auto"
  }
}));
const TempleteStuPage = React.memo(() => {
    const [open, setOpen] = useState(false);
    const [data, setData] = useState([]);
    const [topicid, setTopicId] = useState("")
    const classes = useStyles();
    const topics = useGetTopics();
    console.log(topics);
    console.log(data)
    useEffect(() => {
        console.log(topicid)
        const getData = async () => {
        const response = await axios.get(
            `http://jackhack-2021-server-1783148408.ap-northeast-1.elb.amazonaws.com/questions/${topicid}`
        )
        setData(response.data)
        }
        getData();
        if(topicid != ""){
            console.log(data)
            setOpen(true);
        }
    }, [topicid])
    const handleChange = (id: string) => {
        setTopicId(id);
    }
    const onClose = () => {
        setOpen(false)
    }
    return (
        <ContentWrapper>
            <Typography className={classes.text}>
                話題を選んでください
            </Typography>
            <Grid container spacing={6} alignItems="center">
                {topics.length > 0 && (
                    topics.map((v: any) => (
                    <Grid item xs={6} key={v.id}>
                        <Button className={classes.button} onClick={() => handleChange(v.id)}>
                            {v.name}
                        </Button>
                    </Grid>
                )))}
            </Grid>
            <Modal open={open} onClose={onClose}>
                <div className = {classes.modal}>
                    <Typography>
                        関連する質問
                    </Typography>
                    {data.length > 0 ? (
                        data.map((v: any) => (
                            <Typography key={v.id}>
                                {v.content}
                            </Typography>
                        ))
                    ) : (
                        <Typography>
                            関連した質問は存在しません<br/>
                            持ち前のコミュ力で乗り切りましょう。
                        </Typography>
                    )}
                </div>
                
            </Modal>
        </ContentWrapper>
    )
})
export default TempleteStuPage;