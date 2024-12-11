#绘制总分折线，单科柱状图
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']  # 使用黑体字

# 读取Excel文件
file_path = "D:/grade.xlsx"
df = pd.read_excel(file_path)

# 获取列数据
dates = df.iloc[1:12, 8].values  # 考试日期
total_scores = df.iloc[1:12, 3].values  # 总分
chinese_scores = df.iloc[1:12, 4].values  # 语文成绩
math_scores = df.iloc[1:12, 5].values  # 数学成绩
english_scores = df.iloc[1:12, 6].values  # 英语成绩
science_scores = df.iloc[1:12, 7].values  # 理综成绩

# 创建图形
fig, ax1 = plt.subplots(figsize=(12, 6))

# 设置标签
ax1.set_xlabel('考试日期', fontsize=12)
ax1.set_ylabel('总分', fontsize=12, color='blue')

# 创建x轴坐标
x = range(len(total_scores))

# 处理日期格式
dates_str = [str(int(date))[0:4] + "." + str(int(date))[6:8] for date in dates]

# 绘制总分折线图
ax1.plot(x, total_scores, marker='o', c='blue', label='总分')
ax1.tick_params(axis='y', labelcolor='blue')

# 创建第二个y轴
ax2 = ax1.twinx()
ax2.set_ylabel('各科成绩', fontsize=12, color='black')

# 绘制各科成绩的柱状图
bar_width = 0.2
ax2.bar([i - 1.5 * bar_width for i in x], chinese_scores, width=bar_width, label='语文', color='red', alpha=0.6)
ax2.bar([i - 0.5 * bar_width for i in x], math_scores, width=bar_width, label='数学', color='green', alpha=0.6)
ax2.bar([i + 0.5 * bar_width for i in x], english_scores, width=bar_width, label='英语', color='purple', alpha=0.6)
ax2.bar([i + 1.5 * bar_width for i in x], science_scores, width=bar_width, label='理综', color='orange', alpha=0.6)

# 设置x轴刻度和标签
ax1.set_xticks(x)
ax1.set_xticklabels(dates_str, rotation=45)

# 获取日期范围
date1 = dates_str[0]
date2 = dates_str[-1]

# 设置背景颜色
fig.set_facecolor((0.92, 0.92, 0.96))

# 设置标题
ax1.set_title(f'李华的高三成绩变化(日期：{date1}-{date2})', fontsize=14)

# 计算最大值和最小值的位置及值
i_min_total, min_total = np.argmin(total_scores), np.min(total_scores)
i_max_total, max_total = np.argmax(total_scores), np.max(total_scores)

# 添加文本注释
ax1.text(i_max_total, max_total, f'{max_total}(最高总分)', color='r', fontsize=12, verticalalignment='bottom')
ax1.text(i_min_total, min_total, f'{min_total}(最低总分)', color='g', fontsize=12, verticalalignment='top')

# 添加图例
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# 显示图形
plt.tight_layout()
plt.show()