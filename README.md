jackhack2021 のチーム C のリポジトリです

## backend

dev-server: jackhack-2021-backend-dev-811780550.ap-northeast-1.elb.amazonaws.com

### API 仕様

https://github.com/jack-app/jackHack2021_C/issues/1#issuecomment-830605733

### mock server

JSON server を利用

- https://github.com/typicode/json-server
- https://www.cyokodog.net/blog/use-well-json-server/
- https://www.to-r.net/media/json-server/

```
$ cd front/mock
$ node server.js
```

### セットアップ

```

$ cd backend

// 任意. 好きに仮想環境作ってください
$ python -m pyenv jackhack2021_env
$ source jackhack2021_env/bin/activate

$ pip install -r requirement.txt

```

### サーバー起動方法

```

$ python app.py

```
