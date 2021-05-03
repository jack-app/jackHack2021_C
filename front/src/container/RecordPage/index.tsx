import React, { useState, useRef, useEffect, useCallback, memo } from 'react';
import ContentWrapper from "components/atoms/ContentWrapper";
import { Typography, Grid, IconButton, makeStyles} from "@material-ui/core";
import SearchIcon from '@material-ui/icons/Search';
import MicIcon from '@material-ui/icons/Mic';
import { useReactMediaRecorder } from "react-media-recorder";
import axios from "axios"
import { ReactMic } from 'react-mic';
const useStyles = makeStyles((theme) => ({
  button: {
  width:"150px",
  height:"150px",
      borderRadius: "",
      backgroundColor:"#21C49C"
  },
  text: {
      fontSize:"20px",
      color: "",
      margin: "20px 0"
  },
  icon: {
      width: "50px",
      height: "50px"
  },
  expSection: {
      margin: "90px 0"
  },
  buttonSection: {
      margin: "100px 0"
  },
  mic: {
      width: "50px"
  }
}));

const RecordPage: React.FC = () => {
    const classes = useStyles();
    const [record, setRecord] = useState(false);
    const requestVoiceAnalyze = (blob: any) =>  {
        const data = new FormData();
        data.append("files", blob, "audio.wav");
        axios
            .post("http://jackhack-2021-server-1783148408.ap-northeast-1.elb.amazonaws.com/extract-word", data)
            .then((res) => console.log("success", res))
            .catch((err) => console.log("error", err));
    };
        const onData = (recordedBlob: any) => {
        }
        const onStop = (recordedBlob: any) => {
            const f = async () => {
                const blob = await fetch(recordedBlob.blobURL).then(r => r.blob())
                requestVoiceAnalyze(blob);
            }
            f()
        }
        const stopRecording = () => {
          setRecord(false)
        }
        const startRecording = () => {
        setRecord(true);
        setTimeout(stopRecording, 3000)
    }

  
    return (
        <>
            <ContentWrapper>
                <div className={classes.expSection}>
                    <Typography
                        variant="body2"
                        align="left"
                        className={classes.text}>
                        使い方<br/>
                        １相手が話始めたら録音開始<br/>
                        ２音声認識によって相手の発言に関連するキーワードが表示されます。<br/>
                    </Typography>
                </div>
                <div className={classes.expSection}>
                    <Typography
                        variant="body2"
                        align="left"
                        className={classes.text}>
                        <SearchIcon/>関連キーワード<br/>
                        お寿司<br/>
                        お寿司<br/>
                    </Typography>
                </div>
                <div className={classes.buttonSection}>
                    <Typography
                        variant="body1"
                        align="center"
                        className={classes.text}>
                        録音を開始
                    </Typography>
                    <IconButton className={classes.button} onClick={startRecording}>
                        <MicIcon className={classes.icon} />
                    </IconButton>
                </div>
                <ReactMic
                className={classes.mic}
                record={record}
                onStop={onStop}
                onData={onData}
                mimeType="audio/wav" />
            </ContentWrapper>
        </>
    )
};

export default RecordPage;
