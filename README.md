1. ./make_exectuable.sh

run a test of the local host

MACOSX Help at:
https://wiki.jenkins.io/display/JENKINS/Thanks+for+using+OSX+Installer

DEV NOTES

Additons to follow:

* Code commit to main or release branch: when tests pass, push an artifact, such as pip package or docker image, or an artifact repository
* Submission of pull/merge request: run tests and provide feedback to git server, such as GitHub or GitLab, and block submission approval if tests fail.

For visual feed back to the a git server:

* webhooks on those services
* token generated with authorization to access the repository (or an account with access)
* Jenkins plug-in (GitLab plugin and GitHub plugin)

PROJECT PRIMER
https://medium.com/@Joachim8675309/jenkins-ci-pipeline-with-python-8bf1a0234ec3 # Thanks!
