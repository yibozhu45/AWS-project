import speech_recognition as sr
import os
import boto3
import sys
import uuid
from urllib.parse import unquote_plus

s3_client = boto3.client('s3')

def audio_to_text(audio_path,saved_path):
    r = sr.Recognizer()
    with sr.AudioFile(audio_path) as source:
        audio = r.record(source)
    with open(os.path.join(saved_path, "audio2text.txt"), "a") as file1:
        file1.write(r.recognize_google(audio))
        file1.close()

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        print(bucket)
        key = unquote_plus(record['s3']['object']['key'])
        print(key)
        tmpkey = key.replace('/', '')
        print(tmpkey)
        download_path = '/tmp/{}{}'.format(uuid.uuid4(), tmpkey)
        print(download_path)
        upload_path = '/tmp/'
        print(upload_path)
        s3_client.download_file(bucket, key, download_path)
        audio_to_text(download_path, upload_path)
        s3_client.upload_file(upload_path + 'audio2text.txt', '{}-resized'.format(bucket), 'audio2text.txt')

