import os

import matplotlib.pyplot as plt
import numpy as np
# 比较共享单车各用户类别的平均骑行时间趋势
# python3 -m pip install numpy 安装numpy
# 数据: https://video.mugglecode.com/data.zip
from numpy.core._multiarray_umath import ndarray

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
    :param data_arr_list: data_arr_list
    :param member_type: member_type
    """
    mean_duration_list = []
    for data_arr in data_arr_list:
        # [:, -1] 所有行的最后一列
        bool_arr = (data_arr[:, -1] == member_type)

        filtered_arr = data_arr[bool_arr]
        # 时间（分钟）
        mean_duration = np.mean(filtered_arr[:, 0].astype('float') / 1000 / 60)
        mean_duration_list.append(mean_duration)
    return mean_duration_list


def save_and_show_results(member_mean_duration_list, casual_mean_duration_list):
    # 信息输出
    for idx in range(len(member_mean_duration_list)):
        member_mean_duration = member_mean_duration_list[idx]
        casual_mean_duration = casual_mean_duration_list[idx]
        print('第{}个季度，会员的平均骑行时长是{:.2f}分钟，非会员的平均骑行时长是{:.2f}分钟'.format(
            idx + 1, member_mean_duration, casual_mean_duration
        ))
    # 分析结果保存
    # 构造多维数组
    mean_duration_arr = np.array([member_mean_duration_list, casual_mean_duration_list]).transpose()
    # 上面的这个，这是两行四列的数据，要是想存四行两列，需要转置，这时候用transpose()方法
    np.savetxt(
        'data/bikeshare/mean_duration.csv',  # 保存路径/文件名
        mean_duration_arr,  # 保存哪个变量
        delimiter=',',  # 变量之间以什么分隔
        header='Member mean duration, Casual mean duration',  # 首行类名标注
        fmt='%.4f',  # 数据存储默认科学计数法，如不愿意，fmt可指定小数点后几位
        comments=''  # 存储时，第一个类名会默认带个井号#，一般都不要井号，想指定为空时候就这么干
    )
    # 可视化
    plt.figure()
    # bar是柱状图，plot是折线图
    plt.plot(member_mean_duration_list, color='g', linestyle='-', marker='o', label='Member')  # 画第一条线
    plt.plot(casual_mean_duration_list, color='r', linestyle='--', marker='*', label='Casual')  # 画第二条线
    plt.title('Member VS Casual')  # 题目
    plt.xticks(range(0, 4), ['1st', '2nd', '3rd', '4th'], rotation=45)
    # 上一行的意思是对x刻度进行指定，这里是留四个位置，后面填位置上写的东西
    # 刻度特别长的时候，可以旋转避免文字相碰，可选参数rotation
    plt.xlabel('Quarter')  # x标签名
    plt.ylabel('Mean Duration (min)')  # y标签名
    plt.legend(loc='best')  # 图例位置自动选择最优位置摆放
    plt.tight_layout()  # 保持紧凑，避免下方变体文字越界
    plt.savefig('data/bikeshare/duration_trend.png')
    # 保存操作一定要在show之前，不然保存下来的将会是一个图片
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
    save_and_show_results(member_mean_duration_list, casual_mean_duration_list)


if __name__ == '__main__':
    main()
