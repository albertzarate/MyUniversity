# MyUniversity

Installed on this EC2 instance is mysql 5.7. You can connect to it via CLI using the following command:
```
mysql -u myuniversity -p -h myuniversity.......us-east-2.rds.amazonaws.com
```
Get the mysql host from Udit.

I've included a sample python script on how to login to mysql programmatically. 
Feel free to test out code there. Once you're happy with the code, feel free to 
add it to the flask app and see if it works there too. 

## Logging Into EC2 Instance
1. Download the pem key
2. Run: 
```
chmod 400 *somekey.pem*
```
3. Login using:
```
ssh -i "somekey.pem" ubuntu@ec2-......compute.amazonaws.com
```
Get the ec2 host from Udit.

## Roles

MyUniversity is a multi-role web application meaning that depending on the login user, they will be presented with a  different web UI showing information relavant to them. Students and teachers/professors will both have access to the useful tools we've integrated. 

## Jenkins

Jenkins CI/CD server is running live on http://18.222.161.78:8080 
It will generate a build whenever someone pushes to this repo. Build will fail if Jenkins cannot pull most recent changes from Github or if website is down. 

## Docker

Docker is installed on the AWS EC2 instance and is used to create containers of our entire web app. This guarantees that no matter what machine we run our web app on, it will always run successfully (given the appropriate hardware). 

## Ansible

An Ansible file exists in the config folder. It'll create an EC2 instance on AWS, create an RDS MySQL instance on AWS, SSH into the AWS EC2 instance, install pip, install docker-py, install docker.io, copy over the Dockerfile, build an image from the Dockerfile, create a container using that image, and start the apache server on port 80. The container's port 80 is forwarded to port 80 of the host (EC2 instance). When running the playbook, make sure the Dockerfile is in the same directory as the playbook. 

## Integrations
* Google Maps
* Google Calendar
* NewsAPI News
* DarkSky Weather

## Video Demo
https://youtu.be/PxCyvCKT4EA

## Helpful Links
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Scenarios.html#USER_VPC.Scenario1
https://www.codementor.io/mamytianarakotomalala/how-to-deploy-docker-container-with-ansible-on-debian-8-mavm48kw0
https://docs.docker.com/v17.12/engine/reference/run/
