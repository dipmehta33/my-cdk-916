import aws_cdk as cdk
import aws_cdk.aws_s3 as s3
from constructs import Construct

class MyCdk916Stack(cdk.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        #All constructs take three parameters when they are intialized
        # You define a construct by instantiating the class.  scope -> Usually using this ,  id -> identifer, namespace, unique, resource names, AWS Cloud Formation logical ids , props -> 
        bucket = s3.Bucket(self, "myBucketId", bucket_name="anikabucket9151255", versioned=True, encryption=s3.BucketEncryption.KMS_MANAGED)
        

       