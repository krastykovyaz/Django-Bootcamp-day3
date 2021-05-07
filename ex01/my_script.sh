#! /usr/local/bin/zsh

pip -V
if [[ -d ./local_lib ]]
then
    echo "Crash, library has already been installed!"
else
    pip3 install -t local_lib git+https://github.com/jaraco/path.py.git > install.log
fi
echo "\n" 
python3 my_program.py