import matplotlib.pyplot as plt
import numpy as np

def plot_gauge(value):
    fig, ax = plt.subplots()
    ax.set_ylim([0,100])
    ax.set_xlim([-1,1])
    theta = np.linspace(0, 2*np.pi, 100)
    x = np.sin(theta)
    y = np.cos(theta)
    ax.plot(x, y, color='gray')
    angle = (value / 100) * (2 * np.pi)
    x = [0, np.sin(angle)]
    y = [0, np.cos(angle)]
    ax.plot(x, y, color='red', linewidth=10)
    plt.show()

plot_gauge(50)



