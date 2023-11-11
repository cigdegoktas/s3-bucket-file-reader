import boto3 as bt

def list_all_files_from_s3_directory(bucket_name, directory_name, url, access_id, access_key):
    # Initialize a boto3 S3 client
    s3_client = bt.resource('s3',
                           endpoint_url = url,
                           aws_access_key_id = access_id,
                           aws_secret_access_key = access_key,
                           verify = False)
    
    bucket = s3_client.Bucket(bucket_name)

    # Return the list of files from the specified directory in the bucket
    return [file.key.split(directory_name+"/")[1] for file in bucket.objects.filter(Prefix = directory_name)]

# Example usage
list_all_files_from_s3_directory('your-bucket-name', 'your-directory-name', 'your-url', 'your-access-id', 'your-access-key')