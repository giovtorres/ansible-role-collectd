import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_collectd_socket(host):
    assert host.socket("udp://ff18::efc0:4a42:25826").is_listening
    assert host.socket("udp://239.192.74.66:25826").is_listening
