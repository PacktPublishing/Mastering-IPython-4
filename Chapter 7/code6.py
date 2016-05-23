%load_ext rpy2.ipython
from rpy2.robjects import pandas2ri
pandas2ri.activate()
from rpy2.robjects import r
import pandas
from rpy2.robjects.lib import ggplot2
df_cars = pandas2ri.ri2py(r['mtcars'])
wt = df_cars['wt']
mpg = df_cars['mpg']
type(mpg)
df_wtVsMpg = pandas.DataFrame()
df_wtVsMpg['wt'] = wt
df_wtVsMpg['mpg'] = mpg
p = ggplot2.ggplot(df_wtVsMpg)
type(p)
p.plot()
