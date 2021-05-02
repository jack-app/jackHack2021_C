import React, {useEffect, useCallback, useState, memo } from 'react'
import { Typography, Input, Form, Button, Row, Col } from "antd";
import styled from "styled-components";
import ContentWrapper from "components/atoms/ContentWrapper";
import { usePostUser } from "hooks/useUser"; 
import { Link, useHistory } from "react-router-dom";

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
const TopPage = React.memo(() => {
    const history = useHistory();
    const onFinish = useCallback((values) => {
        console.log(values)
        const { username } = values;
        history.push(`/user?name=${escape(username)}`)
    },[])
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
            <Form onFinish={onFinish}>
                <Form.Item 
                    label="username"
                    name="username"
                    rules={[{required: true, message: "名前を登録してください"}]}
                >
                    <Input/>
                </Form.Item>
                <Form.Item>
                    <Button type="primary" htmlType="submit">
                        登録
                    </Button>
                </Form.Item>
            </Form>
        </ContentWrapper>
    )
})

export default TopPage;