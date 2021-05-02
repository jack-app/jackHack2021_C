import React, { memo } from 'react'
import { Typography, Input, Row, Col } from "antd";
import styled from "styled-components";
import ContentWrapper from "components/atoms/ContentWrapper";
const { Title, Text } = Typography;
const MainTitle = styled(Title)`
    margin: 100px 0;
`;
const TextWrapper = styled.div`
    margin 40px 0;
`;
const ExpText = styled(Text)`
`;
const NameInput = styled(Input)`
`;
export default memo(function index() {
    return (
        <ContentWrapper>
            <MainTitle level={1}>
                タイトルタイトル
            </MainTitle>
            <TextWrapper>
                <ExpText>
                    コミュ症陰キャの皆さん初対面の人と話す時にこんな悩みごとを抱えていませんか？
                </ExpText>
            </TextWrapper>
            <TextWrapper>
                <ExpText>
                    話題が広がらない、、、<br/>
                    いまいち盛り上がれない、、、<br/>
                </ExpText>
            </TextWrapper>
            <TextWrapper>
                <ExpText>
                    タイトルはそんな陰キャたちが会話を弾ませるのに役立つ便利ツールです。
                    これを使えば君もコミュ強陽キャになれること間違いなし！
                </ExpText>
            </TextWrapper>
            <NameInput />
        </ContentWrapper>
    )
})
