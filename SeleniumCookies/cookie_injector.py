# -*- coding:utf-8 -*-

import logging

# external imports
try:
    from SeleniumCookies import wrapper
except:
    import wrapper

__doc__ = 'Process cookies from cookiejar to be injected in selenium'

# Clearning older logs if any
try:
    with open('SeleniumCookies/selenium_cookies.log', 'w') as clear_logs:
        pass
except:
    pass

LoadingFailure = 5001
FirefoxCookieNotFound = 4001
ChromeCookieNotFound = 4002
JsonParsingError = 5002
LZ4ParsingError = 5003
CreateCookie = 2001
LoadCookie = 2002
LoadFirefoxCookie = 2003
LoadChromeCookie = 2004


CodeMap = {
    5001: 'Error in Cookie Loading',
    5002: 'Error parsing firefox session JSON',
    5003: 'Error parsing firefox session JSON LZ4',
    4001: 'Failed to find Firefox Cookie',
    4002: 'Failed to find Chrome cookie',
    2001: 'Creating Cookie',
    2002: 'Loading Cookie from CookieJar',
    2003: 'Loading cookie from Firefox',
    2004: 'Loading cookie from Chrome'

}


LEVEL = logging.INFO
FORMAT = "{'FileName': 'cookie_injector' ,'DateTime':'%(asctime)s', 'LevelName':'%(levelname)s', 'Message':%(message)s}"
logging.basicConfig(filename='SeleniumCookies/selenium_cookies.log',
                    filemode='a', level=LEVEL, format=FORMAT, datefmt='%d-%b-%y %H:%M:%S')

cookies = []


def inject_cookie():
    logging.info("{'StatusCode':'%s' ,'Status':'%s'}",
                 LoadCookie, CodeMap[LoadCookie])
    _cookiejar = wrapper.load()
    for webname in _cookiejar._cookies:
        for endpoint in _cookiejar._cookies[webname]:
            for processed_cookie in _cookiejar._cookies[webname][endpoint]:
                cookies.append(
                    _cookiejar._cookies[webname][endpoint][processed_cookie].__dict__)
    logging.info(
        "{'StatusCode':'%s', 'Status':'%s cookies loaded'}", 2000, len(cookies))
    return cookies


if __name__ == '__main__':
    pass
