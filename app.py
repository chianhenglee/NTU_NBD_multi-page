import dash

#app = dash.Dash()
app = dash.Dash(__name__) # this is needed for adding local CSS files. (in assets folder)
server = app.server
app.config.suppress_callback_exceptions = True


#server.secret_key = os.environ.get('secret_key', 'secret')

