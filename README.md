# gradejs-py-api

Asyncio micro-library for working with [GradeJS](https://github.com/gradejs/gradejs).

- [gradejs-py-api](#gradejs-py-api)
  - [1. Dependencies](#1-dependencies)
  - [2. Usage example](#2-usage-example)

## 1. Dependencies

- [`aiohttp` 3.8 or never](https://pypi.org/project/aiohttp/);
- [Python 3.7 or newer](https://www.python.org/).

## 2. Usage example

```python
import asyncio

from gradejs_py_api import API


async def main():
    url_example = 'https://github.com/'
    package_example = 'axios'
    api = API('https://api.gradejs.com')
    print(f'Ping: {await api.ping()}\n')
    print(f'URL Scan: {await api.getOrRequestWebPageScan(url_example)}\n')
    print(f'Package Scan: {await api.getPackageInfo(package_example)}\n')
    print(f'getShowcase: {await api.getShowcase()}')
    await api.close()  # Mandatory closure of the session `aiohttp.ClientSession` if you no longer need it


if __name__ == '__main__':
    asyncio.run(main())
```
