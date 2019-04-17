from .views import add_url, urls, keywords


def setup_routes(app):
    app.router.add_post('/', add_url, name='add_url')
    app.router.add_get('/urls', urls, name='urls_list')
    app.router.add_get('/kw', keywords, name='kw_list')
