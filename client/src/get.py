import os
import argparse
import requests



url="http://localhost:8080/key/"
getall="http://localhost:8080/alllist"
def getall():
    result = requests.get(getall)
    responses=result.json()
    print(responses)

def get(params):
    url="http://localhost:8080/key/"+params.get[1]
    result=requests.get(url)
    print(result.json())

def main():
    usagemsg="usage: get [-h] requires key | ex get {key}"
    my_parser = argparse.ArgumentParser(description='A Simple KV (key-value) store web service with a subscription feature. As a user, I should be able to perform set(key, val) and get(key)  operations over HTTP and also subscribe to changes happening to any of the keys.',usage=usagemsg)
    my_parser.add_argument('get', action='store', nargs=2,type=str)
    my_parser.add_argument('-all','--getall',help="get all the key")
    args = my_parser.parse_args()
    if args.get:
        get(args)
    if args.getall:
        getall()




if __name__ == "__main__":
    main()
