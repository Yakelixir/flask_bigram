#!/usr/bin/env bash

chmod +x app.py
chmod +x test_app.py

app.py &
# test the server
curl -i localhost:5000/
curl -i localhost:5000/hello/
curl -i localhost:5000/hello/Simon

# start Jenkins
sudo launchctl load /Library/LaunchDaemons/org.jenkins-ci.plist

cd /Applications/Jenkins/

java --enable-future-java -jar jenkins.war --httpPort=8080

#Jenkins initial setup is required. An admin user has been created and a password generated.
#Please use the following password to proceed to installation:
#
#ada4bfcfb051417287a5e8452214de8a
#
#This may also be found at: /Users/truth/.jenkins/secrets/initialAdminPassword