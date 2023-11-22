import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

# Data for the graph
tech_iterations = np.linspace(0, 10, 100)

# Using a quadratic function to represent the curve
gate_impact = -1/3*((tech_iterations+2) ** 2) + 89
wire_impact = 100 - gate_impact

# Adjusting the data to stop when wire_impact is exactly 60%
indices = np.where(wire_impact >= 60)[0]

# Check if there are any valid indices
if len(indices) > 0:
    # Get the first valid index
    end_idx = indices[0]
else:
    # Handle the case where no valid indices are found
    end_idx = len(tech_iterations) - 1 

# Plotting the steeper curves up to the point where wire impact is 60%
plt.figure(figsize=(12, 7))
plt.plot(tech_iterations[:end_idx], gate_impact[:end_idx], label='Gate Delay/Power', color='blue', linewidth=2)  # Adjust line thickness here
plt.plot(tech_iterations[:end_idx], wire_impact[:end_idx], label='Wire Delay/Power', color='red', linewidth=2)  # Adjust line thickness here

# Customizing text style
font_title = FontProperties(family='Courier New', style='normal', size=18, weight='bold')  # Adjust title font style and size
font_label = FontProperties(family='Courier New', style='normal', size=14, weight='bold')  # Adjust label font style and size

# plt.title('Impact of Gate vs Wire with Technological Progression', fontproperties=font_title)
plt.ylabel('Percentage of Impact (%)', fontproperties=font_label)
plt.xlabel('Years', fontproperties=font_label)
plt.legend(prop=font_label)
plt.grid(True, which='both', linestyle='--', linewidth=1.0)
plt.xticks([])  # Removing x-axis ticks

# Save the plot as an image file
plt.tight_layout()
# plt.savefig('/mnt/data/gate_vs_wire_impact.png')

# Show the plot
plt.show()
