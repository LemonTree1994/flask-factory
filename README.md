# flask-factory
 This is a simple example of flask factory app.
 Use docker to support it and do cicd.
 
## Run it
    Preparation: git docker
    the first time: git clone https://github.com/LemonTree1994/flask-factory.git && sh cicd.sh
    update: git pull && sh cicd.sh
    
# Why flask
Flask is a flexible and micro framework, and it is more suitable for a restful api.
# Why factory
## What is a factory design pattern
     Simply, I give u a name(in this project, it is a config name), u give me an entity(an app).
     That means it don't need u create the app from begin to end, just need a name.
##  Advantage
     Use factory design pattern is easier to switch between prod and dev environments.
