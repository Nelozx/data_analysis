"""
统计不同用户骑行时间的直方图
"""
import os

# 数据路径
data_path = 'data/bikeshare'
data_filenames = ['2017-q1_trip_history_data.csv', '2017-q2_trip_history_data.csv',
                  '2017-q3_trip_history_data.csv', '2017-q4_trip_history_data.csv']
# 结果保存路径
output_path = 'data/bikeshare/output'

# 如果不存在就新建一个
if not os.path.exists(output_path):
    os.makedirs(output_path)


# 数据获取和数据处理
def collect_and_process_data():
    pass


def analyze_data():  # 数据分析
    pass


def save_and_show_results():  # 数据保存和展示
    pass


def main():
    collect_and_process_data()
    analyze_data()
    save_and_show_results()


if __name__ == '__main__':
    main()
