#code=utf-8
import os
from pathlib import Path
import shutil

os.chdir('/home/ubuntu/code/CodeRecommend/FR_Benchmark/entity/mahout/source_code')
path_name = Path('/home/ubuntu/code/CodeRecommend/FR_Benchmark/entity/mahout/source_code/mahout-distribution-0.6-src.tar.gz')
print('suffix', path_name.suffix)
shutil.unpack_archive(str(path_name))
print('ok')