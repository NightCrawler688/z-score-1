import pandas as pd 
import plotly.figure_factory as ff 
import csv
import random
import plotly.graph_objects as go 
import statistics

df = pd.read_csv('medium_data.csv')
data = df['publication'].tolist()
mean_population = statistics.mean(data)
std_deviation_population = statistics.stdev(data)
# fig = ff.create_distplot([data],['Maths Score'],show_hist=False)
# fig.show()
print('Population mean: ',mean_population)
print('Population Standard deviation: ',std_deviation_population)

def random_set_of_mean(count):
            data_set = []
            for i in range(0,count):
                    random_index = random.randint(0,len(data)- 1)
                    value = data[random_index]
                    data_set.append(value)
            mean = statistics.mean(data_set)
            return mean

mean_list = []
for i in range(0,30):
            setOfMeans = random_set_of_mean(100)
            mean_list.append(setOfMeans)
std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print('Mean: ',mean)
print('Standard deviation: ',std_deviation)

firstStdStart,firstStdEnd = mean - std_deviation,mean + std_deviation
secondStdStart,secondStdEnd = mean - (2 * std_deviation) , mean + (2 * std_deviation)
thirdStdStart,thirdStdEnd = mean - (3 * std_deviation) , mean + (3 * std_deviation)



meanOfSample = statistics.mean(data)
fig = ff.create_distplot([mean_list],['Maths Score'],show_hist=False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.2],mode = 'lines',name = 'MEAN'))
fig.add_trace(go.Scatter(x = [meanOfSample,meanOfSample], y = [0,0.2], mode = 'lines',name = 'Mean of sample3'))
fig.add_trace(go.Scatter(x = [firstStdEnd,firstStdEnd], y = [0,0.2],mode = 'lines',name = 'First standard deviation end'))
fig.add_trace(go.Scatter(x = [secondStdEnd,secondStdEnd], y = [0,0.2],mode = 'lines',name = 'Second standard deviation end'))
fig.add_trace(go.Scatter(x = [thirdStdEnd,thirdStdEnd], y = [0,0.2],mode = 'lines',name = 'Third standard deviation end'))
fig.show()