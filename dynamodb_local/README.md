# DynamoDB Local

DynamoDB 를 로컬 환경에서 구동할 수 있도록 최소한의 설정을 준비

<https://hub.docker.com/r/amazon/dynamodb-local>

<https://hub.docker.com/r/aaronshaf/dynamodb-admin>

## 준비물

### Docker

Docker Desktop 설치

<https://docs.docker.com/desktop/install/mac-install/>

### AWS

AWS-CLI 설치

<https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html>

#### boto3

```shell
pip install boto3
```

<https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html>

#### Configure

원활한 이용을 위해 AWS Credentials 설정이 필요

```shell
aws configure
```

아래와 같이 설정

```text
$ aws configure
AWS Access Key ID [None]: dummy
AWS Secret Access Key [None]: dummy
Default region name [None]: ap-northeast-1
Default output format [None]: json
```

수동 설정의 경우는 아래와 같음

```shell
touch ~/.aws/credentials
vi ~/.aws/credentials
```

```text
[default]
aws_access_key_id = dummy
aws_secret_access_key = dummy
```

```shell
touch ~/.aws/config
vi ~/.aws/config
```

```test
[default]
region = ap-northeast-1
output = json
```

## Run

```shell
docker-compose up
```

### Test

```shell
aws dynamodb list-tables --endpoint-url http://localhost:8000
```

아래와 같이 출력되면 OK

```text
$ aws dynamodb list-tables --endpoint-url http://localhost:8000
{
    "TableNames": []
}
```

### GUI

8000 에서 DynamoDB 를, 8001 에서 GUI 를 기동하므로, GUI 에서도 확인 가능

<http://localhost:8001/>
