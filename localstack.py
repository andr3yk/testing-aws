import boto3

# Connect to S3 localstack and create a test-bucket
s3_client = boto3.client("s3", endpoint_url="http://localhost:4572")
s3_response = s3_client.create_bucket(Bucket="test-bucket")

# Connect to Kinesis localstack and create a test-stream
kinesis_client = boto3.client("kinesis", endpoint_url="http://localhost:4568", region_name='localstack')
kinesis_response = kinesis_client.create_stream(
    StreamName='test-stream',
    ShardCount=5
)
