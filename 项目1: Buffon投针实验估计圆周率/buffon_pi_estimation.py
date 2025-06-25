import random
import math
import matplotlib.pyplot as plt

def buffon_needle_simulation(num_trials):
    """
    执行Buffon投针实验
    :param num_trials: 投针次数
    :return: π的估计值
    """
    # 平行线间距 (D) 和针的长度 (L)，满足 L <= D
    D = 2.0
    L = 1.0
    
    # 初始化相交次数
    cross_count = 0
    
    for _ in range(num_trials):
        # 随机生成针中心点到最近平行线的距离 (0 <= y <= D/2)
        y = random.uniform(0, D/2)
        
        # 随机生成针与平行线的夹角 (0 <= theta <= π/2)
        theta = random.uniform(0, math.pi/2)
        
        # 判断针是否与平行线相交
        if y <= (L/2) * math.sin(theta):
            cross_count += 1
    
    # 计算π的估计值（避免除零错误）
    if cross_count > 0:
        pi_estimate = (2 * L * num_trials) / (D * cross_count)
    else:
        pi_estimate = float('inf')  # 如果没有相交，返回无穷大
    
    return pi_estimate

def analyze_precision(trial_counts):
    """
    分析不同实验次数对π估计精度的影响
    :param trial_counts: 不同实验次数的列表
    """
    results = []
    
    print("实验次数\t估计π值\t绝对误差\t相对误差(%)")
    print("-" * 50)
    
    for n in trial_counts:
        pi_est = buffon_needle_simulation(n)
        abs_error = abs(pi_est - math.pi)
        rel_error = (abs_error / math.pi) * 100
        
        results.append((n, pi_est, abs_error, rel_error))
        print(f"{n}\t{pi_est:.6f}\t{abs_error:.6f}\t{rel_error:.4f}%")
    
    return results

def plot_results(results):
    """
    可视化实验结果
    :param results: 分析结果列表
    """
    # 准备数据
    trials, estimates, errors, rel_errors = zip(*results)
    
    # 创建图表
    plt.figure(figsize=(12, 8))
    
    # 子图1：π估计值随实验次数的变化
    plt.subplot(2, 1, 1)
    plt.plot(trials, estimates, 'bo-', label='估计值')
    plt.axhline(y=math.pi, color='r', linestyle='--', label='真实值')
    plt.xscale('log')
    plt.xlabel('实验次数')
    plt.ylabel('π估计值')
    plt.title('π估计值随实验次数变化')
    plt.legend()
    plt.grid(True)
    
    # 子图2：相对误差随实验次数的变化
    plt.subplot(2, 1, 2)
    plt.plot(trials, rel_errors, 'go-')
    plt.xscale('log')
    plt.xlabel('实验次数')
    plt.ylabel('相对误差(%)')
    plt.title('相对误差随实验次数变化')
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('buffon_analysis.png')
    plt.show()

if __name__ == "__main__":
    # 设置不同的实验次数
    trial_counts = [100, 500, 1000, 5000, 10000, 50000, 100000]
    
    # 执行实验并分析结果
    results = analyze_precision(trial_counts)
    
    # 可视化结果
    plot_results(results)
