import React, { memo } from 'react';
import { Typography, Button, Grid, Modal, makeStyles } from "@material-ui/core";
import { Link, useHistory } from "react-router-dom";
import ContentWrapper from "components/atoms/ContentWrapper";
import useGetTemplate from "hooks/useGetTemplate";
import { Content } from 'antd/lib/layout/layout';
const useStyles = makeStyles((theme) => ({
  button: {
      borderRadius: "",
      backgroundColor: ""
  },
  text: {
      color: ""
  },
  expSection: {
      margin: "px 0"
  },
  buttonSection: {
      margin: "px 0"
  }
}));
const TempleteStuPage = React.memo(() => {
    const history = useHistory();
    const classes = useStyles();
    const sample = ["a", "b", "c", "d", "e", "f", "g"]
    return (
        <ContentWrapper>
            <Typography>
                話題を選んでください
            </Typography>
            <Grid container spacing={2} alignItems="center">
                {sample.map((v) => (
                    <Grid item xs={6}>
                        <Button>
                            {v}
                        </Button>
                    </Grid>
                ))}
            </Grid>
        </ContentWrapper>
    )
})
export default TempleteStuPage;