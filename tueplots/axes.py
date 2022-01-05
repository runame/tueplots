"""Axes behaviour."""


def lines(
    *,
    base_width=0.5,
    line_base_ratio=2.0,
    tick_major_base_ratio=1.0,
    tick_minor_base_ratio=0.5,
    axisbelow=True,
):
    return {
        # Set the line-widths appropriately (including the grid)
        "axes.linewidth": base_width,
        "lines.linewidth": line_base_ratio * base_width,
        "xtick.major.width": tick_major_base_ratio * base_width,
        "ytick.major.width": tick_major_base_ratio * base_width,
        "xtick.minor.width": tick_minor_base_ratio * base_width,
        "ytick.minor.width": tick_minor_base_ratio * base_width,
        "xtick.major.size": 1.5 + 3 * base_width,
        "ytick.major.size": 1.5 + 3 * base_width,
        "xtick.minor.size": 1.0 + 3 * 0.5 * base_width,
        "ytick.minor.size": 1.0 + 3 * 0.5 * base_width,
        "grid.linewidth": base_width,
        # Legend frame linewidth
        "patch.linewidth": base_width,
        "legend.edgecolor": "inherit",  # inherit color from axes. passing 'color' leads to awkward future warnings.
        # Control the zorder of the ticks and gridlines
        # This is somewhat out of place in this function, but creating a new function
        # seems a bit unnecessary here... suggestions welcome!
        "axes.axisbelow": axisbelow,
    }


def grid(*, grid_alpha=0.15, grid_linestyle="solid"):
    return {
        # Update the linestyle of the grid
        # (it shares a color with the frame, and needs to be distinguishable)
        "grid.linestyle": grid_linestyle,
        "grid.alpha": grid_alpha,
    }


def legend(*, shadow=False, frameon=True, fancybox=False):
    return {
        "legend.shadow": shadow,
        "legend.frameon": frameon,
        "legend.fancybox": fancybox,
    }


def color(*, base="black", face="none"):
    return {
        "text.color": base,
        "axes.edgecolor": base,
        "axes.labelcolor": base,
        "xtick.color": base,
        "ytick.color": base,
        "grid.color": base,
        "axes.facecolor": face,
    }


def spines(*, left=True, right=True, top=True, bottom=True):
    return {
        "axes.spines.left": left,
        "axes.spines.right": right,
        "axes.spines.top": top,
        "axes.spines.bottom": bottom,
    }


def tick_direction(*, x="inout", y="inout"):
    return {
        "xtick.direction": x,
        "ytick.direction": y,
    }
