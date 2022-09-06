from numerical_solver import forward_euler
from plotter import plot_and_animate

if __name__ == '__main__':
    dt = 0.01
    fps = 30
    ic = [0, 0, 0]
    time_span = [0, 10]
    pendulum_length = 1
    sim_p, sim_dp, sim_ddp, time = forward_euler(pendulum_length, initial_condition=ic, sim_time=time_span, dt=dt)
    plot_and_animate(sim_p, sim_dp, sim_ddp, time, fps, save_anim=False)
