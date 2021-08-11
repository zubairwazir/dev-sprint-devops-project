#!/bin/bash
sudo apt-get udpate 
sudo apt-get install python3 python3-pip python3-venv python3-pytest
pip3 install-r $WORKSPACE/service_1/requirements.txt $WORKSPACE/service_2/requirements.txt $WORKSPACE/service_3/requirements.txt $WORKSPACE/service_4/requirements.txt
bash $WORKSPACE/scripts/build.sh
