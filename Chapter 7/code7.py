df_wtVsMpg['cyl'] = df_cars['cyl']
p2 = ggplot2.ggplot(df_wtVsMpg)
p2 = p2 + ggplot2.aes_string(x="mpg", fill="factor(cyl)")
p2 = p2 + ggplot2.geom_histogram( )
p2.plot( )
