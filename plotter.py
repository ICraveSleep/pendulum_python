import matplotlib.pyplot as plt
import matplotlib.animation as animation
from math import sin, cos


def plot_and_animate(theta, d_theta, dd_theta, time, fps, save_anim=False):

    sim_p, sim_dp, sim_ddp, time = compress(theta, d_theta, dd_theta, time, fps)

    fig, axs = plt.subplots(3)
    fig.suptitle("Pendulum", fontsize=14)
    axs[0].plot(time, sim_p)
    axs[0].set_title(r"$\theta$")
    axs[0].set_ylabel(r"$\theta$")
    axs[0].set_xlabel("time")
    axs[1].plot(time, sim_dp)
    axs[1].set_title(r"$\dot\theta$")
    axs[1].set_ylabel(r"$\dot\theta$")
    axs[1].set_xlabel("time")
    axs[2].plot(time, sim_ddp)
    axs[2].set_title(r"$\ddot\theta$")
    axs[2].set_ylabel(r"$\ddot\theta$")
    axs[2].set_xlabel("time")
    fig.tight_layout()

    plt.rcParams['animation.html'] = 'html5'

    x = [sin(a) for a in sim_p]
    y = [cos(a) for a in sim_p]

    fig = plt.figure(figsize=(6.4, 6.4))
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(-1.2, 1.2), ylim=(-1.2, 1.2))
    ax.set_xlabel('position')
    ax.get_yaxis().set_visible(False)

    rod, = ax.plot([], [], color='k')
    pendulum, = ax.plot([], [], color='orange', marker='o', markersize=25, markeredgecolor='k')
    time_template = 'time = %.1fs'
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

    def init():
        rod.set_data([], [])
        pendulum.set_data([], [])
        time_text.set_text('')
        return pendulum, time_text

    def animate(i):
        rod.set_data([0, x[i]], [0, y[i]])
        pendulum.set_data([x[i]], [y[i]])
        hinge, = ax.plot([0, 0], [0, 0], color="orange", marker='o', markersize=10, markeredgecolor='k')
        time_text.set_text(time_template % time[i])
        return rod, pendulum, time_text

    anim = animation.FuncAnimation(fig, animate, len(time), interval=40, blit=False, init_func=init)
    if save_anim:
        anim.save('misc/pendulum.gif', writer='imagemagick', fps=30)
    plt.show()


def compress(theta, d_theta, dd_theta, time, fps):
    x_new = [theta[0]]
    dx_new = [d_theta[0]]
    ddx_new = [dd_theta[0]]
    time_new = [time[0]]
    compress_value = 1 / fps
    counter = 0
    for i in time:
        if i > compress_value:
            x_new.append(theta[counter])
            dx_new.append(d_theta[counter])
            ddx_new.append(dd_theta[counter])
            time_new.append(time[counter])
            compress_value += 1 / fps
        counter += 1
    return x_new, dx_new, ddx_new, time_new
