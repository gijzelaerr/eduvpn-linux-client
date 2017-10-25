# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/xenial64"
    config.vm.provision :shell, :path => "vagrant_provision.sh"
    config.ssh.forward_x11 = true
    config.vm.provider "virtualbox" do |v|
      v.memory = 2048 
      v.cpus = 2
    end
end
