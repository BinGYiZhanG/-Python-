#### 一个最小的应用

```
(venv) D:\Python\Flask>cd python_prog

(venv) D:\Python\Flask\python_prog>set FLASK_APP=hello.py

(venv) D:\Python\Flask\python_prog>flask run
 * Serving Flask app "hello.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [28/Oct/2019 12:02:41] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [28/Oct/2019 12:02:41] "GET /favicon.ico HTTP/1.1" 404 -
```
* 现在在浏览器中打开 http://127.0.0.1:5000/ ，应该可以看到 Hello World! 字样。
