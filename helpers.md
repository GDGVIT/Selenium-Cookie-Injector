## Whatsapp AutoLogin after one-time QR-Scan
```bash
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome('cdr/chromedriver', options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data")
url = 'https://web.whatsapp.com/'
driver.get(url)
```


## Instructions to run

* directions to install
```bash
pip install SeleniumCookie==0.1
```

* directions to execute

```bash
from selenium import webdriver
from SeleniumCookie import cookie_injector

driver = webdriver.Chrome('cdr/chromedriver')
driver.get("https://www.google.com")

#COOKIE INJECTION
cookies = cookie_injector.inject_cookie()
for cookie in cookies:
	try:
		driver.add_cookie(cookie)
	except:
		pass
```
