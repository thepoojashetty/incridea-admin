from python:3.5-onbuild

cmd rm -rf /usr/src/app
copy . /usr/src/app