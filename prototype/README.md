# prototype

[Streamlit](https://streamlit.io/) 과 [Flask](https://flask.palletsprojects.com/en/3.0.x/) 를 이용한 프로토타입 개발 및 [ngrok](https://ngrok.com/) 를 통한 외부 공개

## Setting

Poetry를 이용하여 개발 환경 구축

```shell
poetry install
```

```shell
poetry shell
```

### duckdb

[https://duckdb.org/#quickinstall](https://duckdb.org/#quickinstall)

```shell
brew install duckdb
```

#### Create DB

아래의 커맨드로 간단히 DB 작성 가능

```shell
duckdb [DB 명].db
```

예시)

```shell
duckdb prototype.db
```

#### DuckDB GUI Client

아래의 GUI 클라이언트를 사용할 수도 있음

[DB Pilot](https://www.dbpilot.io/duckdb)

이용 방법에 관해선 [블로그](https://idenrai.tistory.com/296) 참조

flask 기동중에는 사용 불가

### ngrok

#### 유저 등록

[ngrok 공식 사이트](https://dashboard.ngrok.com/signup) 유저 등록

MFA 라던가 복구 코드라던가 해야 할 세팅이 좀 있음

#### DL

```shell
brew install ngrok/ngrok/ngrok
```

#### Config

```shell
ngrok config add-authtoken $YOUR_AUTHTOKEN
```

## Run

### Flask

```shell
FLASK_APP=server FLASK_DEBUG=true flask run
```

### Streamlit

```shell
streamlit run main.py
```

### ngrok를 통한 글로벌 공개

```shell
ngrok http http://localhost:8501
```

상기 설정을 통해 포워딩해주는 Website URL로 접속
