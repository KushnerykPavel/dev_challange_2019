import aiohttp
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


class UrlFetcher:

    def __init__(self, url):
        self.url = url

    async def fetch_url(self):
        ua = UserAgent()
        headers = {'User-Agent': ua.random, }
        async with aiohttp.ClientSession() as session:
            async with session.get(self.url, headers=headers, timeout=30) as response:
                response = await response.text()
                soup = BeautifulSoup(response, 'html.parser')
                return soup.title.string
