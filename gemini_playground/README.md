# gemini_playground

[Google AI Gemini API](https://ai.google.dev/gemini-api) 를 이용하여 간단한 챗봇 작성

## Setting

### Get Gemini API

[Get API Key](https://aistudio.google.com/app/apikey) 에서 API 키를 만들기

#### Setting Environmental Variables

```shell
cp ./envs/.dev.env.sample ./envs/.dev.env
```

위에서 만든 API 키를 `./envs/.dev.env` 의 `GOOGLE_API_KEY` 에 입력

### Building a Development Environment

Poetry를 이용하여 개발 환경 구축
Poetry의 설치에 관해서는 [poetry 사용법 메모](https://idenrai.tistory.com/289) 참조

```shell
poetry install
```

```shell
poetry shell
```

## Chatbot

Streamlit을 이용하여 간단한 Chatbot을 구현

```shell
streamlit run main.py
```

## Sample Scripts

간단한 파이썬 코드로 API 키가 동작하는 것을 확인

### Run

```shell
python chat_sample.py --env=dev
```
