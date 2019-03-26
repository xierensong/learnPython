from pathlib import Path

if __name__ == '__main__':
    p = Path('..')
    print(p)
    print([x for x in p.iterdir() if x.is_dir()])

    # assign file with path, not exist
    q = Path('../data/tmp')
    if q.exists() == 0:
        # not exist case
        print(q.name, 'is not exist!')

        # create empty file
        q.touch()
        print(q.name, q.stat().st_size)

        # write text into file
        q.write_text('werwqer')
        print(q.name, q.stat().st_size)

    else:
        # exist case
        print(q.name, 'is exist, delete it first!')
        if q.stat().st_size == 0:
            # file size 0
            # 删除文件
            q.unlink();
        else:
            print(q.read_text())
            q.unlink();
    # 遍历文件
    dir_path = Path('.')
    for file in dir_path.glob('*.*'):
        print('file name', file)
        print('name ', file.stem)   # 不带扩展名的文件名
        print('suffix ', file.suffix)   # 扩展名
        print('parent dir', file.parts[-2]) # 上一级父目录


