from plotly.offline import plot

import plotly.graph_objs as go
import pandas as pd
import numpy as np
import os

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
current_dir = os.path.dirname(os.path.realpath(__file__))


file_name = os.path.join(current_dir, 'data', 'TSLA_from_Numbers.csv')

fs = pd.read_csv(
    file_name,
    error_bad_lines=False
)


def select_fs():
    information_rows = [2, 4, 5, 6, 7, 8, 9, 12, 14, 32, 43, 48]
    _information_df = fs.iloc[information_rows]
    new_columns = np.append(np.array(['Year']), fs.iloc[1, 1:].values)
    _information_df.columns = new_columns

    return _information_df


information_df = select_fs()
chart_columns = information_df.columns.values[1:]


# create_table(data_frame):
#     return html.Table(
#         # Header
#         [html.Tr([html.Th(col) for col in data_frame.columns])] +

#         # Body
#         [html.Tr([
#             html.Td(data_frame.iloc[i][col]) for col in data_frame.columns
#         ]) for i in range(min(len(data_frame), data_frame.shape[0]))]
#     )


def get_revenue_plot():
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

    figure = go.Figure(data=revenue_data, layout=revenue_layout)

    plot_div = plot(figure, output_type='div', include_plotlyjs=False)

    return plot_div


def get_cash_flow_plot():
    trace_operating_cash_flow = go.Bar(x= chart_columns, y= information_df.values[7, 1:], name= 'Operating Cash Flow USD')
    trace_free_cash_flow = go.Bar(x= chart_columns, y= information_df.values[8, 1:], name= 'Free Cash Flow USD')

    cash_flow_data = [trace_operating_cash_flow, trace_free_cash_flow]
    cash_flow_layout = go.Layout(title= 'Cash Flow Data Visualization')

    figure =  go.Figure(data=cash_flow_data, layout=cash_flow_layout)

    plot_div = plot(figure, output_type='div', include_plotlyjs=False)

    return plot_div


def get_eps_plot():
    trace_eps = go.Bar(x=chart_columns, y=information_df.values[4, 1:], name='Earning Per Share USD')
    trace_revenue_yoy = go.Scatter(x=chart_columns, y=information_df.values[10, 1:], name='Revenue YoY %', yaxis='y2')
    trace_operating_income_yoy = go.Scatter(x=chart_columns, y=information_df.values[11, 1:], name='Operating Income YoY %', yaxis='y2')

    eps_data = [trace_eps, trace_revenue_yoy, trace_operating_income_yoy]
    eps_layout = go.Layout(xaxis={'title': 'Year'},
                        yaxis={'title': 'USD'},
                        yaxis2={'title': 'Percent %', 'overlaying': 'y', 'side': 'right'},
                        title='EPS Visualization')

    figure = go.Figure(data=eps_data, layout=eps_layout)

    plot_div = plot(figure, output_type='div', include_plotlyjs=False)

    return plot_div


def get_dividends_plot():
    trace_dividends = go.Bar(x=chart_columns, y=information_df.values[5, 1:], name='Dividends USD')
    trace_payout_ratio = go.Scatter(x=chart_columns, y=information_df.values[6, 1:], name='Payout Ratio %', yaxis='y2')

    dividends_data = [trace_dividends, trace_payout_ratio]
    dividends_layout = go.Layout(xaxis={'title': 'Year'},
                        yaxis={'title': 'USD'},
                        yaxis2={'title': 'Percent %', 'overlaying': 'y', 'side': 'right'},
                        title='Dividends Visualization')

    figure = go.Figure(data=dividends_data, layout=dividends_layout)

    plot_div = plot(figure, output_type='div', include_plotlyjs=False)

    return plot_div

# def _make_head_title():
#     _file_name = copy.deepcopy(file_name)
#     _title = _file_name.split('/')[-1]
#     _title = _title.split('_')[0]
#     _title = _title + " Financial Statements"
#     return _title