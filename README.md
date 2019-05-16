# Setting up your development environment

1. install Python3.7 (this might help: https://tecadmin.net/install-python-3-7-on-ubuntu-linuxmint/)
2. install pip3 and pip

```
sudo apt install python-pip
sudo apt install python3-pip
```
 
3. install virtualenvwrapper (this is worthwhile! Because it is cool):
   please follow this tutorial for easy installation [here](https://www.youtube.com/watch?v=kC20Pfi-k1Q&t=100s)

   1. After following the tutorial, open your .bashrc script with:
        $ nano  ~/.bashrc

   2. Update your.bashrc by adding something like this near the top.
      You can probably just copy-paste this stuff:

      ```
      export WORKON_HOME=~/.Envs
      VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'
      source /usr/local/bin/virtualenvwrapper.sh

      ```

   3. Now source your bashrc file with:

   ```
   source ~/.bashrc
   ```

4. make a virtualenvironment to use for this project and activate it:
   1. if using virtualenvwrapper:
      `mkvirtualenv -p $(which python3.7) web-refvn`
      For now on you can activate this environment like so:
      `workon web-refvn`


5. Install requirements: `pip3 install -r requirements.txt`


# setting up the dev database

This project relies on mysql 5.7.25.

The simplest way to set up a development db that is consistent with everyone else is to use docker. So install `docker`

Follow the simple instructions found here `https://docs.docker.com/install/linux/docker-ce/ubuntu/`

After installing docker, create a mysql container with:
`sudo docker run --name db -d -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password mysql:latest`

Here's what it does:

0. Creates a Docker MySql container called `db`
1. The container is mapped to use port 3306
1. The password of the database is `password`

    If you prefer to view your database through a GUI, you can use MySql Workbench or install it if you do not have it on your machine. Else, you can open the MySql shell by running:
    `sudo docker exec -it db /bin/bash`

    After running the above command, then run the following command
    `mysql -uroot -ppassword`

    Now you have access to the database through the shell.

Now create a database called `webref` from the shell or MySql Workbench.

When the database has been created, run `python3 manage.py migrate` to create tables in the database


Now everything is set up. If you want to run the development server, activate your virtual environment then:


`cd web_ref`
`python3 manage.py runserver`




# Port errors when launching docker

If you are getting an error to the effect of: Port 8080 or port 3306 is already in use, and you aren't using those ports anywhere that you know of then you might wanna do the following:

Use this command to list the running containers:
`sudo docker container ls`

The output could look something like this:

```
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                               NAMES
74142f965c05        adminer             "entrypoint.sh docke…"   13 minutes ago      Up 2 seconds        0.0.0.0:8080->8080/tcp              dev_db_adminer_1
e057225282a1        mysql:5.7.25        "docker-entrypoint.s…"   3 hours ago         Up 3 seconds        0.0.0.0:3306->3306/tcp, 33060/tcp   dev_db_db_1
```

These are all the running containers. You can kill them individually by using their container ids. Eg if I wanted to kill the adminer container then I would do the following:
`sudo docker kill 74142f965c05`

If you want to kill all running containers you can run:
`sudo docker kill $(docker container ls -a -q)`

If your container is not running and the name of the container is x, you can restart it with:
`sudo docker restart x`



# Running the db migrations

if you made some changes to app_x.models then:

```
python3 manage.py makemigrations
python3 manage.py makemigrations app_x
python3 manage.py migrate
```

# creating a superuser

```
python3 manage.py createsuperuser
```