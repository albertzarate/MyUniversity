# MyUniversity

Installed on this EC2 instance is mysql 5.7. You can connect to it via CLI using the following command
```
mysql -u myuniversity -p -h myuniversity.cwscsavqzqxt.us-east-2.rds.amazonaws.com
```

I've included a sample python script on how to login to mysql programmatically. 
Feel free to test out code there. Once you're happy with the code, feel free to 
add it to the flask app and see if it works there too. 

End goal is to use python and this mysql-connector package to read and write from 
AWS RDS MySQL which running in the same VPC. Afterwards, the HTML/CSS should be able
to render that information in tables/graphs. 
