INSERT INTO user (name) VALUES ('Bob');
INSERT INTO user (name) VALUES ('Tom');
INSERT INTO user (name) VALUES ('Nancy');

INSERT INTO situation_type (name) VALUES ('初対面の学生');
INSERT INTO situation_type (name) VALUES ('初対面の先輩');
INSERT INTO situation_type (name) VALUES ('初対面の社会人');

INSERT INTO topic (name, situation_type_id) VALUES ('部活・サークル', 1);
INSERT INTO topic (name, situation_type_id) VALUES ('バイト', 2);
INSERT INTO topic (name, situation_type_id) VALUES ('社会人', 3);

INSERT INTO question (content, topic_id, situation_type_id) VALUES ('部活はなんですか？', 1, 1);
INSERT INTO question (content, topic_id, situation_type_id) VALUES ('時給はいくらですか？', 2, 2);
INSERT INTO question (content, topic_id, situation_type_id) VALUES ('ご趣味は？', 3, 1);

INSERT INTO diary (title, content, user_id) VALUES ('日記１', 'ハッカソンたのちぃぃぃ！', 1);
INSERT INTO diary (title, content, user_id) VALUES ('日記２', 'ハッカソンたのちぃぃぃ！', 1);
INSERT INTO diary (title, content, user_id) VALUES ('日記３', 'ハッカソンたのちぃぃぃ！', 1);
