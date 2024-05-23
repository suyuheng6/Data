# --------------------------转换成csv格式文件------------------
# import pandas as pd
#
# # 加载数据
# file_path = 'user_taggedartists-timestamps.dat'  # 假设数据文件和此 Python 脚本在同一个目录下
# data = pd.read_csv(file_path, delimiter='\t')  # 使用制表符作为分隔符
#
# # 排序数据
# # 首先按 userID 排序，然后在每个用户内按 timestamp 排序
# sorted_data = data.sort_values(by=['userID', 'timestamp'],ascending=[True, False])
#
# # 保存为 CSV 文件
# sorted_data.to_csv('LastFm.txt', index=False,header=None)  # 不保存行索引到文件

#----------------转换用户成csv格式--------------------
import pandas as pd

# 加载数据
file_path = 'user_friends.dat'  # 假设数据文件和此 Python 脚本在同一个目录下
data = pd.read_csv(file_path, delimiter='\t')  # 使用制表符作为分隔符


# 保存为 CSV 文件
data.to_csv('LastFm.uu', index=False,header=None,sep=',')  # 不保存行索引到文件
