from nvd3 import pieChart
%load_ext rpy2.ipython
xs = %R sort(unique(mtcars$cyl))
ys = %R table(mtcars$cyl)
chart = pieChart(name="Cylinders", color_category='category10', height=500, width=400)
chart.add_serie(x=xs.tolist(), y=ys.tolist())
output_file = open('nvd3-3.html', 'w')
chart.buildhtml()
output_file.write(chart.htmlcontent)
output_file.close()
