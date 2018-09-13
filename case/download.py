import requests

if __name__ == '__main__':
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/67.0.3396.99 Safari/537.36'}
    url = 'http://www.apache.org/dist/zookeeper/current/zookeeper-3.4.12.tar.gz'
    print('now downloading...')
    remote_file = requests.get(url, headers=headers)
    # print(len(remote_file))
    print(remote_file)
    local_path = '../data/'
    local_file = 'zookeeper-3.4.12.tar.gz'
    with open(local_path + local_file, 'wb') as f:
        f.write(remote_file.content)

