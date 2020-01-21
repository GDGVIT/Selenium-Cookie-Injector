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


LEVEL = logging.INFO
FORMAT = "{'FileName': 'cookie_injector' ,'DateTime':%(asctime)s, 'LevelName':%(levelname)s, 'Message':%(message)s}"
logging.basicConfig(filename='SeleniumCookies/selenium_cookies.log',
                    filemode='a', level=LEVEL, format=FORMAT, datefmt='%d-%b-%y %H:%M:%S')

cookies = []


def inject_cookie():
    logging.info('Starting to take Cookies')
    _cookiejar = wrapper.load()
    for webname in _cookiejar._cookies:
        for endpoint in _cookiejar._cookies[webname]:
            for processed_cookie in _cookiejar._cookies[webname][endpoint]:
                cookies.append(
                    _cookiejar._cookies[webname][endpoint][processed_cookie].__dict__)
    logging.info(f'{len(cookies)} cookies loaded')
    return cookies


if __name__ == '__main__':
    pass
