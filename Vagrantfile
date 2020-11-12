# -*- mode: ruby -*-
# vi: set ft=ruby :
default_box = "generic/opensuse42"

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.

  config.vm.define "infra" do |infra|
    infra.vm.box = default_box
    infra.vm.hostname = "infra"
    infra.vm.network 'private_network', ip: "192.168.0.200",  virtualbox__intnet: true
    infra.vm.network "forwarded_port", guest: 22, host: 2222, id: "ssh", disabled: true
    infra.vm.network "forwarded_port", guest: 22, host: 2000 # infra Node SSH
    infra.vm.network "forwarded_port", guest: 6443, host: 6443 # API Access
    infra.vm.network "forwarded_port", guest: 2181, host: 2181 # Zoo Keeper
    infra.vm.network "forwarded_port", guest: 9092, host: 9092 # kafka
    for p in 30000..30100 # expose NodePort IP's
      infra.vm.network "forwarded_port", guest: p, host: p, protocol: "tcp"
      end
    infra.vm.provider "virtualbox" do |v|
      v.memory = "3072"
      v.name = "infra"
      end
    infra.vm.provision "shell", inline: <<-SHELL
      sudo zypper refresh
      sudo zypper --non-interactive install bzip2
      sudo zypper --non-interactive install etcd
      curl -sfL https://get.k3s.io | sh -
    SHELL
  end

end
