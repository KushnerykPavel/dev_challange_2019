from devchallenge.views import add_url


def setup_routes(app):
    app.router.add_get('/', add_url, name='index')
