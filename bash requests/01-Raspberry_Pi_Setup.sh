#Bash SSH into your Raspberry Pi

# Update Raspberry Pi
sudo apt update
sudo apt upgrade -y

# Enable Camera
sudo raspi-config
# Interface Options -> Camera -> Enable
# Reboot afterwards

sudo reboot

# Install camera software
sudo apt install -y python3-picamera2 python3-opencv python3-flask git

# Make project folder
mkdir ~/eclipse_lamp
cd ~/eclipse_lamp

# Create Python virtual environment
python3 -m venv venv
source venv/bin/activate

# Increase swap space for torch installation
sudo dphys-swapfile swapoff
sudo sed -i 's/CONF_SWAPSIZE=.*/CONF_SWAPSIZE=1024/' /etc/dphys-swapfile
sudo dphys-swapfile setup
sudo dphys-swapfile swapon

# If picamera2 gives errors
sudo apt install python3-picamera2
