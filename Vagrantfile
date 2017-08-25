# Verify whether required plugins are installed.
required_plugins = [ "vagrant-disksize" ]
required_plugins.each do |plugin|
  if not Vagrant.has_plugin?(plugin)
    raise "The vagrant plugin #{plugin} is required. Please run `vagrant plugin install #{plugin}`"
  end
end

Vagrant.configure(2) do |config|
  config.vm.provider "virtualbox" do |v|
    v.memory = 2048
    v.cpus = 2
  end

  config.vm.provision "shell",
      privileged: false,
      inline: <<-SHELL
          cd /vagrant
         ./run_tests.sh
      SHELL

  config.vm.define "ubuntu1404" do |trusty|
    trusty.disksize.size = "40GB"
    trusty.vm.box = "ubuntu/trusty64"
  end

  config.vm.define "ubuntu1604" do |xenial|
    xenial.disksize.size = "40GB"
    xenial.vm.box = "ubuntu/xenial64"
  end

  config.vm.define "centos7" do |centos7|
    centos7.vm.box = "centos/7"
  end

end
