* 激活虚拟环境
```

C:\Users\Administrator>D:

D:\>cd Python

D:\Python>cd Flask

D:\Python\Flask>python -m venv venv
Error: [Errno 13] Permission denied: 'D:\\Python\\Flask\\venv\\Scripts\\python.exe'

D:\Python\Flask>python -m venv venv

D:\Python\Flask>venv\Scripts\activate

```

* 运行程序（一共四个程序：3个.py，1个命令行）

```
2,
(venv) D:\Python\Flask\Flask_Web\ch02>python hello_pro.py
 * Serving Flask app "hello_pro" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 991-707-899
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [28/Oct/2019 13:49:45] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [28/Oct/2019 13:49:50] "GET /user/Dave。 HTTP/1.1" 200 -
127.0.0.1 - - [28/Oct/2019 13:49:50] "GET /favicon.ico HTTP/1.1" 404 -
127.0.0.1 - - [28/Oct/2019 13:50:03] "GET /user/张一冰 HTTP/1.1" 200 -

3,获取名称
(venv) D:\Python\Flask\Flask_Web\ch02>python
Python 3.6.4 |Anaconda custom (32-bit)| (default, Jan 16 2018, 10:21:59) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from hello import app
>>> from flask import current_app
>>> current_app.name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "D:\Python\Flask\venv\lib\site-packages\werkzeug\local.py", line 348, in __getattr__
    return getattr(self._get_current_object(), name)
  File "D:\Python\Flask\venv\lib\site-packages\werkzeug\local.py", line 307, in _get_current_object
    return self.__local()
  File "D:\Python\Flask\venv\lib\site-packages\flask\globals.py", line 52, in _find_app
    raise RuntimeError(_app_ctx_err_msg)
RuntimeError: Working outside of application context.

This typically means that you attempted to use functionality that needed
to interface with the current application object in some way. To solve
this, set up an application context with app.app_context().  See the
documentation for more information.
>>> app_ctx = app.app_context()
>>> app_ctx.push()
>>> current_app.name
'hello'
>>> app_ctx.pop()
>>> app.url_map
Map([<Rule '/' (OPTIONS, HEAD, GET) -> index>,
 <Rule '/static/<filename>' (OPTIONS, HEAD, GET) -> static>])

1,
4,使用Flask-Script支持命令行选项

from flask import Flask
app = Flask(__name__)

#from flask.ext.script import Manager
from flask_script import Manager
manager = Manager(app)

'''
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'
''' 
if __name__ == '__main__':
    #app.run(debug=True)
    manager.run()

(venv) D:\Python\Flask\Flask_Web\ch02>python hello.py
usage: hello.py [-?] {shell,runserver} ...

positional arguments:
  {shell,runserver}
    shell            Runs a Python shell inside Flask application context.
    runserver        Runs the Flask development server i.e. app.run()

optional arguments:
  -?, --help         show this help message and exit

```
















