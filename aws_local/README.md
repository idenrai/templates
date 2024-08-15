# Terraform for local aws

## 개요

[LocalStack](https://docs.localstack.cloud/overview/) 을 이용한 로컬 AWS 를 Terraform 으로 다루기

## 상세

### 준비

#### Docker

Docker Desktop 설치

<https://docs.docker.com/desktop/install/mac-install/>

#### AWS

AWS-CLI 설치

<https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html>

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

#### LocalStack

<https://docs.localstack.cloud/getting-started/installation/>

내 경우는 `brew` 를 통해 설치

```shell
brew install localstack/tap/localstack-cli
```

설치 확인

```shell
localstack --version
```

기동

```shell
localstack start -d
```

동작 확인

```shell
localstack status services
```

Web Application 에서도 확인 가능

<https://app.localstack.cloud/>

#### Terraform

[tfenv](https://github.com/tfutils/tfenv) 설치

```shell
brew install tfenv
```

Terraform install

```shell
tfenv install 1.9.3
```

```shell
tfenv use 1.9.3
```

#### tflocal

[tflocal](https://github.com/localstack/terraform-local) 설치

```shell
pip install terraform-local
```
