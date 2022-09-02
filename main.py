from math import sin, cos
import matplotlib.pyplot as plt
import matplotlib.animation as animation


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


def create_time_span(t_start, t_end, step_size):
    time_span = []
    time = t_start
    while time <= t_end:
        time_span.append(time)
        time += step_size
    time_span.append(time)
    return time_span


if __name__ == '__main__':
    dt = 0.01
    fps = 30
    time = create_time_span(0, 10, dt)
    ic = [1.57, 0, 0]
    l = 1
    g = 9.81
    p = ic[0]
    dp = ic[1]
    ddp = ic[2]
    sim_p = []
    sim_dp = []
    sim_ddp = []
    for t in time:
        ddp = g/l * sin(p)
        dp = dp + ddp * dt
        p = p + dp * dt

        sim_p.append(p)
        sim_dp.append(dp)
        sim_ddp.append(ddp)

    sim_p, sim_dp, sim_ddp, time = compress(sim_p, sim_dp, sim_ddp, time, fps)

    fig, axs = plt.subplots(3)
    fig.suptitle("figure", fontsize=14)
    axs[0].plot(time, sim_p)
    axs[0].set_title("theta")
    axs[1].plot(time, sim_dp)
    axs[1].set_title("theta d")
    axs[2].plot(time, sim_ddp)
    axs[2].set_title("theta dd")
    fig.tight_layout()

    plt.rcParams['animation.html'] = 'html5'

    pendulum_length = 1

    x = [sin(a) for a in sim_p]
    y = [cos(a) for a in sim_p]

    fig = plt.figure(figsize=(6.4, 6.4))
    ax = fig.add_subplot(111, autoscale_on=False, xlim=(-1.2, 1.2), ylim=(-1.2, 1.2))
    ax.set_xlabel('position')
    ax.get_yaxis().set_visible(False)

    hinge, = ax.plot([0, 0], [0, 0], 'k', marker='o')
    pendulum, = ax.plot([], [], color='k', marker='o', markersize=10)
    time_template = 'time = %.1fs'
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

    def init():
        pendulum.set_data([], [])
        time_text.set_text('')
        return pendulum, time_text

    def animate(i):
        pendulum.set_data([0, x[i]], [0, y[i]])
        time_text.set_text(time_template % time[i])
        return pendulum, time_text

    anim = animation.FuncAnimation(fig, animate, len(time), interval=40, blit=False, init_func=init)

    anim.save('gifs/energy_swingup.gif', writer='imagemagick', fps=30)

    plt.show()