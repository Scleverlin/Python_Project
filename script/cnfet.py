import matplotlib.pyplot as plt
import pandas as pd

# New data
power_data = {
    'unit': ['ASAP7', 'CNFET7', 'CNFET5'],
    'Dynamic Power': [38.78064346,  2.65315163, 2.08638727],
    'Static Power': [2.1158511, 0.69999719, 0.44165572]
}
power_df = pd.DataFrame(power_data)

# Font properties
font_properties_labels = {'family': 'Courier New', 'weight': 'bold', 'size': 25}
font_properties_legend = {'family': 'Courier New', 'weight': 'bold', 'size': 20}
font_properties_ticks = {'family': 'Courier New', 'weight': 'bold', 'size': 25}

# Grayscale colors
colors = ["#888888", "#CCCCCC"]

# Bar width
bar_width = 0.5

# Plotting the data
fig, ax = plt.subplots(figsize=(10, 6))

# Plot new data (side by side)
indices = range(len(power_df))
ax.bar(indices, power_df['Static Power'], bar_width, label='Static Power', color=colors[1], hatch='\\')
ax.bar(indices, power_df['Dynamic Power'], bar_width, label='Dynamic Power', color=colors[0], bottom=power_df['Static Power'], hatch='//')

# Font properties
ax.set_ylabel('Total Power ($mW$)', fontdict=font_properties_labels)
# ax.set_title('Dynamic and Static Power', fontdict=font_properties_labels)
ax.set_xticks(indices)
ax.set_xticklabels(power_df['unit'], fontdict=font_properties_ticks)
ax.legend(prop=font_properties_legend)

ax.grid(False)
plt.tight_layout()
plt.show()
