# The Mars Rover Challenge - Python Edition

This is my solution to the Mars Rover Challenge found here: [https://code.google.com/archive/p/marsrovertechchallenge/](https://code.google.com/archive/p/marsrovertechchallenge/)

  - The Python project is currently under construction.
  - Django is the application web server that will be used for this project.

### Installation

This Project is being written in Python 3.7.2. Please ensure that all dependencies are installed on the localhost before running Django web server:

Install the following dependencies(preferably using pip(default Python installer - available after Python install)):

  - Python 3.7.2
  - Django 2.1.7
  - django-crispy-forms 1.7.2

### Start-up

Once all dependencies have been installed, open your system terminal(bash/mac/cmd(MINGW32/64)) and change your directory to where your branch has been pulled to, make sure there is a manage.py file in this directory. From here, run 'python manage.py runserver', this will start the django server on your local machine. Once up, go to [http://localhost:8000/](http://localhost:8000/) and follow the instructions.

Most machines will have 'python' as the default environmental variable once Python is installed. 
```sh
python manage.py runserver
``` 
However some machines, particularly ones with pre-existing Python 2, will have to use the following:
```sh
python3 manage.py runserver
``` 
If you would like to test the server before hand, please run a check as follows:
```sh
python manage.py check
``` 