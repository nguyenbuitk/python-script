# In this chapter, we will doing following tasks
1. Create sample lambda function
2. Change performance, Memory, CPU of lambda function
3. Managing lambda version
4. Managing alias
5. Create deployment package and send slack notification
6. Using layers of lambda
7. Passing env to lambda function
8. Encrypt sensitive data of lambda env
9. Find unused volume of ec2 and send email
10. When json file uploaded to s3, automatically process and input file to dynamoDB
11. Read CSV from S3 and persist to dynamoDB
12. AWS Lambda - Run EC2 instances In Schedule
13. Remove Unused AMIs
14. AWS Lambda, send email notification when EC2 stopped
# Notes 
## For using lambda, you can zip below file and upload to lambda function
Notes:
    lambda don't have package likes "requests", so to use it, you need to compress all module and python scripts and push it to lambda. Or you can compress module and push it as layer on lambda