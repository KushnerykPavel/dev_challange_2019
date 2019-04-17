import json

from aiohttp.web import Request, Response

from keywords.db import set_url, get_urls, get_keywords
from .services.url_fetcher import UrlFetcher

async def add_url(request):

    if request.method == 'POST':
        data = await request.post()
        urls = data.values()
        async with request.app['db_pool'].acquire() as conn:
            for url in urls:
                uf = UrlFetcher(url)
                print(uf.fetch_url())
                await set_url(conn, url)
                print(url)

    return Response(status=200)


async def urls(request):
    async with request.app['db_pool'].acquire() as conn:
        urls_list = await get_urls(conn)
        print(urls_list)
    return {'urls': urls_list}

async def keywords(request):
    async with request.app['db_pool'].acquire() as conn:
        urls_list = await get_keywords(conn)
        print(urls_list)
    return {'urls': urls_list}
