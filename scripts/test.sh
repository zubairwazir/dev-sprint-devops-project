#! bin/bash
sudo apt-get install python3-venv -y 
python3 -m venv venv 
source venv/bin/activate
pip3 install -r service_1/requirements.txt
python3 -m pytest service_1/tests/test_unit1.py --cov  
python3 -m pytest service_2/tests/test_unit2.py --cov
python3 -m pytest service_3/tests/test_unit3.py --cov 
python3 -m pytest service_4/tests/test_unit4.py --cov
python3 -m pytest --cov