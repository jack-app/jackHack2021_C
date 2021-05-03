import React, { memo } from 'react';
import ContentWrapper from "components/atoms/ContentWrapper";
import { Typography, Grid, IconButton, makeStyles} from "@material-ui/core";
import SearchIcon from '@material-ui/icons/Search';
import MicIcon from '@material-ui/icons/Mic';
const useStyles = makeStyles((theme) => ({
  button: {
  width:"150px",
  height:"150px",
      borderRadius: "",
      backgroundColor:"red"
  },
  text: {
      fontSize:"20px",
      color: ""
  },
  expSection: {
      margin: "90px 0"
  },
  buttonSection: {
      margin: "100px 0"
  }
}));

const RecordPage: React.FC = () => {
    const classes = useStyles();
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
                    <IconButton className={classes.button}>
                      <MicIcon/>
                    </IconButton>
                </div>
            </ContentWrapper>
        </>
    )
};

export default RecordPage;
