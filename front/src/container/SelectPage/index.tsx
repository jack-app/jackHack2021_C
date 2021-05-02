import React, {useEffect, useCallback, useState, memo } from 'react';
import { useHistory, useLocation, Link } from "react-router-dom";
import ContentWrapper from "components/atoms/ContentWrapper";
import { Typography, Grid, Button, makeStyles } from '@material-ui/core';
import {usePostUser} from "hooks/useUser";
import { Content } from 'antd/lib/layout/layout';
const useStyles = makeStyles((theme) => ({
  button: {
      height: "80px"
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
    },[loading])
    return (
        <>
            <ContentWrapper>
                { !!userName && (
                    <p>ようこそ、{userName}さん</p>
                )}
                <Grid container spacing={2} alignItems="center">
                    <Grid item xs={6}>
                        <Button color="primary" variant="contained" size="large" className={classes.button}>
                            話題＆質問<br/>
                            テンプレート
                        </Button>
                    </Grid>
                    <Grid item xs={6}>
                        <p>
                            話題別に<br/>盛り上がりやすい<br/>質問を厳選しました
                        </p>
                    </Grid>
                </Grid>
                <Grid container spacing={2} alignItems="center">
                    <Grid item xs={6}>
                        <Button color="secondary" variant="contained" size="large" className={classes.button}>
                            相手の話で<br/>
                            盛り上がろう
                        </Button>
                    </Grid>
                    <Grid item xs={6}>
                        <p>
                            相手の話を音声認識してキーワードを抽出<br/>
                            関連する話題を提供します
                        </p>
                    </Grid>
                </Grid>
                <Grid container spacing={2} alignItems="center">
                    <Grid item xs={6}>
                        <Button variant="outlined" color="primary" size="large" className={classes.button}>
                            自分の話で<br/>
                            もりあがろう
                        </Button>
                    </Grid>
                    <Grid item xs={6}>
                        <p>
                            話題別に盛り上がりやすい質問を厳選しました
                        </p>
                    </Grid>
                </Grid>
            </ContentWrapper>
        </>
    )
})

export default SelectPage