From nginx:latest
RUN echo '<h1>Welcome to Container World！</h1>' > /usr/share/nginx/html/index.html
EXPOSE 80
CMD ["nginx","-g","daemon off;"]