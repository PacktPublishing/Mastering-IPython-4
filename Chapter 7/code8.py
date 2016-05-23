from nvd3 import scatterChart
xs = [1, 2, 3, 4, 5]
ys = [2, 3, 5, 7, 11]
kwargs = {'shape': 'circle', 'size': '1'}
chart = scatterChart(name='The first few primes', height=400, width=400)
chart.add_serie(name="Primes", x=xs, y=ys, **kwargs)
output_file = open('nvd3-1.html', 'w')
chart.buildhtml()
output_file.write(chart.htmlcontent)
output_file.close()
