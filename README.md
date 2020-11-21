# KV (key-value) Service

# Problem Statement
The problem statement was to build a simple KV (key-value) store web service with a subscription feature. As a user, I should be able to perform set(key, val) and get(key)  operations over HTTP and also subscribe to changes happening to any of the key

# Approach

The approach to solve the above problem was to use python flask framework to create a CRUD api which can store data in key value form in memory and similarly design a client in python which can fetch the values from the given api.

### language Used

* python
* shell


# Prerequisite
[Docker](https://docs.docker.com/get-docker/) must be installed and running  


#### Directory Structure of Assignment

After Cloning the  directory this will look something like this :-

![directory Structure](https://github.com/YashDevops/KV-Store/blob/master/images/direct-structure.png)


- utility : It contains all the code for in memory saving key-value data
- client : It contains all `bin` and `src` where the binary in in `bin` and the client code is in `src`
- The Root Directory contains the `Dockerfile` for the build and running of `kv-server`
- build.sh : It as interactive command-line to setup `kv-server` for user


# :rocket: Launch

### To get App up and running follow the server follow the following steps

1. Clone the following Repo

```
git clone https://github.com/YashDevops/KV-Store.git

cd KV-Store
```
2. The simplest way to get `kv-server` up and running is by running command

```
bash build.sh

```

which will give you an interactive menu to choose either to configure `kv-server` or `kv-client`

```
The following script will setup both the CLIENT and SERVER for you
 --------------------------------------------------------------------------------------------------------
 1 . To Setup Server
 2 . To Setup Client
Enter your choice :

```

3. Choose `1` to `Setup Server` and it will start a docker container with application running on it.

Output will be like something :-

```
Sending build context to Docker daemon  922.1kB
Step 1/5 : FROM python:3.8
 ---> c0e1d3033786
Step 2/5 : COPY utility/requirements.txt .
 ---> Using cache
 ---> f1afaa82c662
Step 3/5 : RUN pip install -r requirements.txt
 ---> Using cache
 ---> 3173130eb029
Step 4/5 : COPY  utility/code/ .
 ---> Using cache
 ---> 134e08747ce5
Step 5/5 : CMD [ "python", "app.py" ]
 ---> Using cache
 ---> 5f0eeeb22cf0
Successfully built 5f0eeeb22cf0
Successfully tagged kv-server:latest
e3d8eacc5ab61984e6931eac407708628bb32dc4fe5c38d6c10d3389b858dab3

```
