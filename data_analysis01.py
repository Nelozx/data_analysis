import os

import matplotlib.pyplot as plt
import numpy as np

# 比较共享单车各用户类别的平均骑行时间趋势
# python3 -m pip install numpy 安装numpy
# 数据: https://video.mugglecode.com/data.zip

data_path = 'data/bikeshare'
data_filenames = ['2017-q1_trip_history_data.csv', '2017-q2_trip_history_data.csv',
                  '2017-q3_trip_history_data.csv', '2017-q4_trip_history_data.csv']


def collect_and_process_data():
    """
    setp 1+2: 数据收集,数据处理
    """
    cln_data_arr_list = []
    for data_filename in data_filenames:
        data_file = os.path.join(data_path, data_filename)
        # 加载文件，用','号分割，类型为字符串，忽略第一行
        data_arr = np.loadtxt(data_file, delimiter=',', dtype='str', skiprows=1)

        # 去掉双隐藏好
        cln_data_arr = np.core.defchararray.replace(data_arr, '"', '')
        cln_data_arr_list.append(cln_data_arr)

    return cln_data_arr_list


def get_mean_duration_by_byte(data_arr_list, member_type):
    """
    Step 3: 数据分析
    :param data_arr_list: 分析的数据
    :param member_type: member_type
    """
    mean_duration_list = []
    for data_arr in data_arr_list:
        # [:, -1] 所有行的最后一列
        bool_arr = data_arr[:, -1] == member_type
        filtered_arr = data_arr[bool_arr]

        mean_duration = np.mean(filtered_arr[:, 0].astype('float') / 1000 / 60)
        mean_duration_list.append(mean_duration)

    return mean_duration_list


def save_and_show_result(member_mean_duration_list, casual_mean_duration_list):
    """
    结果展示
    """
    # 信息输出
    for idx in range(len(member_mean_duration_list)):
        member_mean_duration = member_mean_duration_list[idx]
        casual_mean_duration = casual_mean_duration_list[idx]
        print('第{}个季度，会员平均骑行时长：{:.2f}分钟;非会员平均骑行时长：{:.2f}分钟'.format(idx + 1, member_mean_duration, casual_mean_duration))

    # 分析结果保存
    # 构造多维数组
    mean_duration_arr = np.array([member_mean_duration_list, casual_mean_duration_list])
    np.savetxt('./mean_duration_csv', mean_duration_arr, delimiter=',')

    # 可视化保存
    plt.plot(member_mean_duration_list, color='g', linestyle='-', marker='o', lable='Member')
    plt.plot(casual_mean_duration_list, color='r', linestyke='--', marker='*', lable='Casual')
    plt.title('Member vs Casual')
    plt.xlabel('Quarter')
    plt.ylabel('Mean duration (min)')
    plt.legend(loc='best')

    plt.savefig('./duration_trend.png')
    plt.show()


def main():
    """
    主函数
    """
    # 数据获取和数据处理
    cln_data_arr_list = collect_and_process_data()
    # 数据分析
    # 会员数据分析
    member_mean_duration_list = get_mean_duration_by_byte(cln_data_arr_list, 'Member')
    # 非会员数据分析
    casual_mean_duration_list = get_mean_duration_by_byte(cln_data_arr_list, 'Casual')

    # 保存和展示结果
    save_and_show_result(member_mean_duration_list, casual_mean_duration_list)


if __name__ == '__main__':
    main()
