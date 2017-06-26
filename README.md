# Ansible Role: collectd

[![Build Status](https://travis-ci.org/giovtorres/ansible-role-collectd.svg?branch=master)](https://travis-ci.org/giovtorres/ansible-role-collectd)

Installs and configures [collectd](https://collectd.org), the system statistics
collection daemon.

This role uses the collectd yum repo available at
https://pkg.ci.collectd.org/rpm/collectd-5.7.

By default, this role enables the following read and write plugins:

- cpu           (read)
- interface     (read)
- load          (read)
- memory        (read)
- rrdtool       (write)

## Requirements

None.

## Role Variables

> The variables below are defaults for the role.  A commented out variable
> denotes that the variable is optional.

> To enable or disable a plugin, set the corressponding
> `collectd_plugin_<pluginname>` value to `true` or `false`.

Set collectd version.  Valid values are "5.4", "5.5", "5.6" and "5.7":

    collectd_version: "5.7"

Enable the collectd yum repo in /etc/yum.repos.d/collectd.repo:

    collectd_yum_repo_enabled: yes

The default global collectd configuration file:

    collectd_global_config: /etc/collectd.conf

Global settings for the daemon:

    #collectd_conf_hostname: {{ inventory_hostname }}
    collectd_conf_fqdnlookup: "true"
    collectd_conf_basedir: /var/lib/collectd
    collectd_conf_pidfile: /var/run/collectd.pid
    collectd_conf_plugindir: /usr/lib64/collectd
    collectd_conf_typesdb: /usr/share/collectd/types.db

When enabled, plugins are loaded automatically with the default options when an
appropriate <Plugin ...> block is encountered.  Disabled by default.

    collectd_conf_autoloadplugin: "false"

When enabled, internal statistics are collected, using "collectd" as the plugin
name.  Disabled by default:

    collectd_conf_collectinternalstats: "false"

Set the logging plugin.  Valid values are "syslog", "logfile" and "log_logstash":

    collectd_plugin_logging: syslog

Set the interval at which to query values:

    collectd_conf_interval: 10

Other daemon settings:

    collectd_conf_maxreadinterval: 86400
    collectd_conf_timeout: 2
    collectd_conf_readthreads: 5
    collectd_conf_writethreads: 5

Limit the size of the write queue. Default is no limit. Setting up a limit is
recommended for servers handling a high volume of traffic.

    #collectd_conf_writequeuelimithigh: 1000000
    #collectd_conf_writequeuelimitlow: 800000

Include all configuration files in this directory:

    collectd_conf_include_dir: /etc/collectd.d

### Plugin Configuration

See the online manpage for collectd.conf(5) at
https://collectd.org/documentation/manpages/collectd.conf.5.shtml for plugin
options.

#### Contextswitch Plugin

    collectd_plugin_contextswitch: false

#### CPU Plugin
    collectd_plugin_cpu: true
    collectd_plugin_cpu_reportbycpu: "true"
    collectd_plugin_cpu_reportbystate: "true"
    collectd_plugin_cpu_valuespercentage: "false"

#### DF Plugin

    collectd_plugin_df: false
    #collectd_plugin_df_device:
    #  - /dev/sda1
    #collectd_plugin_df_mountpoint:
    #  - 192.168.0.2:/mnt/nfs
    #collectd_plugin_df_fstype:
    #  - ext4
    collectd_plugin_df_ignoreselected: "false"
    collectd_plugin_df_reportbydevice: "false"
    collectd_plugin_df_reportinodes: "false"
    collectd_plugin_df_valuesabsolute: "true"
    collectd_plugin_df_valuespercentage: "false"

#### Disk Plugin

    collectd_plugin_disk: false
    collectd_plugin_disk_disk:
      - "/^[hsv]d[a-z][0-9]?$/"
    collectd_plugin_disk_ignoreselected: "false"
    #collectd_plugin_disk_usebsdname: "false"
    #collectd_plugin_disk_udevnameattr: "DEVNAME"

#### Interface Plugin

    collectd_plugin_interface: true
    collectd_plugin_interface_interface:
      - "eth0"
    collectd_plugin_interface_ignoreselected: "false"
    collectd_plugin_interface_reportinactive: "true"
    #collectd_plugin_interface_uniquename: "false"

#### Load Plugin

    collectd_plugin_load: true
    collectd_plugin_load_reportrelative: "false"

#### MD Plugin

    collectd_plugin_md: false
    collectd_plugin_md_device:
      - /dev/md0
    collectd_plugin_md_ignoreselected: "false"

#### Memory Plugin

    collectd_plugin_memory: true
    collectd_plugin_memory_valuesabsolute: "true"
    collectd_plugin_memory_valuespercentage: "false"

#### Processes Plugin

    collectd_plugin_processes: false
    #collectd_plugin_processes_process:
    #  - name
    #collectd_plugin_processes_processmatch:
    #  - name: foo
    #    regex: /foo/
    #collectd_plugin_processes_collectcontextswitch: "false"

#### Protocols Plugin

    collectd_plugin_protocols: false
    collectd_plugin_protocols_value:
      - "/^Tcp:/"
    collectd_plugin_protocols_ignoreselected: "false"

#### RRDTool Plugin

    collectd_plugin_rrdtool: true
    collectd_plugin_rrdtool_datadir: /var/lib/collectd/rrd
    collectd_plugin_rrdtool_createfileasync: "false"
    collectd_plugin_rrdtool_cachetimeout: 120
    collectd_plugin_rrdtool_cacheflush: 900
    collectd_plugin_rrdtool_writepersecond: 50

## Dependencies

- giovtorres.epel

## Example Playbook

    - hosts: servers
      vars:
        collectd_plugin_contextswitch: true
        collectd_plugin_df: true
        collectd_plugin_df_fstype:
          - xfs
        collectd_plugin_disk: true
        collectd_plugin_processes: true
        collectd_plugin_processes_process:
          - collectd
        collectd_plugin_protocols: true
      roles:
         - ansible-role-collectd

## License

BSD

## Testing

This role uses [Molecule](https://molecule.readthedocs.io/en/master/), Docker
and [Testinfra](https://testinfra.readthedocs.io/en/latest/index.html) for unit
tests.  After installing Molecule and Docker locally, run:

    molecule test

> Note: Molecule will install Testinfra as a dependency.
