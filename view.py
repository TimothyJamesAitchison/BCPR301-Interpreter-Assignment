class View:
    def display(self, list_of_dictionaries):
        for dictionary in list_of_dictionaries:
            for key in dictionary:
                print("{0} = {1}".format(key, dictionary[key]))
import plotly

print(plotly.__version__)  # version >1.9.4 required

"""
plotly.offline.plot({
    "data": [
        Scatter(x=[1, 2, 3, 4], y=[4, 1, 3, 7])
    ],
    "layout": Layout(
        title="hello world"
    )
})
"""

# Learn about API authentication here: https://plot.ly/python/getting-started
# Find your api_key here: https://plot.ly/settings/api

# import plotly.plotly as py
# import plotly.graph_objs as go

fig = {
    'data': [{'labels': ['Sales'],
              'values': [19, 26, 55],
              'type': 'pie'}],
    'layout': {
        'title': 'Forcasted 2014 U.S. PV Installations by Market Segment'}
}

plotly.offline.plot(fig)
