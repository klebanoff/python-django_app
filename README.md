# python django app
[![Build Status](https://app.travis-ci.com/klebanoff/python-self-study-project.svg?branch=main)](https://app.travis-ci.com/klebanoff/python-self-study-project)
[![Coverage Status](https://coveralls.io/repos/github/klebanoff/python-self-study-project/badge.svg?branch=main)](https://coveralls.io/github/klebanoff/python-self-study-project?branch=main)  
this is a web-based application for Human resource management  
Server can be started with following commands:
```
source env/bin/activate
cd mysite
gunicorn mysite.wsgi
```
Web server is accecable via http://127.0.0.1:8000/department_app/
## screenshots
List of departments:
![departments](/images/departments.png)
Detailed view of department:
![department](/images/department.png)

List of employees:

![employees](/images/employes.png)

Detailed view of employee:

![employee](/images/employee.png)
