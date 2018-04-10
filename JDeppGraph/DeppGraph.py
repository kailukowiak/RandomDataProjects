import pandas as pd
import numpy as np
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, plot, iplot


# Data from here: https://bodyheightweight.com/johnny-depp-love-life/
df = pd.read_csv('data.csv')

# Age of JD:
jdDOB = 1963
df['AgeDiff'] = jdDOB-df.DOB # Difference between JD and SO
print(df)

jdFirst = df.StartOfRelationship.min()-jdDOB
jdLast = df.EndOfRelationship.max()-jdDOB

jdAge = np.arange(jdFirst, jdLast)
X = np.arange(df.StartOfRelationship.min(), df.EndOfRelationship.max())
nrow = df.shape[0]
avgAgeStart = df.StartOfRelationship.mean()


def createTrace():
    traceList = []
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

plot(test)
print(mask)
