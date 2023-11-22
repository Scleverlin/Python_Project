import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.family'] = 'Courier New'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titleweight'] = 'bold'
# 数据
annot_format = "{:.3f}"
data = np.array([
    [0.981766911, 0.741573166, 0.70752815, 0.722155569, 0.796751849, 0.51243],
    [0.356983475, 0.3709585, 0.392592296, 0.434355443, 0.361839885, np.nan],
    [0.271152284, 0.308285418, 0.311578998, 0.298841006, np.nan, np.nan],
    [0.272201794, 0.29945331, 0.29281941, np.nan, np.nan, np.nan],
    [0.272974674, 0.311724, np.nan, np.nan, np.nan, np.nan],
    [0.30525, np.nan, np.nan, np.nan, np.nan, np.nan]
])
data2 = np.array([
    [16.75590202	,17.96097145	,19.66725	,24.29701987	,25.9318	,25.65533267],
    [11.11146131	,12.2276	,12.59232	,12.92121175	,13.361205, np.nan],
    [9.746470927	,10.64381396	,10.8003	,10.44122749	, np.nan, np.nan],
    [9.801261497,	10.85482701,	10.80382001, np.nan, np.nan, np.nan],
    [	10.637925	,11.82919556, np.nan, np.nan, np.nan, np.nan],
    [11.73674703, np.nan, np.nan, np.nan, np.nan, np.nan]
])
	
f_values = np.arange(6)
l_values = np.arange(6)

# 使用Seaborn的heatmap函数绘制热图
plt.figure(figsize=(10, 8))
# sns.heatmap(data, annot=True, cmap='viridis', xticklabels=f_values, yticklabels=l_values)
ax = sns.heatmap(data2, annot=True, cmap='Blues', xticklabels=f_values, yticklabels=l_values, annot_kws={"weight": "bold"},fmt=".3f")
# plt.figure(figsize=(10, 8))
# ax = sns.heatmap(data, annot=True, cmap='gray_r', xticklabels=f_values, yticklabels=l_values, annot_kws={"weight": "bold"})
ax.xaxis.tick_top()
ax.xaxis.set_label_position('top')
# plt.title('Heatmap of PDP')
plt.xlabel('f : Max fan-out$=2^f + 1$')
plt.ylabel('l : Logic level$= L+l$ ')
plt.show()

# 数据已经按照您提供的格式排列，无需更改
# 重新绘制热图



