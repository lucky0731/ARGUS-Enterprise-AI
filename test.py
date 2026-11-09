import boto3
import json

client = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)

response = client.invoke_model(
    modelId="amazon.nova-lite-v1:0",
    contentType="application/json",
    accept="application/json",
    body=json.dumps({
        "messages": [
            {
                "role": "user",
                "content": [
                    {"text": "Explain Python in one sentence"}
                ]
            }
        ],
        "inferenceConfig": {
            "maxTokens": 300,
            "temperature": 0.7
        }
    })
)

result = json.loads(response["body"].read())
print(result)