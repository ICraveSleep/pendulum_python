from math import sin, cos, pi


def runge_kutta_4(pendulum_length, initial_condition: [], sim_time: [], dt):
    time = create_time_span(sim_time[0], sim_time[-1], dt)

    length = pendulum_length
    g = 9.81
    p = initial_condition[0]
    dp = initial_condition[1]
    ddp = initial_condition[2]
    sim_p = []
    sim_dp = []
    sim_ddp = []
    for t in time:
        ddp = acc(p, g, length)
        f1 = ddp
        f2 = acc(p+dt/2*f1, g, length)
        f3 = acc(p+dt/2*f2, g, length)
        f4 = acc(p+dt*f3, g, length)

        dp = dp + dt/6*(f1+2*f2+2*f3+f4)
        #dp = dp + dt*ddp

        p = p + dp * dt

        sim_p.append(p)
        sim_dp.append(dp)
        sim_ddp.append(ddp)
    return sim_p, sim_dp, sim_ddp, time


def acc(p, g, length):
    return -g / length * cos(p)


def create_time_span(t_start, t_end, step_size):
    time_span = []
    time = t_start
    while time <= t_end:
        time_span.append(time)
        time += step_size
    time_span.append(time)
    return time_span
