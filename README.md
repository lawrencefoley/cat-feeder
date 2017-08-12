# Cat Feeder

This is a simple application that is used to feed your cat (or any other pet!) at scheduled times every day.
It is built using the Raspberry Pi Zero-W using an electric motor and a cereal dispenser.

## Installation
```
git clone https://github.com/lawrencefoley/cat-feeder.git
cd cat-feeder
chmod +x setup
sudo ./setup
```
Add your user to the video group to use the webcam
```
usermod -a -G video <username-here>
```
Copy the supervisor config file
Note: you will need to modify this conf file based on your username, etc
```
cp cat-feeder.conf /etc/supervisor/conf.d/cat-feeder.conf
```
Update supervisor's apps and start the app
```
sudo supervisorctl reread 
sudo supervisorctl update
sudo supervisorctl start cat-feeder
```
## TODO
- Add hardware build instructions

## History
### 2017-08-12
- Added support for mutliple quarter cups of food.
- Added webcam functionality to take a picture of food bowl after feeding.
