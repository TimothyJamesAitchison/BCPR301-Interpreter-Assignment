import plotly
import plotly.graph_objs
import pygal

class View:
    def display(self, list_of_dictionaries):
        for dictionary in list_of_dictionaries:
            for key in dictionary:
                print("{0} = {1}".format(key, dictionary[key]))

    def plot_bar(self, data, label):
        values = []
        keys = []
        for employee in data:
            keys.append(employee[0])
            print(employee[0])
            values.append(employee[1])
            print(employee[1])
        chart = {"data": [plotly.graph_objs.Bar(x=keys,y=values)]}
        plotly.offline.plot(chart)

    def plot_pie_gender(self, data):
        males = 0
        females = 0
        others = 0
        for employee in data:
            if employee[1] == "M":
                males += 1
            elif employee[1] == "F":
                females += 1
            else:
                others += 1

        fig = {
            'data': [{'labels': ['Male', 'Female', 'Other'],
                      'values': [males, females, others],
                      'type': 'pie'}],
            'layout': {
                'title': 'Gender diversity in organisation'}
        }

        plotly.offline.plot(fig)
    # hasitha
    def pygal_line_salebased(self,sales,ages):
        data_points = []
        sales = dict(sales)
        ages = dict(ages)
        print(sales)
        print(ages)
        for employee in sales:
            data_point = (ages[employee], sales[employee])
            data_points.append(data_point)
        xy_chart = pygal.XY(stroke=False)
        xy_chart.title = 'Correlction between Sales and Age'
        xy_chart.add('Sales', data_points)
        xy_chart.render_in_browser()

