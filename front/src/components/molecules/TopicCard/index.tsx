import React, { memo } from 'react'
import {Button} from "antd";
import styled from "styled-components";

const TopicButton = styled(Button)`
    width: 100%;
    min-width: 90px;
    max-width: 120px;
    text-align: center;
`;
export default memo(function index(topic: string) {
    return (
        <TopicButton>
            topic
        </TopicButton>
    )
})
