# Note:
# This file is maintained in the openstack-ansible-tests repository.
# https://git.openstack.org/cgit/openstack/openstack-ansible-tests/tree/Vagrantfile
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
  end

  config.vm.synced_folder ".", "/vagrant", type: "rsync"

  config.vm.provision "shell",
      privileged: false,
      inline: <<-SHELL
          cd /vagrant
         ./run_tests.sh
      SHELL

  config.vm.define "ubuntu1604" do |xenial|
    xenial.vm.box = "bento/ubuntu-16.04"
  end

  config.vm.define "opensuse423" do |leap423|
    leap423.vm.box = "bento/opensuse-leap-42.3"
  end

  config.vm.define "centos7" do |centos7|
    centos7.vm.box = "bento/centos-7"
  end

end
