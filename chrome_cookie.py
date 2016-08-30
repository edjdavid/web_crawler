import requests
import pytz
import calendar

from datetime import datetime
from http.cookiejar import CookieJar, Cookie


def load_cookie(loc):
    cj = CookieJar()
    with open(loc, 'r') as f:
        for line in f.readlines():
            l = line.strip('\n').split('\t')

            while len(l) < 9:
                l.append(None)
            try:
                expires = (pytz.utc.localize(
                    datetime.strptime(l[4], '%Y-%m-%dT%H:%M:%S.%fZ')))
                expires = calendar.timegm(expires.utctimetuple())
            except ValueError:
                expires = None

            ck = Cookie(name=l[0],
                        value=l[1],
                        domain=l[2],
                        path=l[3],
                        secure='✓' == l[7],
                        rest={'HttpOnly': '✓' == l[6]},
                        version=0,
                        port=None,
                        port_specified=False,
                        domain_specified=False,
                        domain_initial_dot=False,
                        path_specified=True,
                        expires=expires,
                        discard=True,
                        comment=None, comment_url=None, rfc2109=False)
            cj.set_cookie(ck)
    return cj


def create_session(cookie_jar):
    req = requests.Session()
    req.cookies = cookie_jar
    return req

if __name__ == '__main__':
    req_sess = create_session(load_cookie('test.cookie'))
    r = req_sess.get('https://mail.google.com/mail/u/0/#inbox')
    print(r.status_code)
    with open('out.html', 'w', encoding='utf8') as f:
        f.write(r.text)
    print('Done!')
