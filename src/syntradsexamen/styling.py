import matplotlib as mpl
import matplotlib.pyplot as plt


# --- Professional muted color palette ---
SAGE = '#6B8E7F'
GRAY = '#8C8C8C'
TAN = '#D4A373'
GOLDENROD = '#B8860B'
SLATE = '#708090'
ROSY = '#BC8F8F'
OLIVE = '#556B2F'
BROWN = '#8B7355'
CADET = '#5F9EA0'

PALETTE = [SAGE, GRAY, TAN, GOLDENROD, SLATE, ROSY, OLIVE, BROWN, CADET]

# --- Statistical reference line colors ---
MEAN_COLOR = '#CC0000'
MEDIAN_COLOR = '#E04040'
P25_COLOR = '#D2691E'
P75_COLOR = '#E8820C'
PVALUE_COLOR = '#FF6347'


def standard_style():
    # Remove chart junk
    mpl.rcParams['axes.spines.right'] = False
    mpl.rcParams['axes.spines.top'] = False

    # Figure size
    mpl.rcParams['figure.figsize'] = (10, 5)

    # Color cycle
    mpl.rcParams['axes.prop_cycle'] = plt.cycler(color=PALETTE)

    # Lines: somewhat thicker than default (1.5)
    mpl.rcParams['lines.linewidth'] = 2.5
    mpl.rcParams['lines.markersize'] = 9

    # Font sizes: all comfortably above defaults for readability
    mpl.rcParams['font.size'] = 14
    mpl.rcParams['axes.titlesize'] = 18
    mpl.rcParams['axes.labelsize'] = 16
    mpl.rcParams['xtick.labelsize'] = 13
    mpl.rcParams['ytick.labelsize'] = 13
    mpl.rcParams['legend.fontsize'] = 13

    # Legend
    mpl.rcParams['legend.frameon'] = False
