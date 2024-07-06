import boto3
from datetime import datetime, timedelta

# 엔드포인트 설정
dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
table = dynamodb.Table("Document")

# 데이터 생성 및 삽입
current_time = datetime.now()
for i in range(1, 101):
    item = {
        "id": str(i),
        "title": f"My Document Title {i}",
        "summary": f"Brief summary of the document {i}",
        "detail": f"Detailed description of the document {i}",
        "status": "INSERTED",
        "created_at": (current_time - timedelta(days=i)).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "updated_at": (current_time - timedelta(days=i)).strftime("%Y-%m-%dT%H:%M:%SZ")
    }
    table.put_item(Item=item)
