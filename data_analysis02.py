"""
比较全年共享单车用户类别（会员&非会员）的比例
"""
import os

import matplotlib.pyplot as plt
import numpy as np

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
    member_type_list = []
    for data_filename in data_filenames:
        data_file = os.path.join(data_path, data_filename)
        print(data_file)
        # 读数据默认读取是浮点数， 但这个csv数据类型，各种还有年月日的，保险起见都用字符串类型
        data_arr = np.loadtxt(data_file, delimiter=',', dtype='str', skiprows=1)  # 读进来的数据
        member_type_col = np.core.defchararray.replace(data_arr[:, -1], '"', '')  # 获取最后一列并去掉双引号,
        # 默认一位数据以行向量存储，想变成列向量就用reshape，不知道要多少行没事，该维度加上-1，python自动帮你算
        member_type_col = member_type_col.reshape(-1, 1)
        member_type_list.append(member_type_col)
    year_member_type = np.concatenate(member_type_list)
    return year_member_type


def analyze_data(year_member_type):  # 数据分析
    n_member = year_member_type[year_member_type == 'Member'].shape[0]  # 会员行数
    n_casual = year_member_type[year_member_type == 'Casual'].shape[0]  # 非会员行数
    return [n_member, n_casual]


def save_and_show_results(n_users):  # 数据保存和展示
    plt.figure()
    plt.pie(
        n_users,  # 哪个变量要画饼
        labels=['Member', 'Casual'],  # 变量的标签
        autopct='%.2f%%',  # 显示数目百分比
        shadow=True,  # 阴影饼状图
        explode=[0, 0.05],  # 使各个扇形彼此分离，列表内的值是距离圆心的offset
    )
    plt.axis('equal')  # 保证是个圆饼，不是扁饼，因为默认是扁的
    plt.tight_layout()
    plt.savefig(os.path.join(output_path, 'piechart.png'))
    plt.show()


def main():
    year_member_type = collect_and_process_data()
    n_users = analyze_data(year_member_type)
    save_and_show_results(n_users)


if __name__ == '__main__':
    main()
