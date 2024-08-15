# templates

개발시 자주 사용할 법 한 최소한의 내용을 템플릿으로 만들어 보았다.

- dbt_duckdb_local
  - dbt project 를 손쉽게 검증할 수 있도록 duckdb 를 이용한 로컬 개발 환경을 구축
- dynamodb_local
  - DynamoDB 를 로컬 환경에서 구동할 수 있도록 최소한의 설정을 준비
- python_script
  - 데이터 입출력 등의 간단한 처리를 위한 Python script 를 작성함에 있어, 최소한의 설정을 준비

## TBD

만들어 두고 싶은 내용

- aws_local
  - localstack + terraform-local을 이용한 로컬 테라폼 검증 환경 구축
- streamlit_chatbot
  - streamlit으로 간단하게 챗봇 PoC가 가능하도록 준비
  - openai & gemini api 가 사용 가능하도록 할 것
