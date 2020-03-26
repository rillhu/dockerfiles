# docker-files



## nginx

```
PS C:\Users\hongf\Documents\03_Git\docker-nginx> docker build -t nginx:v1 .
PS C:\Users\hongf\Documents\03_Git\docker-nginx> docker run -it -p 80:80 --name mylocalnginx nginx:v1
172.17.0.1 - - [25/Mar/2020:02:40:28 +0000] "GET / HTTP/1.1" 200 42 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36 Edg/80.0.361.6
9" "-"
```

In browser input access: http://127.0.0.1/



## python-flask

```
PS C:\Users\hongf\Documents\03_Git\docker-python-flask> docker build -t flask:v1 .
PS C:\Users\hongf\Documents\03_Git\docker-python-flask> docker run -p 5000:5000 --name localflask flask:v1
* Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
172.17.0.1 - - [25/Mar/2020 03:14:33] "GET / HTTP/1.1" 200 -
```

In browser access: http://127.0.0.1:5000/

