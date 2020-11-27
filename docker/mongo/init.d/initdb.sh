#!/usr/bin/env bash

mongo -u ${MONGO_INITDB_ROOT_USERNAME} -p ${MONGO_INITDB_ROOT_PASSWORD} << EOF

use admin
db.createUser(
    {
        user: "admin",
        pwd: "${MONGO_PASSWORD}",
        roles: [{role: "userAdminAnyDatabase", db: "admin"}]
    }
)

use ${MONGO_DATABASE}
db.createUser(
    {
        user: "${MONGO_USERNAME}",
        pwd: "${MONGO_PASSWORD}",
        roles: [{role: "readWrite", db: "${MONGO_DATABASE}"}]
    }
)
db.createCollection("test")

EOF
