#!/bin/sh
sudo rm /etc/nginx/sites-enabled/DTEnginx
sudo cp DTEnginx /etc/nginx/sites-available/
sudo ln -s /etc/nginx/sites-available/DTEnginx /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx