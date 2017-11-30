#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi

html_body = """
<html>
<body>
<p>당신의 이름은 <span style="font-size:48px"> %s </span> 입니다!</p>
</body>
</html>
"""

form = cgi.FieldStorage()

print("Content-type: text/html")
print(html_body % form['name'].value)
