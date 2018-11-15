import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
#from apps import app1, app2
from apps import choropleth, lineplots, hospital_data_visual2


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content',
             children=[
                html.H3('This is the index page!'),
                #html.H4(dcc.Link('Line plots', href='/apps/lineplots')),
                #html.H4(dcc.Link('Choropleth', href='/apps/choropleth')),
                #html.H4(dcc.Link('Treemaps', href='/apps/treemaps')),
                #html.H4(dcc.Link('Subplots', href='/apps/subplots'))
                html.H4(dcc.Link('hospital_data_visual2', href='/apps/hospital_data_visual2'))
                      ]),
])



@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    print(pathname)
    if pathname == '/apps/lineplots':
        return lineplots.layout
    elif pathname == '/apps/choropleth':
        return choropleth.layout
    elif pathname =='apps/hospital_data_visual2':
        return hospital_data_visual2.layout
    elif pathname =='/':
        return html.Div([
                #dcc.Location(id='url', refresh=False),
                html.Div([
                    html.H3('This is the index page!!'),
                    html.H4(dcc.Link('Line plots', href='/apps/lineplots')),
                    html.H4(dcc.Link('Choropleth', href='/apps/choropleth')),
                    html.H4(dcc.Link('Hospital_data_visual', href='/apps/hospital_data_visual2'))
                          ]),
                ])

if __name__ == '__main__':
    app.run_server(debug=True)




