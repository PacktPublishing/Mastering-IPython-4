from nvd3 import scatterChart
%load_ext rpy2.ipython
from rpy2.robjects import pandas2ri
pandas2ri.activate()
from rpy2.robjects import r
import pandas
df_cars = pandas2ri.ri2py(r['mtcars'])
wt = df_cars['wt']
mpg = df_cars['mpg']
kwargs = {'shape': 'circle', 'size': '1'}
chart = scatterChart(name='Weight vs MPG', height=400, width=800, y_axis_scale_min='0', show_legend='False')
chart.add_serie(name="Cars", x=wt, y=mpg, **kwargs)
output_file = open('nvd3-2.html', 'w')
chart.buildhtml()
output_file.write(chart.htmlcontent)
output_file.close()
