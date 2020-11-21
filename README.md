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
