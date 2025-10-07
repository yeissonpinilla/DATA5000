# DATA5000

Repository for DATA 5000 final course project at Carleton University

To be able to clone and execute this Django project, you should:

1. Clone this repository. Using SSH is adviced, and not too complex. In case you need any help, let me know.
2. Once you have cloned the repository, you will have to create a virtual environment, steps 3 to 6 explain how to do it.
3. Navigate through your terminal until DATA5000 folder created when you cloned the repo (the first folder with that name)
4. Run command "python3 -m venv venv" this is going to create a virtual environment with name venv
5. Activate your venv (using Mac "source venv/bin/activate", using Windows CMD "venv\Scripts\activate.bat")
6. You should see now a sign on your cmd indicating you are using venv
7. On your venv, run command to install dependencies: "pip install -r requirements.txt"
8. Now, move to the nested DATA5000 folder
9. You will need to apply DB changes by using "python manage.py migrate", everything should show "OK"
10. Download ANY .json file from match folder from statsbomb repository
11. Create your own superuser "python manage.py createsuperuser" and follow instructions on your terminal
12. Run following command to bring .json data into our Django project "python manage.py import_json {your_path_to_json_file}" NOTE: Put your path until the folder containing your json file, not until your actual json file.
13. Run following command to start Django server "python manage.py runserver"
14. Go to http://127.0.0.1:8000/admin, where you can login with the superuser credentials you created in step 11.
