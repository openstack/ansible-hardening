# Note:
# This file is maintained in the openstack-ansible-tests repository.
# https://opendev.org/openstack/openstack-ansible-tests/src/Vagrantfile
#
# If you need to perform any change on it, you should modify the central file,
# then, an OpenStack CI job will propagate your changes to every OSA repository
# since every repo uses the same Vagrantfile

# Verify whether required plugins are installed.
required_plugins = [ "vagrant-disksize" ]
required_plugins.each do |plugin|
  if not Vagrant.has_plugin?(plugin)
    raise "The vagrant plugin #{plugin} is required. Please run `vagrant plugin install #{plugin}`"
  end
end

Vagrant.configure(2) do |config|
  config.vm.provider "virtualbox" do |v|
    v.memory = 6144
    v.cpus = 2
    # https://github.com/hashicorp/vagrant/issues/9524
    v.customize ["modifyvm", :id, "--audio", "none"]
  end

  config.vm.synced_folder ".", "/vagrant", type: "rsync"

  config.vm.provision "shell",
      privileged: false,
      inline: <<-SHELL
          cd /vagrant
         ./run_tests.sh
      SHELL

  config.vm.define "centos8" do |centos8|
    centos8.vm.box = "centos/8"
  end

  config.vm.define "debian8" do |debian8|
    debian8.vm.box = "debian/jessie64"
  end

  config.vm.define "debian9" do |debian9|
    debian9.vm.box = "debian/stretch64"
  end

  config.vm.define "gentoo" do |gentoo|
    gentoo.vm.box = "generic/gentoo"
  end

  config.vm.define "opensuse150" do |leap150|
    leap150.vm.box = "opensuse/openSUSE-15.0-x86_64"
  end

  config.vm.define "opensuse151" do |leap151|
    leap151.vm.box = "opensuse/openSUSE-15.1-x86_64"
  end

  config.vm.define "ubuntu1804" do |bionic|
    bionic.disksize.size = "40GB"
    bionic.vm.box = "ubuntu/bionic64"
  end
end
