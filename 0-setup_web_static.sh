#!/usr/bin/env bash

if ! command -v nginx &> /dev/null; then
	sudo apt-get update -y
	sudo apt-get install nginx -y
fi

directory="/data/"
directory1="/data/web_static"
directory2="/data/web_static/releases/"
directory3="/data/web_static/shared/"
directory4="/data/web_static/releases/test/"
file="/data/web_static/releases/test/index.html"

if [ ! -d "$directory" ]; then
	sudo mkdir "$directory"
fi

if [ ! -d "$directory1" ]; then
	sudo mkdir "$directory1"
fi

if [ ! -d "$directory2" ]; then
	sudo mkdir "$directory2"
fi

if [ ! -d "$directory3" ]; then
	sudo mkdir "$directory3"
fi

if [ ! -d "$directory4" ]; then
	sudo mkdir "$directory4"
fi

sudo echo -e  "<html>
  <head>
  </head>
  <body>
    Alx School
  </body>
</html>" | sudo tee $file

sudo ln -sf $directory4 /data/web_static/current
sudo chown -R ubuntu:ubuntu $directory
file2="/etc/nginx/sites-available/default"
phrase="location /hbnb_static/{\n\talias /data/web_static/current/;\n}\n"
sudo sed -i "27i $phrase" $file2
sudo service nginx restart
