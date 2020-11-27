FROM python:3.8.3

ENV env prod

COPY requirements.txt /tmp/requirements.txt
RUN /bin/cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && \
    echo 'Asia/Shanghai' >/etc/timezone && \
    pip install -r /tmp/requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

WORKDIR /app
EXPOSE 5000
CMD python manage.py runserver --host='0.0.0.0' --port=5000