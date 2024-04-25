#!/bin/bash

#В системе должны быть ln -s в /usr/bin/pm2 /usr/bin/npm /usr/bin/node

pm2 stop all
cd /var/www/telmark-frontend/
sudo rm -rf telmark-frontend
sudo git clone https://gitlab.com/telmark/telmark-frontend.git --branch main
rm -rf /var/www/telmark-frontend/telmark-frontend/public/img2
sudo ln -s /home/ubuntu/img2 /var/www/telmark-frontend/telmark-frontend/public/img2
cp /home/ubuntu/favicon.ico /var/www/telmark-frontend/telmark-frontend/public
rm -rf /var/www/telmark-frontend/telmark-frontend/public/img2/img2
cd /var/www/telmark-frontend/telmark-frontend
npm install
npm install @next/bundle-analyzer
npm run build
pm2 start npm -- start
