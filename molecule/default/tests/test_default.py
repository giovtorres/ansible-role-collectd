import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_collectd_package(host):
    assert host.package("collectd").is_installed


def test_collectd_service(host):
    s = host.service("collectd")
    assert s.is_running
    assert s.is_enabled


def test_collectd_global_config(host):
    f = host.file("/etc/collectd.conf")
    assert f.exists
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644


def test_collectd_plugin_dir(host):
    f = host.file("/etc/collectd.d")
    assert f.exists
    assert f.is_directory
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755


def test_collectd_rrdtool_dir(host):
    f = host.file("/var/lib/collectd/rrd")
    assert f.exists
    assert f.is_directory
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o755
