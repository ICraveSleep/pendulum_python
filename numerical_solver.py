from math import sin, pi


def forward_euler(pendulum_length, initial_condition: [], sim_time: [], dt):
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
        ddp = -g / length * sin(p)
        dp = dp + ddp * dt
        p = p + dp * dt
        sim_p.append(p)
        sim_dp.append(dp)
        sim_ddp.append(ddp)
    return sim_p, sim_dp, sim_ddp, time


def create_time_span(t_start, t_end, step_size):
    time_span = []
    time = t_start
    while time <= t_end:
        time_span.append(time)
        time += step_size
    time_span.append(time)
    return time_span
