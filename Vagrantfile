$script = <<-SCRIPT
echo I am provisioning...
SCRIPT

Vagrant.configure("2") do |config|
  config.vm.box = "hashicorp/bionic64"
  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
    v.cpus = 2
  end
  config.vm.synced_folder '.', '/workspace'
  config.vm.provision "shell", inline: $script
end
