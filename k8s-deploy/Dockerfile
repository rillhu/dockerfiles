FROM python:3.9
LABEL maintainer="hongfei<hongfei.hu@outlook.com>"
RUN pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY app.py /app/
WORKDIR /app
EXPOSE 5000
CMD ["python", "app.py"]