#Creating Virtual Environments

To create a virtual environment, decide upon a directory where you want to place it, and run the venv module as a script with the directory path:

##python3 -m venv tutorial-env
##source tutorial-env/bin/activate

#Managing Packages with pip

You can install, upgrade, and remove packages using a program called pip. By default pip will install packages from the Python Package Index, <https://pypi.org>. You can browse the Python Package Index by going to it in your web browser, or you can use pip’s limited search feature:

##pip search astronomy
##pip install novas
##pip install requests==2.6.0
##pip install --upgrade requests
##pip show requests
##pip list
##pip freeze > requirements.txt
##cat requirements.txt
##pip install -r requirements.txt