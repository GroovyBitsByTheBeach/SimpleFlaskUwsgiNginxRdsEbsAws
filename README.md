# SimpleFlaskUwsgiNginxRdsEbsAws
Simple example of a FLASK web app communicating with uWSGI to Nginx, with Dockerfile, etc. as needed for deployment on ElasticBeanstalk (Amazon Web Services, AWS)

This project is inspired by:

How To Serve Flask Applications with uWSGI and Nginx on Ubuntu 14.04
https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-14-04

Deploying a Flask application on AWS
https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80

Note that you will need to fill appropriate values in config.py (related to your DB connection string and secret code). See the 2nd of the 2 articles mentioned immediately above.

To run locally, edit config.py. Uncomment the setting of SQLALCHEMY_DATABASE_URI so you use a local SQLLite DB (test.db). 

The cleanbuild.sh script:
1) Kills this Docker container if it happens to be running.
2) WARNING: Deletes all existing Docker images and containers.
3) Builds this web app as a Docker image/container and runs it.

Once the Docker container is running, open a browser and visit localhost (on OSX this will be the IP identified by the statement: boot2docker IP). 

Once you have an AWS RDS DB and an appropriate connection string, you can put it in config.py. You can use that DB, even when running from your computer. The Docker container does not need to be deployed on AWS to use the DB on AWS.

However deploying on AWS is easy. Make sure that the AWS DB is configured for use in config.py. ZIP up 5 files and the app folder:
Dockerfile
Dockerrun.aws.json
flask.conf
supervisord.conf
uwsgi.ini

Deploy that ZIP on AWS' ElasticBeanstalk.
