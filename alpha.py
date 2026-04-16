import numpy as np
import matplotlib.pyplot as plt

def generate_alpha_wave(duration=5, sample_rate=1000, color='#8A2BE2', line_width=1.5,截取长度=None):
    """
    生成并绘制模拟alpha脑电波的波形（仅保留波形曲线）
    
    参数:
    duration: 持续时间（秒）
    sample_rate: 采样率
    color: 波形颜色
    line_width: 线条宽度
    截取长度: 截取的波形长度（点数），None表示使用全部长度
    """
    # 计算总点数
    points = int(duration * sample_rate)
    
    # 生成时间轴
    t = np.linspace(0, duration, points)
    
    # 生成alpha波（频率8-13Hz）
    # 基础频率在8-13Hz之间
    base_frequency = np.random.uniform(1,3)
    
    # 基础振幅（相对稳定）
    base_amplitude = 0.5
    
    # 生成基础波形
    waveform = base_amplitude * np.sin(2 * np.pi * base_frequency * t)
    
    # 添加轻微的振幅调制，模拟真实脑电波的微小变化
    # 慢波调制（0.1-0.5Hz）
    slow_modulation = 1 + 3 * np.sin(2 * np.pi * np.random.uniform(0.1, 1) * t)
    waveform *= slow_modulation
    
    # 添加非常小的随机噪声，模拟脑电波的微小波动
    noise = 0 * np.random.randn(points)
    waveform += noise
    
    # 截取波形
    if 截取长度 is not None and 截取长度 < points:
        t = t[:截取长度]
        waveform = waveform[:截取长度]
    
    # 创建图形
    plt.figure(figsize=(12, 4))
    
    # 移除所有坐标轴和边框
    plt.axis('off')
    
    # 设置背景为透明
    plt.gca().set_facecolor('none')
    plt.gcf().set_facecolor('none')
    
    # 调整边距，移除所有空白
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
    
    # 绘制波形图（仅曲线）
    plt.plot(t, waveform, color=color, linewidth=line_width)
    
    # 保存为矢量图
    output_file = 'wave/alpha_wave.svg'
    plt.savefig(output_file, format='svg', bbox_inches='tight', transparent=True, dpi=100)
    print(f"波形图已保存为: {output_file}")
    
    # 显示图形
    plt.show()

if __name__ == "__main__":
    # 生成模拟alpha脑电波的波形
    generate_alpha_wave(
        duration=3,
        sample_rate=1000,
        color='#8A2BE2',
        line_width=1.5
    )