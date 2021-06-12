import pandas as p
import plotly.figure_factory as pf
import csv

df = p.read_csv('mobile.csv')
fig = pf.create_distplot([df['Avg Rating'].tolist()], [
                         'Average'], show_hist=False)
fig.show()
