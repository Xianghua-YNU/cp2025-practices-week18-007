'''这是一个氢原子电子云模拟的Python代码。'''
import numpy as np
import matplotlib.pyplot as plt

# 物理常数
a = 5.29e-2  # 波尔半径，单位：nm
D_max = 1.1  # 概率密度最大值
N = 10000    # 采样点数，可调整

# 概率密度函数 D(r)
def D(r):
    return 4 * r**2 / a**3 * np.exp(-2 * r / a)

# 蒙特卡洛采样
r_list = []
while len(r_list) < N:
    r = np.random.uniform(0, 0.8)  # 0.8nm足够覆盖主要分布
    p = D(r)
    if np.random.rand() < p / D_max:
        r_list.append(r)
r_list = np.array(r_list)

# 均匀采样球面角度
theta = np.arccos(1 - 2 * np.random.rand(N))
phi = 2 * np.pi * np.random.rand(N)

# 球坐标转直角坐标
x = r_list * np.sin(theta) * np.cos(phi)
y = r_list * np.sin(theta) * np.sin(phi)
z = r_list * np.cos(theta)

# 可视化
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文字体
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题
fig = plt.figure(figsize=(7,7))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x, y, z, s=1, alpha=0.5)
ax.set_title("氢原子基态电子云模拟")
ax.set_xlabel("x (nm)")
ax.set_ylabel("y (nm)")
ax.set_zlabel("z (nm)")
plt.show()

# 参数影响分析（可选，简单示例：不同采样点数）
# for N_test in [1000, 5000, 20000]:
