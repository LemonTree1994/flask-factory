FROM python:3.8.3

ENV TIME_ZONE Asia/Shanghai
ENV env prod

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
EXPOSE 5000
WORKDIR /app
CMD python manage.py runserver --host='0.0.0.0' --port=5000