import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
#
# fig = plt.figure()
# fig.set_dpi(100)
# fig.set_size_inches(7, 6.5)
#
# ax = plt.axes(xlim=(-5, 5), ylim=(-5, 5))
# patch = plt.Circle((5, -5), 0.75, fc='y')
#
# def init():
#     patch.center = (5, -5)
#     ax.add_patch(patch)
#     return patch,
#
# def animate(i):
#     x, y = patch.center
#     x =  np.sin(np.radians(i))
#     y =  np.cos(np.radians(i))
#     patch.center = (x, y)
#     return patch,
#
# anim = animation.FuncAnimation(fig, animate,
#                                init_func=init,
#                                frames=360,
#                                interval=20,
#                                blit=True)
#
# plt.show()
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

x = np.arange(0, 2*np.pi, 0.01)
line, = ax.plot(x, np.sin(x))


def init():  # only required for blitting to give a clean slate.
    line.set_ydata([np.nan] * len(x))
    return line,


def animate(i):
    line.set_ydata(np.sin(x + i / 100))  # update the data.
    return line,


ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=2, blit=True, save_count=50)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# from matplotlib.animation import FFMpegWriter
# writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()
