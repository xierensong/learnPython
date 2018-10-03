# encoding=utf-8

from pathlib import Path
import requests
import csv
import sys

if __name__ == '__main__':
    current_path = Path('.')
    attachment_file = current_path / '..' / 'data' / 'FRAttachment_hbase.csv'
    project_name = attachment_file.stem.split('_')[-1]
    project_path = current_path / '..' / 'data' / project_name
    project_path.mkdir(exist_ok=True)
    with open(str(attachment_file), 'r', encoding='utf-8', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in enumerate(reader):
            print('FRName', row[1]['FRName'])
            FR_name = row[1]['FRName']
            print('AttachmentURL', row[1]['AttachmentURL'])
            Attachment_URL = row[1]['AttachmentURL']
            Attachment_name = Attachment_URL.split('/')[-1]
            FR_path = project_path / FR_name
            FR_path.mkdir(exist_ok=True)
            attachment_file = FR_path / Attachment_name
            if attachment_file.exists():
                print(attachment_file, 'is exist, skip')
                continue
            headers = {
                "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/67.0.3396.99 Safari/537.36'}
            print('now downloading...')
            try:
                remote_file = requests.get(Attachment_URL, headers=headers)
                # print(len(remote_file))
                print(remote_file)

                with open(str(attachment_file), 'w', encoding='utf-8', newline='') as attachment_file:
                    attachment_file.write(remote_file.text)
                    print(attachment_file, 'write successfully!')
            except:
                print("Unexpected error", sys.exc_info()[0])
                if attachment_file.exists():
                    print(attachment_file, 'download failed, delete it.')
                    attachment_file.unlink()
