import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as font_manager

plt.rcParams['font.family'] = 'Courier New'
plt.rcParams['font.weight'] = 'bold'
plt.rcParams['axes.labelweight'] = 'bold'
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['xtick.labelsize'] = 20
plt.rcParams['ytick.labelsize'] = 20
plt.rcParams['axes.labelsize'] = 20

# Define data for PROBE3 as a hypothetical example
data3 = np.array([
    [350000000, 370000000, 390000000, 410000000, 430000000, 450000000],
    [320000000, 340000000, 360000000, 380000000, 400000000, np.nan],
    [300000000, 320000000, 340000000, 360000000, np.nan, np.nan],
    [280000000, 300000000, 320000000, np.nan, np.nan, np.nan],
    [260000000, 280000000, np.nan, np.nan, np.nan, np.nan],
    [240000000, np.nan, np.nan, np.nan, np.nan, np.nan]
])

# Your existing data arrays
data = np.array([
    [355813847.2, 386597460.3, 398952259.6, 379840419.6, 336949535, 339530192.2],
    [359715631.1, 337628478.6, 343163473.4, 324023800.2, 298609574.9, np.nan],
    [327140260.7, 331781188.1, 315708555.7, 302367319, np.nan, np.nan],
    [299765976.6, 315561007.3, 318009256.5, np.nan, np.nan, np.nan],
    [355723654.5, 300653046.3, np.nan, np.nan, np.nan, np.nan],
    [315235922.5, np.nan, np.nan, np.nan, np.nan, np.nan]
])
data2 = np.array([
    [9.904354778, 8.912521267, 9.155492077, 8.886287361, 9.19280033, 7.418483793],
    [8.036063426, 8.29523961, 9.168848531, 7.8114751, 6.535799847, np.nan],
    [7.785320866, 6.942586153, 7.76095731, 7.017071175, np.nan, np.nan],
    [6.301390677, 6.54877406, 6.618666948, np.nan, np.nan, np.nan],
    [6.618666948, 6.46728567, np.nan, np.nan, np.nan, np.nan],
    [6.779197075, np.nan, np.nan, np.nan, np.nan, np.nan]
])

# Set up for 3 subplots
fig, axes = plt.subplots(1, 3, figsize=(30, 8))  # Adjust the figure size as necessary

# Configure each heatmap with individual color scaling
data_sets = [data3, data, data2]
titles = ["a. PROBE3", "b. ASAP7", "c. CNFET7"]

for i, dataset in enumerate(data_sets):
    vmin = np.nanmin(dataset)
    vmax = np.nanmax(dataset)
    sns.heatmap(dataset, annot=True, cmap='RdBu', xticklabels=np.arange(6), yticklabels=np.arange(6),
                annot_kws={"weight": "bold", "size": 25}, fmt=".1f", ax=axes[i], vmin=vmin, vmax=vmax)
    axes[i].xaxis.tick_top()
    axes[i].xaxis.set_label_position('top')
    axes[i].set_xlabel('f : Max fan-out of adders $=2^f+1$')
    axes[i].set_ylabel('l : Logic level of adders $=L+l$ ')
    axes[i].text(0.4, -0.1, titles[i], transform=axes[i].transAxes, va='center', fontsize=25)

# Adjust spacing and layout
plt.subplots_adjust(wspace=0.8)  # Adjust the spacing as needed
plt.tight_layout()
plt.show()
