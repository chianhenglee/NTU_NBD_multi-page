import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
#from apps import app1, app2
from apps import choropleth, lineplots


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content',
             children=[
                html.H3('This is the index page!'),
                #html.H4(dcc.Link('Line plots', href='/apps/lineplots')),
                #html.H4(dcc.Link('Choropleth', href='/apps/choropleth')),
                #html.H4(dcc.Link('Treemaps', href='/apps/treemaps')),
                #html.H4(dcc.Link('Subplots', href='/apps/subplots'))
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
    elif pathname =='/':
        return html.Div([
                #dcc.Location(id='url', refresh=False),
                html.Div([
                    html.H3('This is the index page!!'),
                    html.H4(dcc.Link('Line plots', href='/apps/lineplots')),
                    html.H4(dcc.Link('Choropleth', href='/apps/choropleth')),
                          ]),
                ])

if __name__ == '__main__':
    app.run_server(debug=True)




