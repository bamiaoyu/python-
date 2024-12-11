#绘制李华最后一次考试的成绩雷达图
import pandas as pd
import matplotlib.pyplot as plt
from math import pi
import numpy as np  # 导入numpy库

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体字

# 读取Excel文件
file_path = "D:/grade.xlsx"  # Excel文件路径
df = pd.read_excel(file_path)

# 最后一行是最后一次考试的成绩
last_exam_scores = df.iloc[-1, [4, 5, 6, 7]].to_dict()  # 科目名称在第5列到第8列（从0开始计数）

# 创建数据框
categories = list(last_exam_scores.keys())
values = list(last_exam_scores.values())

# 计算角度
angles = [n / float(len(categories)) * 2 * pi for n in range(len(categories))]
values += values[:1]  # 封闭图形
angles += angles[:1]

# 创建图形
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# 绘制雷达图
ax.fill(angles, values, 'b', alpha=0.25)
ax.plot(angles, values, 'b', linewidth=2)

# 设置标签
ax.set_thetagrids(np.degrees(angles[:-1]), categories)
ax.set_rlabel_position(30)

# 设置标题
ax.set_title('李华最后一次考试的成绩雷达图', fontsize=14)

# 显示图形
plt.tight_layout()
plt.show()