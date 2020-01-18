<p align="center">
	<img src="https://user-images.githubusercontent.com/30529572/72455010-fb38d400-37e7-11ea-9c1e-8cdeb5f5906e.png" />
	<h2 align="center"> Selenium Cookie Injector </h2>
	<h4 align="center"> Inserts Cookie from your all other web browsers into the selenium. It may include session ids, tokens etc. <h4>
</p>

---

<br>

## Functionalities

- [x] Cookie adding from other Browsers cookie
- [ ] Explicit and Selected Cookie Addition
- [ ] Passwords Addition from other Browsers to Selenium Browser

<br>

## Instructions to run

- directions to install

```bash
pip install SeleniumCookie==0.2
```

- directions to execute

```python
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

## Test

- Whatsapp AutoLogin after one-time QR-Scan

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=chrome-data")
driver = webdriver.Chrome('cdr/chromedriver', options=chrome_options)
chrome_options.add_argument("user-data-dir=chrome-data")
url = 'https://web.whatsapp.com/'
driver.get(url)
```

- Checking for added Cookies

      	- Run the above script
      	- Now in Chrome Search Bar: chrome://settings/siteData
      	- Added Cookies can be seen now
      	- Additon of cookie subject to it's various parameters and data it has
      	- In my test 279 (119 websites) cookies were injected and 2924 were rejected

</br>

> [Chromedriver Download](https://chromedriver.chromium.org/downloads)

</br>

## Contributors

- [ Angad ](https://github.com/L04DB4L4NC3R)
- [ Ubaid ](https://github.com/Geek-ubaid/)
- [ Kush ](https://github.com/D-E-F-E-A-T/)

<br>
<br>

<p align="center">
	Made with :heart: by DSC VIT
</p>
