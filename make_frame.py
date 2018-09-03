# Plot
import matplotlib
import matplotlib.pyplot as plt

# GIF
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

from tools import

# Jupyter
%matplotlib inline

# Option to write gif
write_gif = False

# Instanciate figure
fig = plt.figure(figsize=(9, 6))

size = 0.33
alignement = 0.1

# Classic plot
ax_carthesian = fig.add_axes([alignement, 0.4, size, size])
# Polar plot
ax_polar = fig.add_axes([alignement + size, 0.4, size, size], polar=True)
# Patchwork
ax_patchwork = fig.add_axes([alignement + 1.8*size, 0.4, size, size])

# Global iteration
iteration = 0

# PLOTS
global size_time_serie
size_time_serie = float(45)

def make_frame(time):
    # Timesteps
    global iteration

    # Data
    t, time_serie = create_time_serie(45, 0)
    gaf, phi, r, scaled_time_serie = gramian_angular_field(time_serie)

    # Set to 0 unkown data at time stamp iteration
    #t[iteration:] = 0
    time_serie[iteration:] = 0
    scaled_time_serie[iteration:] = 0
    phi[iteration:] = math.acos(0)
    #r[iteration:] = 0
    gaf[iteration:, iteration:] = 0

    # PLOTS
    font = {
        'family': 'serif',
        'color':  'darkblue',
        'weight': 'normal',
        'size': 16,
        }

    # Clear plot
    ax_carthesian.clear()
    ax_polar.clear()
    ax_patchwork.clear()

    # Original Time series
    ax_carthesian.plot(t, scaled_time_serie)
    ax_carthesian.set_title("Scaled Time Serie", fontdict=font)
    ax_carthesian.set_xticklabels([])

    # Polar encoding
    ax_polar.plot(phi, r)
    ax_polar.set_title("Polar Encoding", fontdict=font)
    ax_polar.set_rticks([0, 1])
    ax_polar.set_rlabel_position(-22.5)
    ax_polar.grid(True)

    # Gramian Angular Field
    ax_patchwork.matshow(gaf)
    ax_patchwork.set_title("Gramian Angular Field", fontdict=font)
    ax_patchwork.set_yticklabels([])
    ax_patchwork.set_xticklabels([])

    iteration = iteration + 1

    return mplfig_to_npimage(fig)


if __name__ == "__main__":

    # GIF: Write and visualise
    animation = VideoClip(make_frame, duration=2)

    if(write_gif):
        animation.write_gif("gramian_angulat_field.gif",fps=20)

    animation.ipython_display(fps=20, loop=True, autoplay=True)
