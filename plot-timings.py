import plotly.graph_objs as go
from datetime import datetime
import plotly.express as px
import matplotlib as mpl
import seaborn as sns
import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

plt.style.use('seaborn')

# read timings data from sco3002
# REF: https://towardsdatascience.com/4-tricks-you-should-know-to-parse-date-columns-with-pandas-read-csv-27355bb2ad0e
custom_date_parser = lambda x: datetime.strptime(x, "%d/%m/%Y %H:%M:%S %Z")

df_sco = pd.read_csv('sco3002-timings.txt',
                #index_col='start_date',
                parse_dates=['start_date'],
                date_parser=custom_date_parser)
df_sco['host'] = 'sco3002'
df_sco['color'] = 'red'

# read timings data from axon
df_axon = pd.read_csv('axon-timings.txt',
                #index_col='start_date',
                parse_dates=['start_date'],
                date_parser=custom_date_parser)
df_axon['host'] = 'axon'
df_axon['color'] = 'green'

# read timings data from soma
df_soma = pd.read_csv('soma-timings.txt',
                #index_col='start_date',
                parse_dates=['start_date'],
                date_parser=custom_date_parser)
df_soma['host'] = 'soma'
df_soma['color'] = 'blue'

# Concatenate and sort data from all three hosts
df_all = pd.concat([df_sco, df_axon, df_soma])
#df_all.set_index('start_date', inplace=True)
df_all.info()
print(df_all)

# Sorting values by start_date (inplace)
df_all.sort_values('start_date', inplace=True)
print(df_all)

# Plotting scatter plots using seaborn
# REF:  https://stackoverflow.com/questions/14885895/color-by-column-values-in-matplotlib
#sns.set(style='ticks')
host_order = ['sco3002', 'axon', 'soma']
g = sns.relplot(data=df_all, x='start_date', y='elapsed_time(s)', hue='host', hue_order=host_order)
g._legend.remove()
# REF: https://stackoverflow.com/questions/4700614/how-to-put-the-legend-outside-the-plot-in-matplotlib
plt.gca().legend(loc='center left', title='Host',
                bbox_to_anchor=(1.05, 0.5),
                fancybox=True, shadow=True,
                fontsize=14, title_fontsize=16)
plt.gca().set_xlabel('start date', fontsize=16)
plt.gca().set_ylabel('elapsed time\n(seconds)', fontsize=16)
plt.gca().set_title('Installing ISF python environment (Anaconda2)',
    fontdict= {'fontsize': 16, 'fontweight': 'bold'})
date_format = mpl_dates.DateFormatter('%d. %b %Hh')
plt.gca().xaxis.set_major_formatter(date_format) # format the dates in plot
plt.gcf().autofmt_xdate() # rotate the dates
plt.tight_layout() # add padding to the plot
plt.savefig("install-isf-benchmark.png", bbox_inches="tight")
plt.show() # plt.show() should come after plt.savefig()


# ### Creating scatter plot using matplotlib
# plt.gca().scatter(data=df_all, x='start_date', y='elapsed_time(s)', c='color', label='host')
# plt.gcf().autofmt_xdate() # rotate the dates

# #date_format = mpl_dates.DateFormatter('%d. %b %H:%M')
# date_format = mpl_dates.DateFormatter('%d. %b %Hh')
# plt.gca().xaxis.set_major_formatter(date_format) # format the dates in plot

# plt.tight_layout() # add padding to the plot
# plt.show()
