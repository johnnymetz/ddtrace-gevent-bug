from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class FileStorage(S3Boto3Storage):
    bucket_name = settings.S3_BUCKET_NAME
    # location = "media"
    # default_acl = "public-read"
    # file_overwrite = True
    # custom_domain = False
    # querystring_expire = None
    # querystring_auth = False
