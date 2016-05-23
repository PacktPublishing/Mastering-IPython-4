import numpy as np
import bokeh.plotting as bp
import bokeh.models as bm
bp.output_file("bokeh4.html")
x = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y0 = np.cos(x)
y1 = np.sin(x)
mySource = bm.ColumnDataSource(data=dict(x=x, y0=y0, y1=y1))
myTools = "box_select,lasso_select,help"
left = bp.figure(tools=myTools, width=300, height=300, title="Left")
left.circle('x', 'y0', source=mySource)
right = bp.figure(tools=myTools, width=300, height=300, title="Right")
right.circle('x', 'y1', source=mySource)
p = bp.gridplot([[left, right]])
bp.show(p)
