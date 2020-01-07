# Data-Representation-Project-2019

## How to download the repository:
1. Download the repository from the following link <a href=https://github.com/Roisin-Fallon/Data-Representation-Project-2019>Click here</a>  
2. Click the clone or download button towards the right of your screen
3. Download and unzip this file. Save the unziped file to a location on your desktop where it is easily accessible
4. Open the command line and navigate to the location of your downloaded file using a series of cd commands 

## Command to create virtual machine 
1. python -m venv venv 
2. Create a temporary .gitignore file using the vi .gitignore make sure to change to INSERT venv by typing INSERT then on top venv/ then press esc :wq. The following should be found in your .gitignore venv/ *config.py __pycache__
3.  .\venv\Scripts\activate.bat
4. pip install flask  
   pip3 install mysql-connector-python     
   pip install flask_cors pip3 install flask-mysqldb
   pip freeze > requirements.txt
5. set FLASK_APP=memberserver
   set FLASK_ENV=development
   set FLASK_DEBUG=1
6. echo %FLASK_APP%
7. flask run
8. Copy the url to the web browser: to view the membership should appear like :  http://127.0.0.1:5000/membership.html; to view the general website  http://127.0.0.1:5000/gymwebsite.html and using the tabs we can navigate through the different tabs

Python Anywhere:

Python Anywhere can be accessed at the following link: http://roisinfallonshauna.eu.pythonanywhere.com/
 * Again you will arrive at the login page and the same username and password should be used. Please enter username: andrew and password: andrew. I have promted this in this situation but this would be removed in a normal situation.  If the incorrect username or password is entered the user will not be able to enter the website until they enter the correct credentials.
 * If you would like to view my work for python anywhere this can be accessed by entering the email: lifenmotiongym@gmail.com username: RoisinShaunaFallon password: lifenmotiongym.
 I added a module to the service on the host: added corrs - again this can be viewed by loggining into the python anywhere website. 
 
Please not I added mode

Footer:
In the footer of each of the html pages I have included social networ icon bar which link towards twitter, gmail that I created for Life N Motion Gym, a youtube tutorial to a fitness video etc. 
