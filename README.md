# key-value Service

The approach is to use python flask framework to create a CRUD api which can store data in key value form in memory and similarly design a client in python which can fetch the values from the given api.

# language

* python
* shell

# Usage

* set {key} {value} : It will set key-value in {"key": {key} , "value": {value}}. set command only sets unique keys. If you try set an already present key it will return you a message : `{'message': 'set command can set unique key and value already exists'}`

* get {key} : It will fetches the value of the given key.

* del {key} : It will delete the {key} | {value} pair. Any {key} that has been subscribed and delete will also be removed from the subscription list if not updated.

* getall : It will return all the {key} {value} pair at any point of time in KV-Store memory.

* suball : It will return a list of all the key which has been subscribed. These key will response to any changes done via put.

* put {key} {value} : It's an update command. If there is no key in the memory in the KV-store it will add the {key}-{value} pair. If there is any {key} present it will update that. If any key is under subscription-list and get update via put command it will return a message : `{'message': 'subscription key has been updated', 'key': 'yash', 'oldvalue': 'shah', 'newvalue': 'kumar'}`

* subs {key} : It will set the key in subscription list any changes done to that {key} via put will response to changes.


# Prerequisite
- Docker (https://docs.docker.com/get-docker/) must be installed and running. 
 
- Python

- Pip

# How to Launch

#### 1. Clone the following Repo

```
git clone https://github.com/code-Dark-knight/key-value.git

cd key-value
```

#### 2. To get server up and running is by running command

```
bash build.sh

```

which will give you an interactive menu to choose either to configure server or client

```
The following script will setup both the CLIENT and SERVER for you
 --------------------------------------------------------------------------------------------------------
 1 . To Setup Server
 2 . To Setup Client
Enter your choice :
```

#### 3. Choose `1` to `Setup Server` and it will start a docker container with application running on it.


#### 4. Run the same step again `build.sh` file to setup client this time

```
The following script will setup both the CLIENT and SERVER for you
 --------------------------------------------------------------------------------------------------------
 1 . To Setup Server
 2 . To Setup Client
Enter your choice : 2
```

#### 5. All done

#### 6. Performing Operations

#  Setting a Key

* To Set a key you can set it the following way

![set key](https://github.com/YashDevops/KV-Store/blob/master/images/set.png)



#  Getting a Key

* To get a key you can set it the following way

![get key](https://github.com/YashDevops/KV-Store/blob/master/images/get.png)


#  Deleting a Key

* To delete a key you can set it the following way

![delete key](https://github.com/YashDevops/KV-Store/blob/master/images/del.png)


#  Get all the Key

* To get all a key at a given time

![get-all key](https://github.com/YashDevops/KV-Store/blob/master/images/getall.png)


# Subscribe get for any changes

![sub key](https://github.com/YashDevops/KV-Store/blob/master/images/subs.png)

##### To check subscription on key at any given time you can `suball` to get all the key in subscription is set.



## :exclamation: ERROR

#### 7. IF there is an issue with setting up client. Try setting it up manual. Below are the steps to setup client manually. The above code has been tested in an fresh EC2 machine at region : ap-south-1 with ami-id : ( ami-00ddb0e5626798373 ) ubuntu/images/hvm-ssd/ubuntu-bionic-18.04-amd64-server-20201026

```
pip install -r client/requirements.txt
cd client/bin/
bash kv-client.sh
```
