import boto3

# 엔드포인트 설정
dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

table = dynamodb.Table("Document")
table.delete()

# 테이블 생성
table = dynamodb.create_table(
  TableName="Document",
  KeySchema=[
    {"AttributeName": "id", "KeyType": "HASH"}
  ],
  AttributeDefinitions=[
    {"AttributeName": "id", "AttributeType": "S"}
  ],
  ProvisionedThroughput={
    "ReadCapacityUnits": 5,
    "WriteCapacityUnits": 5
  }
)
