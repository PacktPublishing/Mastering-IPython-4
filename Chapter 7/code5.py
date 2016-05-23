%load_ext rpy2.ipython
from rpy2.robjects import pandas2ri
pandas2ri.activate()
from rpy2.robjects import r
df_cars = pandas2ri.ri2py(r['mtcars'])
type(df_cars)
df_cars.describe()
