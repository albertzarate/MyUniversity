# MyUniversity

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

## Accessing MySQL on AWS RDS
Installed on this RDS instance is mysql 5.7. You can connect to it via CLI using the following command:
```
mysql -u myuniversity -p -h myuniversity.......us-east-2.rds.amazonaws.com
```
Get the mysql host from Udit.

## SSO/Authentication

MyUniversity uses Auth0 SS0 Authentication which allows users to login via Google or username/pass. All users must use The Guardian App by Auth0 for multi-factor authentication. We have also included role-based authentication.

## Role-Based

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

## Donations for Technologies
Please feel free to give us some money for incorporating https on an enterprise-grade production Apache2 web server. I can tell you right now that https can only be accomplished for free if the certificates are self-signed (bogus) or you decide to use a development server (very insecure). Look out for this! Also feel free to donate some money for us to integrate Dropbox, Office 365, and Slack ~ we can easily do this with some money. Additionally, our free trial ends on May 16, 2019 for Auth0 authentication so if you'd like to lend us $13 a month we'll gladly keep our website hosted!

## Helpful Links
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Scenarios.html#USER_VPC.Scenario1
https://www.codementor.io/mamytianarakotomalala/how-to-deploy-docker-container-with-ansible-on-debian-8-mavm48kw0
https://docs.docker.com/v17.12/engine/reference/run/
