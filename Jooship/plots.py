from plotly.offline import plot
from plotly import tools

import plotly.graph_objs as go
import pandas as pd
import numpy as np
import copy
import os

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
current_dir = os.path.dirname(os.path.realpath(__file__))


file_name = os.path.join(current_dir,'data','FB_from_Numbers.csv')

fs = pd.read_csv(
    file_name,
    error_bad_lines=False
)

# def generate_table(data_frame):
#     return html.Table(
#         # Header
#         [html.Tr([html.Th(col) for col in data_frame.columns])] +

#         # Body
#         [html.Tr([
#             html.Td(data_frame.iloc[i][col]) for col in data_frame.columns
#         ]) for i in range(min(len(data_frame), data_frame.shape[0]))]
#     )
def get_revenue_figure(information_df, chart_columns):
    
    trace_revenue = go.Bar(x=chart_columns, y= information_df.values[0, 1:], name= 'Revenue USD')
    trace_operating_income = go.Bar(x=chart_columns, y= information_df.values[1, 1:], name= 'Operating Income')
    trace_net_income = go.Bar(x=chart_columns, y=information_df.values[3, 1:], name='Net Income')
    trace_operating_margin = go.Scatter(x=chart_columns, y=information_df.values[2, 1:], name='Operating Margin %', yaxis='y2')
    trace_net_margin = go.Scatter(x=chart_columns, y=information_df.values[9, 1:], name='Net Margin %', yaxis='y2')

    revenue_data = [trace_revenue, trace_operating_income, trace_net_income, trace_operating_margin, trace_net_margin]
    revenue_layout = go.Layout(xaxis={'title': 'Year'},
                        yaxis={'title': 'USD'},
                        yaxis2={'title': 'Percent %', 'overlaying': 'y', 'side': 'right'},
                        title='Revenue Data Visualization')

    return go.Figure(data=revenue_data, layout=revenue_layout)

def get_cash_flow_figure(information_df, chart_columns):
    trace_operating_cash_flow = go.Bar(x= chart_columns, y= information_df.values[7, 1:], name= 'Operating Cash Flow USD')
    trace_free_cash_flow = go.Bar(x= chart_columns, y= information_df.values[8, 1:], name= 'Free Cash Flow USD')

    cash_flow_data = [trace_operating_cash_flow, trace_free_cash_flow]
    cash_flow_layout = go.Layout(title= 'Cash Flow Data Visualization')

    return go.Figure(data=cash_flow_data, layout=cash_flow_layout)

def customize_subplot(information_df, chart_columns):

    ##########################################################################################################################
    trace_revenue = go.Bar(x=chart_columns, y= information_df.values[0, 1:], name= 'Revenue USD')
    trace_operating_income = go.Bar(x=chart_columns, y= information_df.values[1, 1:], name= 'Operating Income')
    trace_net_income = go.Bar(x=chart_columns, y=information_df.values[3, 1:], name='Net Income')
    trace_operating_margin = go.Scatter(x=chart_columns, y=information_df.values[2, 1:], name='Operating Margin %')
    trace_net_margin = go.Scatter(x=chart_columns, y=information_df.values[9, 1:], name='Net Margin %')

    trace_operating_cash_flow = go.Bar(x= chart_columns, y= information_df.values[7, 1:], name= 'Operating Cash Flow USD')
    trace_free_cash_flow = go.Bar(x= chart_columns, y= information_df.values[8, 1:], name= 'Free Cash Flow USD')

    trace_eps = go.Bar(x=chart_columns, y=information_df.values[4, 1:], name='Earning Per Share USD')
    trace_revenue_yoy = go.Scatter(x=chart_columns, y=information_df.values[10, 1:], name='Revenue YoY %')
    trace_operating_income_yoy = go.Scatter(x=chart_columns, y=information_df.values[11, 1:], name='Operating Income YoY %')

    trace_dividends = go.Bar(x=chart_columns, y=information_df.values[5, 1:], name='Dividends USD')
    trace_payout_ratio = go.Scatter(x=chart_columns, y=information_df.values[6, 1:], name='Payout Ratio %', yaxis='y2')

    figure = tools.make_subplots(rows=2, cols=2, horizontal_spacing=0.18, subplot_titles=('Revenue', 'Cash Flow','EPS','Dividends'))

    figure.append_trace(trace_revenue, 1, 1)            # 0
    figure.append_trace(trace_operating_income, 1, 1)   # 1
    figure.append_trace(trace_net_income, 1, 1)         # 2
    figure.append_trace(trace_operating_margin, 1, 1)   # 3
    figure.append_trace(trace_net_margin, 1, 1)         # 4

    figure.append_trace(trace_operating_cash_flow, 1, 2)  # 5
    figure.append_trace(trace_free_cash_flow, 1, 2)       # 6

    figure.append_trace(trace_eps, 2, 1)              # 7
    figure.append_trace(trace_revenue_yoy, 2, 1)       # 8
    figure.append_trace(trace_operating_income_yoy, 2, 1) # 9

    figure.append_trace(trace_dividends, 2, 2)
    figure.append_trace(trace_payout_ratio, 2, 2)

    ##########################################################################################################################

    figure['data'][3].update(yaxis='y5')  # data[3] : trace_operating_margin
    figure['data'][4].update(yaxis='y5')  # data[4] : trace_net_margin

    figure['data'][8].update(yaxis='y7')  # data[8] : trace_revenue_yoy
    figure['data'][9].update(yaxis='y7')  # data[9] : trace_operating_income_yoy

    figure['data'][11].update(yaxis='y8')

    figure['layout']['yaxis1'].update(title='y1')
    figure['layout']['yaxis2'].update(title='y2')
    figure['layout']['yaxis3'].update(title='y3')
    figure['layout']['yaxis5'] = dict(title='y5', anchor='x1', side='right',  showgrid=False, overlaying='y')
    figure['layout']['yaxis6'] = dict(title='y6', anchor='x2', side='right',  showgrid=False, overlaying='y2')
    figure['layout']['yaxis7'] = dict(title='y7', anchor='x3', side='right',  showgrid=False, overlaying='y3')
    figure['layout']['yaxis8'] = dict(title='y8', anchor='x4', side='right',  showgrid=False, overlaying='y4')

    ##########################################################################################################################

    return figure


def get_graph():
    _head_title = _make_head_title()
    information_df = _select_fs()
    chart_columns = information_df.columns.values[1:]

    # _table =  generate_table(information_df)


    figures = customize_subplot(information_df, chart_columns)

    plot_div = plot(figures, output_type='div', include_plotlyjs=False)

    return plot_div

def _make_head_title():
    _file_name = copy.deepcopy(file_name)
    _title = _file_name.split('/')[-1]
    _title = _title.split('_')[0]
    _title = _title + " Financial Statements"
    return _title


def _select_fs():
    information_rows = [2, 4, 5, 6, 7, 8, 9, 12, 14, 32, 43, 48]
    information_df = fs.iloc[information_rows]
    new_columns = np.append(np.array(['Year']), fs.iloc[1, 1:].values)
    information_df.columns = new_columns

    return information_df