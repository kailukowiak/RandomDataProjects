import pandas as pd
import numpy as np
import plotly.graph_objs as go
#from plotly.offline import plot
import config
import plotly
import plotly.plotly as py


# user name setup
#plotly.tools.set_credentials_file(username='kaiser_xc', api_key='rn4jGIeqkYc4oCOM7ge3')
plotly.tools.set_credentials_file(username=config.user_name, api_key=config.api_key)
# Data from here: https://bodyheightweight.com/johnny-depp-love-life/
df = pd.read_csv('data.csv')

# Age of JD:
jdDOB = 1963
df['AgeDiff'] = jdDOB-df.DOB # Difference between JD and SO
print(df)

jdFirst = df.StartOfRelationship.min()-jdDOB
jdLast = df.EndOfRelationship.max()-jdDOB+1

jdAge = np.arange(jdFirst, jdLast)
X = np.arange(df.StartOfRelationship.min(), df.EndOfRelationship.max()+1)
nrow = df.shape[0]
avgAgeStart = df.StartOfRelationship.mean()


def createTrace():
    traceList = []
    halfPlus7 = go.Scatter(
        x=X,
        y=jdAge/2+7,
        name='Half His Age Plus 7y',
        fill="tozeroy",
        line=dict(color=('rgb(205, 12, 24)')))
    traceList.append(halfPlus7)
    for i in range(df.shape[0]):
        tempDF = df.iloc[i]
        soAgeDiff = tempDF.AgeDiff
        soAge = jdAge+soAgeDiff
        mask = np.where(np.logical_or(X<tempDF.StartOfRelationship,
                                      X>tempDF.EndOfRelationship),
                        None, soAge)
        trace = go.Scatter(
            x=X,
            y=mask,
            name=tempDF.Name,
        )
        traceList.append(trace)
    traceJD = go.Scatter(
        x=X,
        y=jdAge,
        name='Johnny Depp',
    )
    traceList.append(traceJD)

    return traceList
        
test = createTrace()

layout=go.Layout(title="Jonny Depp's Significant Others",
                 xaxis= dict(title='Year',
                             fixedrange=True),
                 yaxis=dict(title='Age',
                            fixedrange=True),
                 autosize=False,
                 width=1000,
                 height=600,)
                 
figurePlot = go.Figure(data=test, layout=layout)
py.plot(figurePlot, filename = "Johnny-Depps-Love-Interests")
#print(mask)
