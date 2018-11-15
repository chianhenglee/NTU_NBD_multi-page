

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import plotly.graph_objs as go
import pandas as pd
import numpy as np

from app import app



layout = html.Div([
    html.H1('Test: this should be hospital_data_visual page.')
])