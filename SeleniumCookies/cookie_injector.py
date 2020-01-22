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


def code_message(errorcode):
    # Code mapping
    LoadingFailure = 5001
    JsonParsingError = 5002
    LZ4ParsingError = 5003
    FirefoxCookieNotFound = 4001
    ChromeCookieNotFound = 4002
    CreateCookie = 2001
    LoadCookie = 2002
    LoadFirefoxCookie = 2003
    LoadChromeCookie = 2004

    CodeMap = {
        5001: {'CodeType': 'Error', 'CodeMessage': 'Error in Cookie Loading'},
        5002: {'CodeType': 'Error', 'CodeMessage': 'Error parsing firefox session JSON'},
        5003: {'CodeType': 'Error', 'CodeMessage': 'Error parsing firefox session JSON LZ4'},
        4001: {'CodeType': 'NotFound', 'CodeMessage': 'Failed to find Firefox Cookie'},
        4002: {'CodeType': 'NotFound', 'CodeMessage': 'Failed to find Chrome cookie'},
        2001: {'CodeType': 'Success', 'CodeMessage': 'Creating Cookie'},
        2002: {'CodeType': 'Success', 'CodeMessage': 'Loading Cookie from CookieJar'},
        2003: {'CodeType': 'Success', 'CodeMessage': 'Loading cookie from Firefox'},
        2004: {'CodeType': 'Success', 'CodeMessage': 'Loading cookie from Chrome'},
    }

    return str({
        'Code': errorcode,
        'CodeType': CodeMap.get(errorcode).get('CodeType'),
        'CodeMessage': CodeMap.get(errorcode).get('CodeMessage')
    })


# Change logging Int from here.
LEVEL = logging.INFO
FORMAT = "{'FileName': 'cookie_injector' ,'DateTime':'%(asctime)s', 'LevelName':'%(levelname)s', 'Message':%(message)s}"
logging.basicConfig(filename='SeleniumCookies/selenium_cookies.log',
                    filemode='a', level=LEVEL, format=FORMAT, datefmt='%d-%b-%y %H:%M:%S')

cookies = []


def inject_cookie():
    logging.info(code_message(2002))
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
