import numpy as np
import matplotlib.pyplot as plt
import random

class ChainReactionSimulator:
    def __init__(self, size=100, initial_neutrons=1, absorption_prob=0.3, fission_prob=0.5, fission_neutrons=2):
        """
        初始化链式反应模拟器
        
        参数:
        size: 模拟区域大小
        initial_neutrons: 初始中子数
        absorption_prob: 中子被吸收概率
        fission_prob: 中子引发裂变概率
        fission_neutrons: 每次裂变产生的中子数
        """
        self.size = size
        self.absorption_prob = absorption_prob
        self.fission_prob = fission_prob
        self.fission_neutrons = fission_neutrons
        self.neutrons = [{'position': np.random.rand(2)*size, 'active': True} 
                         for _ in range(initial_neutrons)]
        self.history = [len(self.neutrons)]
        
    def step(self):
        """模拟一个时间步"""
        new_neutrons = []
        
        for neutron in self.neutrons:
            if not neutron['active']:
                continue
                
            # 中子移动
            neutron['position'] += np.random.normal(0, 1, 2)
            
            # 边界检查
            neutron['position'] = np.clip(neutron['position'], 0, self.size)
            
            # 中子命运
            fate = random.random()
            
            if fate < self.absorption_prob:
                # 被吸收
                neutron['active'] = False
            elif fate < self.absorption_prob + self.fission_prob:
                # 引发裂变，产生新中子
                neutron['active'] = False
                for _ in range(self.fission_neutrons):
                    new_neutrons.append({
                        'position': neutron['position'] + np.random.normal(0, 0.5, 2),
                        'active': True
                    })
            # 否则继续存在但不引发裂变
        
        # 更新中子列表
        self.neutrons = [n for n in self.neutrons if n['active']] + new_neutrons
        self.history.append(len(self.neutrons))
        
    def simulate(self, steps=100):
        """运行模拟"""
        for _ in range(steps):
            self.step()
            
    def visualize(self):
        """可视化结果"""
        plt.figure(figsize=(12, 5))
        
        # 中子数量变化图
        plt.subplot(1, 2, 1)
        plt.plot(self.history)
        plt.title('Neutron Population Over Time')
        plt.xlabel('Time Step')
        plt.ylabel('Number of Neutrons')
        
        # 中子位置图
        plt.subplot(1, 2, 2)
        if len(self.neutrons) > 0:
            positions = np.array([n['position'] for n in self.neutrons if n['active']])
            plt.scatter(positions[:, 0], positions[:, 1], alpha=0.5)
        plt.title('Neutron Positions')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.xlim(0, self.size)
        plt.ylim(0, self.size)
        
        plt.tight_layout()
        plt.show()

# 示例使用
if __name__ == "__main__":
    # 默认参数模拟
    sim = ChainReactionSimulator()
    sim.simulate(50)
    sim.visualize()
