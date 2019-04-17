from aiohttp import web
from keywords.routes import setup_routes


async def init_app():

    app = web.Application()

    setup_routes(app)

    return app


def main():
    app = init_app()
    web.run_app(app)


if __name__ == '__main__':
    main()
