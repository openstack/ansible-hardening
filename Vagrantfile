# Sets up Ubuntu 14.04, downloads security-ansible, and runs it

Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = "sec-ansible-test"

  config.vm.provision "ansible" do |ansible|
    # ansible.verbose = "vvv"
    ansible.playbook = "tests/vagrant.yml"
    # we'll skip V-38496 because Vagrant itself creates the user that causes
    # this to fail
    ansible.skip_tags = ['V-38496']
    # we need to run as sudo for a lot of the checks ansible-security runs
    ansible.raw_arguments = ['-s']
  end
end
