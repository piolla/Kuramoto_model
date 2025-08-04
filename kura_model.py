import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 진동자 수와 시간 설정
N = 10  # 진동자 개수
T = 20  # 총 시뮬레이션 시간
dt = 0.05  # 시간 간격
steps = int(T / dt)

# 초기 위상과 고유 진동수
theta = np.random.uniform(0, 2*np.pi, N)
omega = np.random.normal(loc=1.0, scale=0.1, size=N)

# 결합 강도
K = 1.5

# 위상 기록
theta_history = np.zeros((steps, N))

# 시뮬레이션 수행
for t in range(steps):
    theta_history[t] = theta
    dtheta = np.zeros(N)
    for i in range(N):
        coupling = np.sum(np.sin(theta - theta[i]))
        dtheta[i] = omega[i] + (K / N) * coupling
    theta += dtheta * dt

# 애니메이션: 위상을 원 위에 표시
fig, ax = plt.subplots(figsize=(5, 5))
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
dots, = ax.plot([], [], 'o', color='blue')
title = ax.set_title("Kuramoto Model")

def update(frame):
    angles = theta_history[frame]
    x = np.cos(angles)
    y = np.sin(angles)
    dots.set_data(x, y)
    title.set_text(f"Step {frame}")
    return dots, title

ani = animation.FuncAnimation(fig, update, frames=steps, interval=50, blit=True)
plt.show()
