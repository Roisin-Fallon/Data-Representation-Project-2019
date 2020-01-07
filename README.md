
# Data-Representation-Project-2019

## Roisin Fallon

In this project I created a gym web application. The files above represent the following:

|File Name | Description                            |
|----------|----------------------------------------|
|images | This folder contains the images that were used in this project |
|.gitignore | This is a text file that tells GIT which files or folders to ignore in the project |
|Project Description.pdf | This gives the outline of the Data Representation Project 2019 |
|README.md | This is the current file that briefly describes the project |
|requirements.txt | This file is used for specifying what python packages are required to run the project |
|contact.html| Page on the website that allows user to ask question |
|gymwebsite.html| web page that ties the project together|
|index.html| home page that the user will arrive to once they have entered the correct username and password|
|login.html| Webpage which shows how the login page will appear|
|membership.html| Webpage with CRUD interface for interacting with database|
|schedule.html| Webpage which shows the timetable for the classes for the Life N Motion Gym|
|createDatabase.py| Create a table containing the gym members, run on the command line: python createDatabase.py |
|insertIntoTable.py| Insert row into the gym members table, run on the command line: python insertIntoTable.py |
|dbconfig.py| File for configuration of MySQL parameters|
|dbconfigtemplate.py | Template file for configuration of MySQL parameters|
|memberDAO.py| Data Access Object file for interacting with the members database|
|memberserver.py| Web server for local gost and Python Anywhere|
|gym.js|A JS file is a text file containing JavaScript code that is used to execute JavaScript instructions in web pages. It may include functions that open and close windows, validate form fields, enable rollover images, or create drop-down menus.|
|style.css| This describes how html elements are to be displayed on screen which allows control over multiple web pages all at once |

# PLEASE NOTE THE FOLLING FEATURES TO MY WEB APP

* ### Footer:
In the footer of each of the html pages I have included social networ icon bar which link towards twitter, gmail that I created for Life N Motion Gym, a youtube tutorial to a fitness video etc.
* ### Timetable created using html 
* ###  Mmeber Database it is really important that when you update you include the date joined as it will not work correctly otherwise


# Data-Representation-Project-2019

## How to download the repository:
1. Download the repository from the following link <a href=https://github.com/Roisin-Fallon/Data-Representation-Project-2019>Click here</a>  
2. Click the clone or download button towards the right of your screen
3. Download and unzip this file. Save the unziped file to a location on your desktop where it is easily accessible
4. Open the command line and navigate to the location of your downloaded file using a series of cd commands 

### Run virtual machine
1. Once you have navigated to the location of your folser using a series of cd commands. Please do the following commands:
 *  python -m venv venv 
 * .\venv\Scripts\activate.bat
 * set FLASK_APP=memberserver
 * set FLASK_ENV=development
 * set FLASK_DEBUG=1
 * echo %FLASK_APP%
 * flask run
2.  Copy the url to the web browser: to view the membership should appear like :  http://127.0.0.1:5000/membership.html; to view the general website  http://127.0.0.1:5000/gymwebsite.html and using the tabs we can navigate through the different tabs

### Commands to create a virtual machine 

<i> When setting up the virtual machine there were commands needed which I outlined below but as they are in the requirements.txt and .gitignore there is no need to do all these commands. This is simply to explain how to approach setting up a virtual machine. </i>

 *  python -m venv venv 
 *  Create a temporary .gitignore file using the vi .gitignore make sure to change to INSERT venv by typing INSERT then on top venv/ then press esc :wq. The following should be found in your .gitignore venv/ *config.py __pycache__
 * .\venv\Scripts\activate.bat
 * pip install flask 
 * pip install mysql-connector-python     
 * pip install flask_cors pip3 install flask-mysqldb
 * pip freeze > requirements.txt
 * set FLASK_APP=memberserver
 * set FLASK_ENV=development
 * set FLASK_DEBUG=1
 * echo %FLASK_APP%
 * flask run

## Python Anywhere:

Python Anywhere can be accessed at the following link: http://roisinfallonshauna.eu.pythonanywhere.com/
 * Again you will arrive at the login page and the same username and password should be used. 
 <b> Please enter the following:
   
      * username: andrew 
      * password: andrew. </b> 
      
  * I have promted this in this situation but this would be removed in a normal situation.  
  * If the incorrect username or password is entered the user will not be able to enter the website until they enter the correct credentials.
 * If you would like to view my work for python anywhere my creddentials are the following:
 
      * email: lifenmotiongym@gmail.com 
      * username: RoisinShaunaFallon 
      * password: lifenmotiongym.
      
 * I added a module to the service on the host: added corrs - again this can be viewed by loggining into the python anywhere website. 


### MySQL Database 

#### MySQLommand to creeate table 

 CREATE TABLE members(
       id int NOT NULL AUTO_INCREMENT,
       email VARCHAR(255),
       membershipPlan VARCHAR(20),
       startDate DATE,
       age INT,
       PRIMARY KEY(id)
       );


DESC members;

| Field          | Type         | Null | Key | Default | Extra          |
|----------------|--------------|------|-----|---------|----------------|
| id             | int(11)      | NO   | PRI | NULL    | auto_increment |
| email          | varchar(255) | YES  |     | NULL    |                |
| membershipPlan | varchar(20)  | YES  |     | NULL    |                |
| startDate      | date         | YES  |     | NULL    |                |
| age            | int(11)      | YES  |     | NULL    |                |


#### MySQLommand to insert row into table 

insert into members (email, membershipPlan, startDate, age) values ("marygarcia@gmail.com","Monthly", "2018-07-24", 23)

insert into members (email, membershipPlan, startDate, age) values ("jameskelly@yahoo.ie","Annually", "2018-11-02", 30)

insert into members (email, membershipPlan, startDate, age) values ("johnbyrne@gmail.com","Daily", "2019-02-12", 19)

| id | email                     | membershipPlan | startDate  | age  |
|----|---------------------------|----------------|------------|------|
|  1 | marygarcia@gmail.com      | Monthly        | 2018-07-24 |   23 |
|  2 |  jameskelly@yahoo.ie      | Annually       | 2018-11-02 |   30 |
|  3 |  johnbyrne@gmail.com      | Daily          | 2019-02-12 |   19 |

