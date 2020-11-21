#!/bin/bash
if [[ $1 == 'get' ]]
then
  python3 ../src/get.py $1 $2
elif [[ $1 == '--getall' ]]
then
  python3 ../src/get.py $1
elif [[ $1 == 'set' ]]
then
  python3 ../src/set.py $1 $2 $3
elif [[ $1 == 'del' ]]
then
  python3 ../src/del.py  "rem" $2
elif [[ $1 == '--version' ]] || [[ $1 == '--v' ]]
then
  python3 ../src/client.py $1
else
  python3 ../src/client.py -h
fi
