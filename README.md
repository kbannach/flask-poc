# Simple Flask application
A simple app written in Python's Flask, which uses Google Directions API to execute a simple query (find Gdansk <-> Gdynia route details) and present total distance and time on a simple view.
## How to run
There are two ways:
1. configure the app on your local environment
    - install Python and flask and googlemaps libraries  
      example in bash:
      ```
      sudo apt-get install --assume-yes python-pip
      pip install flask
      pip install -U googlemaps
      ```
    - paste your Google API key in the config file (you can use `config.py.example` file - replace the `your API key` placeholder with your key and remove the `.example` suffix from the file name) 
    - export necessary envs
      ```
      export FLASK_APP=flaskr
      export FLASK_ENV=development
      export APP_CONFIG_FILE=/workspace/flaskr/config.cfg
      ```
    - run the app
      ```
      flask run
      ```
    - app is available at http://127.0.0.1:5000 at your host machine, use `/directions` endpoint to see the route's view
2. use Vagrant to spin up a VM with all necessary setup
   - install Vagrant: www.vagrantup.com
   - install VirtualBox: www.virtualbox.org
   - paste your Google API key in the config file (you can use `config.py.example` file - replace the `your API key` placeholder with your key and remove the `.example` suffix from the file name)
   - create a VM and SSH inside:
     ```
     cd <project-root-dir>
     vagrant up && vagrant ssh
     ```
   - run the app with prepared alias
     ```
     frun
     ```
   - when you're done run `vagrant halt` to stop the VM or `vagrant destroy` to remove it
   - app is available at http://192.168.50.4:5000 at your host machine, use `/directions` endpoint to see the route's view
3. TODO add Dockerfile