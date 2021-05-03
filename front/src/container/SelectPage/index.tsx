import React, {useEffect, useCallback, useState, memo } from 'react';
import { useHistory, useLocation, Link } from "react-router-dom";
import ContentWrapper from "components/atoms/ContentWrapper";
import { Typography, Grid, Button, makeStyles } from '@material-ui/core';
import {usePostUser} from "hooks/useUser";

const useStyles = makeStyles((theme) => ({
  button: {
      height: "80px"
  },
  link: {
      textDecoration: "none"
  },
  grid: {
      margin: "30px 0"
  }
}));
const SelectPage = React.memo(() => {
    const history = useHistory();
    const classes = useStyles();
    const [userName, setUserName] = useState<string | null>(null);
    const [userUuid, setUserUuid] = useState<string | null>(null);
    const location = useLocation();
    const name = unescape(location.search.split("=")[1]);
    const {userid, loading} = usePostUser(name);
    console.log("call")
    useEffect(() => {
        setUserName(name);
        setUserUuid(userid);
        return;
    },[loading])
    return (
        <>
            <ContentWrapper>
                { !!userName && (
                    <p>ようこそ、{userName}さん</p>
                )}
                <Grid container spacing={2} alignItems="center" className={classes.grid}>
                    <Grid item xs={6}>
                        <Link to="/template" className={classes.link}>
                            <Button color="primary" variant="contained" size="large" className={classes.button}>
                                話題＆質問<br/>
                                テンプレート
                            </Button>
                        </Link>
                    </Grid>
                    <Grid item xs={6}>
                        <Typography variant="body2" align="left" color="primary">
                            話題別に<br/>盛り上がりやすい<br/>質問を厳選しました
                        </Typography>
                    </Grid>
                </Grid>
                <Grid container spacing={2} alignItems="center" className={classes.grid}>
                    <Grid item xs={6}>
                        <Link to="/record_sound" className={classes.link}>
                            <Button color="secondary" variant="contained" size="large" className={classes.button}>
                                相手の話で<br/>
                                盛り上がろう
                            </Button>
                        </Link>
                    </Grid>
                    <Grid item xs={6}>
                        <Typography variant="body2" align="left" color="secondary">
                            相手の話を音声認識してキーワードを抽出<br/>
                            関連する話題を提供します
                        </Typography>
                    </Grid>
                </Grid>
                <Grid container spacing={2} alignItems="center" className={classes.grid}>
                    <Grid item xs={6}>
                        <Link to="/diary" className={classes.link}>
                            <Button variant="outlined" color="primary" size="large" className={classes.button}>
                                自分の話で<br/>
                                もりあがろう
                            </Button>
                        </Link>
                    </Grid>
                    <Grid item xs={6}>
                        <Typography variant="body2" align="left" color="primary">
                            話題別に盛り上がりやすい質問を厳選しました
                        </Typography>
                    </Grid>
                </Grid>
            </ContentWrapper>
        </>
    )
})

export default SelectPage