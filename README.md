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

## Goal

End goal is to use python and this mysql-connector package to read and write from 
AWS RDS MySQL which running in the same VPC. Afterwards, the HTML/CSS should be able
to render that information in tables/graphs. 

## Jenkins

Jenkins CI/CD server is running live on http://18.222.161.78:8080 
It will generate a build whenever someone pushes to this repo. Build will fail if Jenkins cannot pull most recent changes from Github or if website is down. 

## Helpful Links
https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.Scenarios.html#USER_VPC.Scenario1

