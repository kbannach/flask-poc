$script = <<-SCRIPT
sudo apt-get update
sudo apt-get install --assume-yes python-pip
pip install flask
pip install -U googlemaps
export FLASK_APP=flaskr
export FLASK_ENV=development
export APP_CONFIG_FILE=/workspace/flaskr/config.cfg
# use this alias to start a flask application server with the access from the host machine
alias frun='flask run --host=192.168.50.4' >> /home/vagrant/.bash_aliases
echo "alias frun='flask run --host=192.168.50.4'" >> /home/vagrant/.bash_aliases
chown vagrant /home/vagrant/.bash_aliases
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
    v.cpus = 2
  end

  config.vm.network "private_network", ip: "192.168.50.4"
  config.vm.synced_folder '.', '/workspace'
  config.vm.provision "shell", inline: $script
end
