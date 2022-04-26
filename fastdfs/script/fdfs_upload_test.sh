#!/usr/bin/env bash 
TMP='/tmp/thisistest.txt'
FDFS_CLIENT_CONF='/etc/fdfs/client.conf'
if [ ! -f $TMP ];then
    touch $TMP
fi
result=$(fdfs_upload_file $FDFS_CLIENT_CONF $TMP)
#echo $result |grep group  > /dev/null
if [ $? == 0 ];then
   echo "upload ok"
   fdfs_delete_file $FDFS_CLIENT_CONF $result
else
   echo "upload bad"
fi
