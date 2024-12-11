#绘制李华的理综成绩直方图及其正态分布
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体字

# 读取Excel文件
file_path = "D:/grade.xlsx"
df = pd.read_excel(file_path)

# 获取理综成绩数据
science_scores = df.iloc[1:12, 6].values  # 假设理综成绩在第7列（从0开始计数）

# 创建图形
fig, ax = plt.subplots(figsize=(8, 6))

# 绘制直方图
n, bins, patches = ax.hist(science_scores, bins=5, density=True, alpha=0.6, color='blue')

# 计算正态分布曲线
mu, std = norm.fit(science_scores)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, std)
ax.plot(x, p, 'k', linewidth=2)

# 设置标题和标签
ax.set_xlabel('理综成绩', fontsize=12)
ax.set_ylabel('频率', fontsize=12)
ax.set_title('李华的理综成绩直方图及正态分布', fontsize=14)

# 添加正态分布参数
ax.text(0.6, 0.8, f'μ = {mu:.2f}\nσ = {std:.2f}', transform=ax.transAxes, fontsize=12, verticalalignment='top')

# 显示图形
plt.show()