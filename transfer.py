import os
from pprint import pprint
from google.cloud import storage

# Either this 
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'pipeline-dataflow-1309f9e8ff56.json'

# or this 
storage_client = storage.Client.from_service_account_json('pipeline-dataflow-1309f9e8ff56.json') # Create your own service account key.

# To check the existing bucket --> 
pprint([bucket for bucket in storage_client.list_buckets()])

# create a new bucket

# bucket = storage_client.bucket(bucket_name)
# bucket.storage_class = 'STANDARD' # Archive | Nearline | Standard
# bucket.location = 'asia'
# bucket = storage_client.create_bucket(bucket) # returns Bucket object

# Using Existing Bucket

bucket_coe_test = storage_client.get_bucket("bucket_coe_test")
print(bucket_coe_test)


# Transfering to Google cloud storage
def individual_upload(blob_name, file_path, bucket_name):
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_path)
    return blob
    print("Successfully uploaded")

individual_upload("FileA",r"C:\Users\Piyush.Dhasmana\Desktop\GCP COE\A-file1.txt","bucket_coe_test")

# Upload file and make a directory in the GCS
# individual_upload("Support_folder1/FileA",r"C:\Users\Piyush.Dhasmana\Desktop\GCP COE\A-file1.txt","bucket_coe_test")


# To upload N no. of files 
def mul_upload(blob_name,folder_path, bucket_name):
    bucket = storage_client.get_bucket(bucket_name)
    for filename in os.listdir(folder_path):  #Human, Object 
        blob = bucket.blob(blob_name+ "" + filename+"/")
        blob.upload_from_filename(folder_path+"\\"+filename)
        return blob
    
    
# mul_upload("Support_folder",r"C:\Users\Piyush.Dhasmana\Desktop\GCP COE\Images","bucket_coe_test")


individual_upload("Support_folder1/Software",r"C:\Users\Piyush.Dhasmana\Desktop\GCP COE\Sample_file.csv","bucket_coe_test")
