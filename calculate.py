import numpy as np

# 创建一个空的列表
data_list = []
tx_num = []

# 列表的第一个数据是 0xFF
tx_num.append(0xFF)

# 创建一个包含16位整数的NumPy数组
data1 = np.int16(169)
data2 = np.int16(-87)

data_list[0] = data1
data_list[1] = data1 >> 8
data_list[2] = data2
data_list[3] = data2 >> 8

# 使用循环赋值列表中的其余数据
for i in range(1, 5):  # i 从 1 到 4
    # 计算每个元素的值，并将其添加到列表中
    tx_num.append(data_list[i-1])  # 假设在这里使用 i * 10 进行赋值

# 列表的最后一个数据是 0xFE
data_list.append(0xFE)








