from pyecharts.charts import Line
import os

# Create a Line chart object
line = Line()

# Add x-axis and y-axis data
line.add_xaxis(["China", "America", "England"])
line.add_yaxis("GDP", [30, 20, 10])

# Create the output directory if it doesn't exist
output_dir = os.path.join("Phase 1", "chapter 10")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Specify the file path and file name to save the rendered chart
output_file = os.path.join(output_dir, "line_chart.html")

# Render the chart to the specified path
line.render(output_file)
