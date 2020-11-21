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

![](https://github.com/YashDevops/Assignment/blob/master/img/tree-Assignment-Dir.png)


- All  the modules are under `modules` directory
- Every `env` | `prod` or `dev` is inside the project directory. Currently prod has the our project `assignment`
- All the Ansible related code is inside the `Ansible` Directory
- `Ansible` Directory contains `roles` and `Mediawiki`. Roles are common roles which are used in the project `Mediawiki` and the dynaminc values are passed on to it via folder `group_vars`
- `keys` are normal which will be used by the `terraform` code to push public key in all the instances lauched to maintain `ssh` accessibility
- `config` directory contains all the common application that require configuration. Mediawiki is running `nginx` as a web-server and `php-fpm` as downstream server. The nginx-conf is copied from local to private app server from `config` directory
