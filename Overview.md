- https://jbrojbrojbro.medium.com/5-ish-ways-to-get-your-data-into-cloud-storage-1ae628992e78
- https://medium.com/google-cloud/using-google-cloud-storage-5b9d3f570945
- https://learndataanalysis.org/source-code-using-google-cloud-storage-api-in-python-for-beginners/

Step 1 : Enable all the cloud storage api : Json and cloud storage

Step 2 : Create a Service account that will be associated with the cloud storage

Step 3 : Open that service account and then create a key from key section, in json format for the service account and download the key and then set credentials.

Step 4 : Transfer.py <--- Referenced file for the code along with the explanation



GSUTIL
- https://www.youtube.com/watch?v=kdRuDaDyyBo
- https://stackoverflow.com/questions/47043441/what-should-i-do-about-this-gsutil-parallel-composite-upload-warning
- https://cloud.google.com/storage/docs/parallel-composite-uploads
- https://cloud.google.com/storage/docs/gsutil/addlhelp/GlobalCommandLineOptions <<-- for all the command line flags for the gustil
- https://cloud.google.com/blog/products/gcp/optimizing-your-cloud-storage-performance-google-cloud-performance-atlas <<-- for -m and 150M performance optimization 

**If you have a large number of files to transfer, you can perform a parallel multi-threaded/multi-processing copy using the top-level gsutil -m option :** 

gsutil -m cp -r dir gs://my-bucket #

**for Bigger files use the below command, here 150M means it is dividing the file (lets say 2GB) into 150MB chunks and then uploading it to GCS**

gsutil -o GSUtil:parallel_composite_upload_threshold=150M cp <FILENAME> gs://your-bucket
