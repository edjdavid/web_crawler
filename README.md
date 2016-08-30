# web_crawler
Scripts for crawling the web

### chrome_cookie.py
Load and use manually copied cookies from the Chrome dev console on the `requests` module.

Sample usage:
```python
req = create_session(load_cookie('test.cookie'))
r = req.get('https://mail.google.com/mail/u/0/#inbox')
print(r.text)
```
To copy cookies from Chrome:
  - Open Chrome browser
  - Login to any website that needs to be crawled
  - F12 -> Application (tab) -> Storage (Cookies) (Left pane) -> Select cookie for website
  - Select any row on the right pane -> Select all (ctrl+a) -> Copy (ctrl+c)
  - Save to any file and replace `test.cookie` on the example.
