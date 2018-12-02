import pygal
my_file = open('pychart.txt', 'w')


my_file.write('dogs are better')

print(my_file)
pie_chart = pygal.Pie()
pie_chart.add('Dog', 6)
pie_chart.render_in_browser()
