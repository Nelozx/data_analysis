
import os
import numpy as np

# python3 -m pip install numpy 安装numpy
# 数据: https://video.mugglecode.com/data.zip

data_path = 'data/bikeshare'
data_filenames = ['1.csv', '2.csv', '3.csv']


def collect_data():
    """
    setp 1: 数据收集
    """
    data_arr_list = []
    for data_filename in data_filenames:
        data_file = os.path.join(data_path, data_filename)
        data_arr = np.loadtxt()

def main():
    collect_data()
    pass

main()