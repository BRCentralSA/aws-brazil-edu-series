#!/bin/bash

sudo /opt/bitnami/ctlscript.sh stop apache && sudo /opt/bitnami/ctlscript.sh stop php-fpm
cd /tmp/
sudo rm -rf /tmp/aws-moodle
sudo touch /opt/version.txt && sudo echo '0.3.0' >> /opt/version.txt # Remove after
sudo git config --global credential.helper '!aws codecommit credential-helper $@' && sudo git config --global credential.UseHttpPath true
git clone https://git-codecommit.us-east-1.amazonaws.com/v1/repos/aws-moodle

sudo cp -r /tmp/aws-moodle/theme/klass /opt/bitnami/apps/moodle/htdocs/klass

sudo rm -rf  /opt/bitnami/apps/moodle/htdocs/deployment_version/index.php
sudo cp -r /tmp/aws-moodle/deployment_version/index.php /opt/bitnami/apps/moodle/htdocs/deployment_version/index.php

sudo chown -R bitnami:daemon /opt/bitnami/apps/moodle
sudo /opt/bitnami/ctlscript.sh start apache && sudo /opt/bitnami/ctlscript.sh start php-fpm