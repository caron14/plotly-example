import numpy as np
import plotly.graph_objects as go
import matplotlib.pyplot as plt



"""dataset for 3d scatter"""
x=np.random.rand(10)
y=np.random.rand(10)
z=np.random.rand(10)
"""Create an object for 3d scatter"""
trace1 = go.Scatter3d(
    x=x, y=y, z=z,
    mode='markers',
    marker=dict(
        size=5,
        color=y,
        colorscale='Viridis')
)
"""Create dataset for a surface"""
mesh_size = .02
xrange = np.arange(0, 1, mesh_size)
yrange = np.arange(0, 1, mesh_size)
xx, yy = np.meshgrid(xrange, yrange)
z = np.ones(xx.shape)*0.5
"""Create an object for a surface"""
surf1 = go.Surface(
    x=xrange, y=yrange, z=z,
    opacity = 0.2,
)
"""Create an object for graph layout"""
layout={
    'xaxis': {'range': [0, 1], 'dtick':0.1},
    'yaxis': {'range': [0, 1], 'dtick':0.1},
    'title': 'This is the title',
    # 'margin':go.layout.Margin(l=50, r=50, b=50, t=50, pad=50)
}
fig = go.Figure(data=[trace1], layout=layout)
fig.add_traces(surf1)
fig.show()








