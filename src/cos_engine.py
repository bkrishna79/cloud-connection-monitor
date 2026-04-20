import boto3
from botocore.config import Config
from concurrent.futures import ThreadPoolExecutor
import time
import logging
import threading
import yaml

with open("configs/cos_config.yaml") as f:
    cfg = yaml.safe_load(f)

config = Config(
    retries={'max_attempts': 5},
    tcp_keepalive=True,
    max_pool_connections=cfg["connections"]
)

s3 = boto3.client(
    "s3",
    endpoint_url=cfg["endpoint"],
    aws_access_key_id=cfg["access_key"],
    aws_secret_access_key=cfg["secret_key"],
    config=config
)

def worker():
    while True:
        try:
            r = s3.get_object(Bucket=cfg["bucket"], Key=cfg["object_key"])
            r['Body'].read(1024)
            print("OK")
        except Exception as e:
            print("ERR", e)
        time.sleep(cfg["sleep"])

with ThreadPoolExecutor(max_workers=cfg["connections"]) as exe:
    for _ in range(cfg["connections"]):
        exe.submit(worker)
