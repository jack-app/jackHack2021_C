import React, { memo } from 'react';
import ContentWrapper from "components/atoms/ContentWrapper";
import { Typography, Grid, Button, makeStyles} from "@material-ui/core";
import SearchIcon from '@material-ui/icons/Search';
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
                        <br/>
                        <br/>
                    </Typography>
                </div>
                <div className={classes.expSection}>
                    <Typography
                        variant="body2"
                        align="left"
                        className={classes.text}>
                        <SearchIcon/><br/>
                        <br/>
                        <br/>
                    </Typography>
                </div>
                <div className={classes.buttonSection}>
                    <Typography
                        variant="body1"
                        align="center"
                        className={classes.text}>
    
                    </Typography>
                    <Button className={classes.button}>
    
                    </Button>
                </div>
            </ContentWrapper>
        </>
    )
};

export default RecordPage;
