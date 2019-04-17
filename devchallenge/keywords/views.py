import json

from aiohttp.web import Request, Response


async def add_url(request):
    print(request)
    return Response(status=200, body='', content_type='application/json')