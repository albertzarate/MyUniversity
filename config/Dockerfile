FROM ubuntu:16.04

# Install Ubuntu dependencies
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y install apache2
RUN apt-get -y install python-virtualenv
RUN apt-get -y install python3-pip
RUN apt-get install -y libmysqlclient-dev
RUN pip3 install virtualenv
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools

#Clone Repo
RUN apt-get -y install git
RUN cd /home/; mkdir ubuntu
RUN cd /home/ubuntu/; git clone https://github.com/albertzarate/MyUniversity.git; mv MyUniversity flaskapp
RUN mv /home/ubuntu/flaskapp/config/000-default.conf /etc/apache2/sites-enabled/

#Install necessary packages for MyUniversity application
RUN pip3 install Flask
RUN pip3 install python-dotenv
RUN pip3 install requests
RUN pip3 install authlib
RUN pip3 install six
RUN pip3 install sqlalchemy
RUN pip3 install pymysql
RUN pip3 install mysql
RUN pip3 install dotenv
RUN pip3 install pyopenssl
RUN pip3 install mysqlclient

RUN apt-get -y install apache2 libapache2-mod-wsgi-py3
RUN ln -sT /home/ubuntu/flaskapp /var/www/html/flaskapp

EXPOSE 80


