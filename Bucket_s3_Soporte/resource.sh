#!/bin/bash

MONGO_URI_0="mongodb://mongo-izzi-prod-shard-00-02.ytutu.mongodb.net:27017"
MONGO_URI_1="mongodb://mongo-izzi-prod-shard-00-00.ytutu.mongodb.net:27017"
MONGO_USERNAME="sym_admin"
MONGO_PASSWORD="QkZEp4sQrAeJTZMu"
MONGO_AUTH_DB="admin"

HOME_PATH="/etc/telegraf/telegraf.d/scripts/old/resourceOrderFailed"
FILE_DUMP="resourceOrderFailed_$(date +%d%m%Y).csv"


/usr/bin/mongo --ssl --quiet --username "$MONGO_USERNAME" --password "$MONGO_PASSWORD" --authenticationDatabase $MONGO_AUTH_DB $MONGO_URI_0 < $HOME_PATH/resourceOrdersFailed.js > $HOME_PATH/$FILE_DUMP 

if grep -q "NotMasterNoSlaveOk" $HOME_PATH/$FILE_DUMP
then
        /usr/bin/mongo --ssl --quiet --username "$MONGO_USERNAME" --password "$MONGO_PASSWORD" --authenticationDatabase $MONGO_AUTH_DB $MONGO_URI_1 < $HOME_PATH/resourceOrdersFailed.js > $HOME_PATH/$FILE_DUMP
fi

sed -i '1d' $HOME_PATH/$FILE_DUMP

while read line
do
        #echo "$line $(date +%s%N)"
        echo "$line"
done < $HOME_PATH/$FILE_DUMP

#rm -f $HOME_PATH/$FILE_DUMP
