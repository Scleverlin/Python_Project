import matplotlib.pyplot as plt
import pandas as pd

# New data provided
data = {
    'unit': ['NG15', 'ASAP7', 'CNFET7', 'CNFET5'],
    'X1': [1443, 313, 141, 124],
    'X2': [0, 195, 1340, 1191],
    'other': [0, 782, 2, 2]
}
df = pd.DataFrame(data)

# Font properties - modify these as needed
font_properties_title = {'family': 'Courier New', 'weight': 'normal', 'size': 14}
font_properties_labels = {'family': 'Courier New', 'weight': 'bold', 'size': 25}
font_properties_legend = {'family': 'Courier New', 'weight': 'bold', 'size': 20}
font_properties_ticks = {'family': 'Courier New', 'weight': 'bold', 'size': 25}

# Color combination - modify this variable to change colormap
colormap_name = "tab20"
colors = plt.cm.get_cmap(colormap_name, df.shape[1]-1)(range(df.shape[1]-1))

# Bar width - modify this value to adjust the bar width (0 for thinnest, 1 for thickest)
bar_width = 0.5

# Plotting the data
fig, ax = plt.subplots(figsize=(12, 8))
categories = df.columns[1:]
for i, category in enumerate(categories):
    bottoms = df[categories[:i]].sum(axis=1) if i > 0 else [0]*df.shape[0]
    ax.bar(df['unit'], df[category], bottom=bottoms, color=colors[i], label=category, width=bar_width)

# Applying font properties
# ax.set_title('Stacked Bar Chart for Different Units', fontdict=font_properties_title)
ax.set_ylabel('Cell Count', fontdict=font_properties_labels)
# ax.legend(loc='upper right', prop=font_properties_legend, ncol=len(categories))
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), prop=font_properties_legend, ncol=1)

for label in ax.get_xticklabels() + ax.get_yticklabels():
    label.set_family(font_properties_ticks['family'])
    label.set_size(font_properties_ticks['size'])
    label.set_weight(font_properties_ticks['weight'])

ax.grid(False)
plt.tight_layout()
plt.show()
