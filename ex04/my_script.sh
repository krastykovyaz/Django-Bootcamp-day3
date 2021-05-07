#! /usr/local/bin/zsh

python3 -m venv django_venv
PWD=`pwd`
echo $PWD
activate () {
    source $PWD/django_venv/bin/activate
}
activate
python3 -m pip install -r requirement.txt