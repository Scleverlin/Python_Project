import numpy as np
import matplotlib.pyplot as plt

# 数据
data = np.array([
    [0.981766911, 0.741573166, 0.70752815, 0.722155569, 0.796751849, 0.51243],
    [0.356983475, 0.3709585, 0.392592296, 0.434355443, 0.361839885, 100],
    [0.271152284, 0.308285418, 0.311578998, 0.298841006, 100, 100],
    [0.272201794, 0.29945331, 0.29281941, 100, 100, 100],
    [0.272974674, 0.311724, 100, 100, 100, 100],
    [0.30525, 100, 100, 100, 100, 100]
])

f_values = np.arange(6)
l_values = np.arange(6)
X, Y = np.meshgrid(f_values, l_values)

# 从数据数组中提取Z值
Z = data

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# 绘制散点图
ax.scatter(X, Y, Z, c=Z, cmap='viridis', depthshade=True)
ax.set_xlabel('f values')
ax.set_ylabel('l values')
ax.set_zlabel('y values')
ax.set_title('3D Scatter Plot of y=f(f,l)')
plt.show()
plt.savefig("figure_name.png")  
