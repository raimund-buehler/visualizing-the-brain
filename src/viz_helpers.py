"""Small plotting helpers for the Visualizing the Brain notebooks."""

from nilearn import plotting


def plot_brain_at_coords(img, x=0, y=0, z=0, title="Brain slice"):
    """Plot one anatomical brain view at selected MNI coordinates.

    Parameters
    ----------
    img : Niimg-like object
        Brain image to display.
    x, y, z : int or float
        MNI coordinates for the displayed slice.
    title : str
        Title shown above the figure.
    """
    return plotting.plot_anat(
        img,
        cut_coords=(x, y, z),
        title=title,
        display_mode="ortho",
        draw_cross=True,
    )
