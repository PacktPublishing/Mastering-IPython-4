import numpy as np
import bokeh.plotting as bp
bp.output_file("bokeh2.html")
x = np.linspace(0, 2 * np.pi, 1024)
y = np.cos(x)
fig = bp.figure(title="simple line example", x_axis_label="x", y_axis_label="y")
fig.line(x, y, legend="cos(x)", color="red", line_width=2)
bp.show(fig)
