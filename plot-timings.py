import plotly.graph_objs as go
from datetime import datetime
import plotly.express as px
import matplotlib as mpl
import seaborn as sns
import pandas as pd
import numpy as np


# sample data in a pandas dataframe

np.random.seed(23)
observations = 75
df=pd.DataFrame(dict(A=np.random.uniform(low=-1, high=1.1, size=observations).tolist(),
                    B=np.random.uniform(low=-1, high=1.1, size=observations).tolist(),
                    C=np.random.uniform(low=-1, high=1.1, size=observations).tolist(),
                    ))
df.iloc[0,] = 0
df = df.cumsum()

firstdate = datetime(2020,1,1)
df['date'] = pd.date_range(firstdate, periods=df.shape[0]).tolist()
df.set_index('date', inplace=True)

px.line(df, x = df.index, y = df.columns)



# fig = go.Figure([{
#     'x': df.index,
#     'y': df[col],
#     'name': col
# }  for col in df.columns])
# fig.show()

#  sns.set_style("darkgrid")
#sns.lineplot(data = df)
