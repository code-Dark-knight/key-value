#!/bin/bash
if [[ $1 == 'get' ]]
then
  python ../src/get.py $1 $2
elif [[ $1 == '--getall' ]]
then
  python ../src/get.py $1
elif [[ $1 == 'set' ]]
then
  python ../src/set.py $1 $2 $3
elif [[ $1 == 'del' ]]
then
  python ../src/del.py  "rem" $2
else
  python ../src/client.py -h
fi
