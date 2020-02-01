<p align="center">
	<img src="https://user-images.githubusercontent.com/30529572/72455010-fb38d400-37e7-11ea-9c1e-8cdeb5f5906e.png" />
	<h2 align="center"> Selenium Cookie Injector </h2>
	<h4 align="center"> Inserts Cookie from your all other web browsers into the selenium. It may include session ids, tokens etc. <h4>
</p>
<p align="center">
	<a align="center" href="https://pypi.org/project/SeleniumCookies"><img src="https://badge.fury.io/py/SeleniumCookies.svg" alt="PyPI version"></a>
</p>

---
<br>

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) [![ForTheBadge built-with-swag](http://ForTheBadge.com/images/badges/built-with-swag.svg)](https://GitHub.com/D-E-F-E-A-T/) [![4U](https://forthebadge.com/images/badges/for-you.svg)](https://github.com/GDGVIT/)
</br>
[![GitHub stars](https://img.shields.io/github/stars/GDGVIT/Selenium-Cookie-Injector.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/GDGVIT/Selenium-Cookie-Injector/stargazers/)[![GitHub followers](https://img.shields.io/github/followers/D-E-F-E-A-T.svg?style=social&label=Follow&maxAge=2592000)](https://github.com/D-E-F-E-A-T?tab=followers)
[![GitHub repo size](https://img.shields.io/github/repo-size/GDGVIT/Selenium-Cookie-Injector.svg?logo=git&style=social)](https://github.com/GDGVIT/) [![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/GDGVIT/Selenium-Cookie-Injector.svg?logo=python&style=social)](https://github.com/GDGVIT/Selenium-Cookie-Injector)
 [![GitHub last commit](https://img.shields.io/github/last-commit/GDGVIT/Selenium-Cookie-Injector.svg?color=critical&logo=github&style=social)](https://github.com/GDGVIT/Selenium-Cookie-Injector/) [![GitHub contributors](https://img.shields.io/github/contributors/GDGVIT/Selenium-Cookie-Injector.svg)](https://GitHub.com/GDGVIT/Selenium-Cookie-Injector/graphs/contributors/) [![Open Source Love png3](https://badges.frapsoft.com/os/v3/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
 </br>
 [![GitHub issues](https://img.shields.io/github/issues/GDGVIT/Selenium-Cookie-Injector.svg)](https://GitHub.com/GDGVIT/Selenium-Cookie-Injector/issues/) [![GitHub issues-closed](https://img.shields.io/github/issues-closed/GDGVIT/Selenium-Cookie-Injector.svg)](https://GitHub.com/GDGVIT/Selenium-Cookie-Injector/issues?q=is%3Aissue+is%3Aclosed)
</br>
[![GitHub pull-requests](https://img.shields.io/github/issues-pr/GDGVIT/Selenium-Cookie-Injector.svg)](https://GitHub.com/GDGVIT/Selenium-Cookie-Injector/pull/) [![GitHub pull-requests closed](https://img.shields.io/github/issues-pr-closed/GDGVIT/Selenium-Cookie-Injector.svg)](https://GitHub.com/GDGVIT/Selenium-Cookie-Injector/pull/)
</br>
[![License](http://img.shields.io/:license-mit-blue.svg?style=flat-square)](http://badges.mit-license.org)
[![HitCount](http://hits.dwyl.io/D-E-F-E-A-T/Selenium-Cookie-Injector.svg)](http://hits.dwyl.io/D-E-F-E-A-T/Selenium-Cookie-Injector)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/GDGVIT/Selenium-Cookie-Injector)

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
from SeleniumCookies import cookie_injector

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
- [ ATechnoHazard ](https://github.com/ATechnoHazard)

<br>
<br>

<p align="center">
	Made with :heart: by DSC VIT
</p>

[![saythanks](https://img.shields.io/badge/say-thanks-ff69b4.svg)](https://github.com/D-E-F-E-A-T) 
[![LinkedIn](https://img.shields.io/static/v1.svg?label=Connect&message=@Kush&color=grey&logo=linkedin&labelColor=blue&style=social)](https://www.linkedin.com/in/kush-choudhary-567b38169?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BDYkgbUGhTniMSRqOUkdN3A%3D%3D) [![Instagram](https://img.shields.io/badge/Instagram-follow-yellow.svg?logo=instagram&logoColor=white)](https://www.instagram.com/kush.philosopher/)
