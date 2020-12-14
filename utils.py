
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


def draw_lines(x_vals, y_vals):
    """Plot interactive 2D line chart with Plotly.

    Arguments
    ---------
    x_vals: list (floats)
        List of x values
    y_vals: list (floats)
        List of y values
    """

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals,
                             mode='lines+markers',
                             name='lines+markers'))
    fig.show()


def make_2d_points(n=10, max=1):
    """Generate list of random x and y values.

    Arguments
    ---------
    n: integer
        Number of points to generate.
    max: integer
        Upper bound of values.

    Return
    ------
    x: list (floats)
        X values.
    y: list (floats)
        Y values.
    """

    arr = np.random.randn(n, 2) * max
    arr = arr.tolist()
    x = [pair[0] for pair in arr]
    y = [pair[1] for pair in arr]

    return x, y
