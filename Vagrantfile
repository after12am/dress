# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

$update_packages = <<SCRIPT

echo "Updating package..."
apt-get -y update >/dev/null 2>&1

SCRIPT

$install_databases = <<SCRIPT

echo "Installing SQLite3..."
apt-get -y install sqlite3 libsqlite3-dev >/dev/null 2>&1

echo "Installing PostgreSQL..."
apt-get -y install postgresql postgresql-contrib libpq-dev >/dev/null 2>&1
sudo -u postgres createuser --superuser vagrant

echo "Installing MySQL..."
debconf-set-selections <<< 'mysql-server mysql-server/root_password password root'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password root'
apt-get -y install mysql-server libmysqlclient-dev >/dev/null 2>&1

SCRIPT

# sudo apt-get install mysql-server

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = 'ubuntu/trusty32'
  config.vm.network :private_network, ip:"192.168.33.10"
  config.vm.provision "shell", inline: $update_packages
  config.vm.provision "shell", inline: $install_databases
end
