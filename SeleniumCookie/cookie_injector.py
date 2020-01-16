# -*- encoding:utf-8 -*-

from SeleniumCookie import wrapper

__doc__ = 'Process cookies from cookiejar to be injected in selenium'

cookies = []


def inject_cookie():
    _cookiejar = wrapper.load()
    for webname in _cookiejar._cookies:
        for endpoint in _cookiejar._cookies[webname]:
            for processed_cookie in _cookiejar._cookies[webname][endpoint]:
                cookies.append(
                    _cookiejar._cookies[webname][endpoint][processed_cookie].__dict__)
    return cookies


if __name__ == '__main__':
    pass
