FROM python:3.8.3

ENV TIME_ZONE Asia/Shanghai

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
EXPOSE 5000
ENV env prod
CMD python manage.py runserver --host='0.0.0.0' --port=5000