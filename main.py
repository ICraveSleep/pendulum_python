from math import sin, cos
from plotter import plot_and_animate


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

    plot_and_animate(sim_p, sim_dp, sim_ddp, time, fps, save_anim=False)
