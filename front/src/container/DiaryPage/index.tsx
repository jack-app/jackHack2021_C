import React, { useState, useEffect, useCallback, memo } from 'react'
import { Typography, Grid, IconButton, Card, CardContent, makeStyles } from "@material-ui/core";
import AddIcon from '@material-ui/icons/Add';
import useGetDiary, { usePostDiary } from "hooks/useDiary";
import { Link, useHistory, useLocation } from "react-router-dom";
import ContentWrapper from "components/atoms/ContentWrapper";

const useStyles = makeStyles((theme) => ({
  card: {
    margin: "30px 0"
  },
  cardTitle: {
    textAlign: "left"
  },
  title: {
    fontWeight: "bold",
    margin: "40px 0"
  },
  icon: {
      color: "#21C49C"
  }
}));
const DiaryPage: React.FC = () => {
    const classes = useStyles();

    const location = useLocation();
    const uuid = unescape(location.search.split("=")[1]);
    const diary = useGetDiary()
    return (
        <ContentWrapper>
            <Typography variant="h5" className={classes.title}>
                コミュ力UPのための日記
            </Typography>
            {diary && diary.map((v:any)=> (
                <Card className={classes.card} key={v.id}>
                    <CardContent>
                        <Typography className={classes.cardTitle} color="textSecondary" gutterBottom>
                        {v.title}
                        </Typography>
                        
                        <Typography variant="body2" component="p">
                        {v.content}
                        <br />
                        </Typography>
                    </CardContent>
                </Card>
            ))}
        <IconButton className={classes.icon}>
            <AddIcon/>
        </IconButton>
        </ContentWrapper>
    )
}

export default DiaryPage;
