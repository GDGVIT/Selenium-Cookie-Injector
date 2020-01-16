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

</br>

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
</br>

## Testing
* Run the above script
* Now in Chrome Search Bar: chrome://settings/siteData
* Added Cookies can be seen now
* Additon of cookie subject to it's various parameters and data it has
* In my test 279 (119 websites) cookies were injected and 2924 were rejected

</br>

## Some Screenshots


![image](https://user-images.githubusercontent.com/41824020/72541165-07846600-38a8-11ea-8d45-88baf4e37513.png)

![image](https://user-images.githubusercontent.com/41824020/72541203-1c60f980-38a8-11ea-887e-32829cb7b091.png)

![image](https://user-images.githubusercontent.com/41824020/72541410-7bbf0980-38a8-11ea-8436-d381aeb021d7.png)

![image](https://user-images.githubusercontent.com/41824020/72541445-8bd6e900-38a8-11ea-8cc9-65d84aea5fa6.png)

