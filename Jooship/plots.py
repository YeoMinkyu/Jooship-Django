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


def get_graph():
    _head_title = _make_head_title()
    information_df = _select_fs()
    chart_columns = information_df.columns.values[1:]

    # _table =  generate_table(information_df)

    revenue_figure = get_revenue_figure(information_df, chart_columns)
    cash_flow_figure = get_cash_flow_figure(information_df, chart_columns)

    # figures = tools.make_subplots(rows=2, cols=2)

    plot_div = plot(revenue_figure, output_type='div', include_plotlyjs=False)
    # plot_div = [plot(revenue_figure, output_type='div', include_plotlyjs=False),
    #             plot(cash_flow_figure, output_type='div', include_plotlyjs=False)]
    
    # graph_cash_flow = go.Graph(
    #         id='cash-flow-graph',
    #         figure={
    #             'data': [
    #                 {'x': chart_columns, 'y': information_df.values[7, 1:], 'type': 'bar',
    #                  'name': 'Operating Cash Flow USD'},
    #                 {'x': chart_columns, 'y': information_df.values[8, 1:], 'type': 'bar',
    #                  'name': 'Free Cash Flow USD'}
    #             ],
    #             'layout': [
    #                 {'title': 'Cash Flow Data Visualization'}
    #             ]
    #         }
    #     )

    # graph_yoy = go.Graph(
    #         id='EPS-YoY-graph',
    #         figure={
    #             'data': [go.Bar(x=chart_columns, y=information_df.values[4, 1:], name='Earning Per Share USD'),
    #                      go.Scatter(x=chart_columns, y=information_df.values[10, 1:], name='Revenue YoY %',
    #                                 yaxis='y2'),
    #                      go.Scatter(x=chart_columns, y=information_df.values[11, 1:], name='Operating Income YoY %',
    #                                 yaxis='y2')
    #                      ],
    #             'layout': go.Layout(
    #                 xaxis={'title': 'Year'},
    #                 yaxis={'title': 'EPS USD'},
    #                 yaxis2={'title': 'YoY %', 'overlaying': 'y', 'side': 'right'}
    #             )

    #         }
    #     )

    # graph_dividends = go.Graph(
    #         id='dividends-payout-ratio-graph',
    #         figure={
    #             'data': [go.Bar(x=chart_columns, y=information_df.values[5, 1:], name='Dividends USD'),
    #                      go.Scatter(x=chart_columns, y=information_df.values[6, 1:], name='Payout Ratio %',
    #                                 yaxis='y2')
    #                      ],
    #             'layout': go.Layout(
    #                 xaxis={'title': 'Year'},
    #                 yaxis={'title': 'Dividends USD'},
    #                 yaxis2={'title': 'Payout Ratio %', 'overlaying': 'y', 'side': 'right'}
    #             )
    #         }
    #     )

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