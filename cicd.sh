#!/bin/bash

dockerhubregistry=your-registry
dockerhubnamespace=your-namespace
username=registry-username
password=registry-password
# ci
# ...
prefix=${dockerhubregistry}/${dockerhubnamespace}
imagename=flask-factory
version=$(date +%Y%m%d.%H%M)
docker build -f Dockerfile -t ${prefix}/${imagename}:${version} .


# 登录
#docker login ${dockerhub_registry} --username=${username} --password=${password}
# 上传

#docker push ${prefix}/${imagename}:${version}
docker tag ${prefix}/${imagename}:${version} ${prefix}/${imagename}
#docker push ${prefix}/${imagename}

# cd
# 起docker-compose.yml
docker-compose -f ./docker-compose.yml up -d

# 手动配置nginx
# ...