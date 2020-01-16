<p align="center">
	<img src="https://user-images.githubusercontent.com/30529572/72455010-fb38d400-37e7-11ea-9c1e-8cdeb5f5906e.png" />
	<h2 align="center"> Selenium Cookie Injector </h2>
	<h4 align="center"> Inserts Cookie from your all other web browsers into the selenium. It may include session ids, tokens etc. <h4>
</p>

---





<br>


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
[![DOCS](https://img.shields.io/badge/HelpersGuide-see%20help-green?style=flat-square&logo=appveyor)](https://github.com/D-E-F-E-A-T/Selenium-Cookie-Injector/blob/master/helpers.md)

<br>

## Functionalities
- [x] Cookie adding from other Browsers cookie
- [ ] Explicit and Selected Cookie Addition

<br>


## Contributors

* [ Angad ](https://github.com/L04DB4L4NC3R)
* [ Ubaid ](https://github.com/Geek-ubaid/)
* [ Kush ](https://github.com/D-E-F-E-A-T/)


<br>
<br>

<p align="center">
	Made with :heart: by DSC VIT
</p>

