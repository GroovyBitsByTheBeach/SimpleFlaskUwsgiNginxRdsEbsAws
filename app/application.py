#!flask/bin/python
'''
Reference https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80
'''

from flask import Flask
from application import application

if __name__ == '__main__':
    application.run(host='0.0.0.0')
