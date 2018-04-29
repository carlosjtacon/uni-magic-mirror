Dependencies
============
1. [Python 3](https://www.python.org/downloads/release/python-364/), [Node JS + NPM](https://nodejs.org/es/).
2. Hey Athena 1.2.2 + [Dependencies](https://rcbyron.github.io/hey-athena-website/docs/intro/install.html#developer-github-installation).
3. [Angular CLI](https://github.com/angular/angular-cli#installation).
4. Arduino + [Arduino IDE](https://www.arduino.cc/en/main/software).
5. Go to /mirror-client and *npm install*.

Execution
=========
1. Run web client: go to /mirror-client and run *ng serve*, go to localhost:4200.
2. Run python server: go to /server and run *python server.py*.
3. Run athena: go to /hey-athena-client-1.2.2/athena and run
*python __main__.py*.
4. Run arduino sensors:go to /mirror-sensors and run *python SensorPoster.py*.  __* ser = serial.Serial('/dev/*********', ****)__.
5. We have everyting running local. You can play modifying and running *python post-dev-demo.py*