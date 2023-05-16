import asyncio
import json
from typing import Any, Dict
from urllib.parse import urljoin

from aiohttp import ClientSession


class API:
    def __init__(self, uri: str = 'https://api.gradejs.com'):
        self.uri = uri
        self._session = ClientSession()

    async def _do_request(self, path: str = '/', method: str = 'post', body: Dict[str, Any] | None = None):
        url = urljoin(self.uri, path)
        async with self._session.request(method=method, url=url, json=body) as response:
            decode_data = await response.text()
            try:
                data = json.loads(decode_data)
            except ValueError as e:
                return decode_data
        return data

    async def ping(self):
        '''
        Checking the server and the API.
        '''
        return await self._do_request(method='get')

    async def getOrRequestWebPageScan(self, url: str, rescan: bool = False, batch: int = 1):
        '''
        Getting information about a web page `url`
        '''
        body = {
            "0": {
                "url": url,
                "rescan": rescan
            }
        }
        return await self._do_request(
            path=f'/client/getOrRequestWebPageScan?batch={batch}',
            method='post',
            body=body
        )

    async def getPackageInfo(self, package: str, batch: int = 1):
        '''
        Getting information about the `package`
        '''
        return await self._do_request(
            path=f'/client/getPackageInfo?batch={batch}&input=%7B%220%22%3A%7B%22packageName%22%3A%22{package}%22%7D%7D',
            method='get'
        )

    async def getShowcase(self):
        return await self._do_request(
            path=f'/client/getShowcase',
            method='get'
        )

    async def close(self) -> None:
        '''
        Closing of the session `aiohttp.ClientSession`
        '''
        if not self._session.closed:
            await self._session.close()


async def main():
    url_example = 'https://github.com/'
    package_example = 'axios'
    api = API('https://api.gradejs.com')
    print(f'Ping: {await api.ping()}\n')
    print(f'URL Scan: {await api.getOrRequestWebPageScan(url_example)}\n')
    print(f'Package Scan: {await api.getPackageInfo(package_example)}\n')
    print(f'getShowcase: {await api.getShowcase()}')
    await api.close()


if __name__ == '__main__':
    asyncio.run(main())
