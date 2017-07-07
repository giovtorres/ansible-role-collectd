# Ansible Role: collectd

[![Build Status](https://travis-ci.org/giovtorres/ansible-role-collectd.svg?branch=master)](https://travis-ci.org/giovtorres/ansible-role-collectd)

Installs and configures [collectd](https://collectd.org), the system statistics
collection daemon.  Supported on EL 6 and 7.

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

    collectd_conf_hostname: "{{ ansible_hostname }}"
    collectd_conf_fqdnlookup: "false"
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

#### Plugin cgroups

    collectd_plugin_cgroups: false
    #collectd_plugin_cgroups_cgroup:
    #  - "libvirt"
    collectd_plugin_cgroups_ignoreselected: "false"

#### Plugin conntrack

    collectd_plugin_conntrack: "false"

#### Plugin contextswitch

    collectd_plugin_contextswitch: false

#### Plugin cpu

    collectd_plugin_cpu: true
    collectd_plugin_cpu_reportbycpu: "true"
    collectd_plugin_cpu_reportbystate: "true"
    collectd_plugin_cpu_valuespercentage: "false"

#### Plugin cpufreq

    collectd_plugin_cpufreq: "false"

#### Plugin cpusleep

    collectd_plugin_cpusleep: "false"

#### Plugin csv

    collectd_plugin_csv: "false"

#### Plugin df

    collectd_plugin_df: false
    #collectd_plugin_df_devices:
    #  - /dev/sda1
    #collectd_plugin_df_mountpoints:
    #  - 192.168.0.2:/mnt/nfs
    #collectd_plugin_df_fstypes:
    #  - ext4
    collectd_plugin_df_ignoreselected: "false"
    collectd_plugin_df_reportbydevice: "false"
    collectd_plugin_df_reportinodes: "false"
    collectd_plugin_df_valuesabsolute: "true"
    collectd_plugin_df_valuespercentage: "false"

#### Plugin disk

    collectd_plugin_disk: false
    collectd_plugin_disk_disks:
      - "/^[hsv]d[a-z][0-9]?$/"
    collectd_plugin_disk_ignoreselected: "false"
    #collectd_plugin_disk_usebsdname: "false"
    #collectd_plugin_disk_udevnameattr: "DEVNAME"

#### Plugin dns

    collectd_plugin_dns: false
    #collectd_plugin_dns_interface: "eth0"
    #collectd_plugin_dns_ignoresourc: "192.168.0.1"
    collectd_plugin_dns_selectnumericquerytypes: "true"

#### Plugin entropy

    collectd_plugin_entropy: false

#### Plugin interface

    collectd_plugin_interface: true
    collectd_plugin_interface_interfaces:
      - "eth0"
    collectd_plugin_interface_ignoreselected: "false"
    collectd_plugin_interface_reportinactive: "true"
    #collectd_plugin_interface_uniquename: "false"

#### Plugin load

    collectd_plugin_load: true
    collectd_plugin_load_reportrelative: "false"

#### Plugin md

    collectd_plugin_md: false
    collectd_plugin_md_devices:
      - /dev/md0
    collectd_plugin_md_ignoreselected: "false"

#### Plugin memory

    collectd_plugin_memory: true
    collectd_plugin_memory_valuesabsolute: "true"
    collectd_plugin_memory_valuespercentage: "false"

#### Plugin nfs

    collectd_plugin_nfs: false

#### Plugin ntpd

    collectd_plugin_ntpd: false
    collectd_plugin_ntpd_host: ""
    collectd_plugin_ntpd_reverselookups: "false"
    collectd_plugin_ntpd_includeunitid: "true"

#### Plugin numa

    collectd_plugin_numa: false

#### Plugin processes

    collectd_plugin_processes: false
    #collectd_plugin_processes_processes:
    #  - name
    #collectd_plugin_processes_processmatches:
    #  - name: foo
    #    regex: /foo/
    #collectd_plugin_processes_collectcontextswitch: "false"

#### Plugin protocols

    collectd_plugin_protocols: false
    collectd_plugin_protocols_values:
      - "/^Tcp:/"
    collectd_plugin_protocols_ignoreselected: "false"

#### Plugin rrdtool

    collectd_plugin_rrdtool: true
    collectd_plugin_rrdtool_datadir: {{ collectd_conf_basedir }}/rrd
    collectd_plugin_rrdtool_createfileasync: "false"
    collectd_plugin_rrdtool_cachetimeout: 120
    collectd_plugin_rrdtool_cacheflush: 900
    collectd_plugin_rrdtool_writepersecond: 50

#### Plugin statsd

    collectd_plugin_statsd: false
    collectd_plugin_statsd_host: "::"
    collectd_plugin_statsd_port: "8125"
    collectd_plugin_statsd_deletecounters: "false"
    collectd_plugin_statsd_deletetimers: "false"
    collectd_plugin_statsd_deletegauges: "false"
    collectd_plugin_statsd_deletesets: "false"
    collectd_plugin_statsd_countersum: "false"
    #collectd_plugin_statsd_timerpercentiles:
    #  - 90.0
    #  - 95.0
    #  - 99.0
    collectd_plugin_statsd_timerlower: "false"
    collectd_plugin_statsd_timerupper: "false"
    collectd_plugin_statsd_timersum: "false"
    collectd_plugin_statsd_timercount: "false"

#### Plugin swap

    collectd_plugin_swap: false
    collectd_plugin_swap_reportbydevice: "false"
    collectd_plugin_swap_reportbytes: "false"
    collectd_plugin_swap_valuesabsolute: "true"
    collectd_plugin_swap_valuespercentage: "false"

#### Plugin tcpconns

    collectd_plugin_tcpconns: false
    collectd_plugin_tcpconns_listeningports: "false"
    #collectd_plugin_tcpconns_localport: ""
    #collectd_plugin_tcpconns_remoteport: ""
    collectd_plugin_tcpconns_allportssummary: "false"

#### Plugin write_graphite

    collectd_plugin_write_graphite: false
    #collectd_plugin_write_graphite_nodes:
    #  - node: example
    #    host: localhost
    #    port: 2003
    #    protocol: tcp
    #    reconnectinterval: 0
    #    logsenderrors: "true"
    #    prefix: "collectd"
    #    postfix: "collectd"
    #    escapecharacter: "_"
    #    storerates: "true"
    #    alwaysappendds: "false"
    #    preserveseparator: "false"
    #    dropduplicatefields: "false"

#### Plugin write_http

    collectd_plugin_write_http: false
    #collectd_plugin_write_http_nodes:
    #  - node: example
    #    url: http://example.com/collectd-post
    #    user: collectd
    #    password: foo
    #    verifypeer: "true"
    #    verifyhost: "true"
    #    cacert: /etc/pki/tls/certs/ca-bundle.crt
    #    capath: /etc/pki/tls/certs
    #    clientkey: /etc/pki/tls/certs/localhost.key
    #    clientcert: /etc/pki/tls/certs/localhost.crt
    #    clientkeypass: secret
    #    headers:
    #      - "X-Custom-Header: custom_value"
    #    sslversion: TLSv1
    #    format: Command
    #    metrics: "true"
    #    notifications: "false"
    #    storerates: "false"
    #    buffersize: 4096
    #    lowspeedlimit: 0
    #    timeout: 0
    #    loghttperror: "false"

#### Plugin write_prometheus

    collectd_plugin_write_prometheus: false
    collectd_plugin_write_prometheus_port: "9103"
    #collectd_plugin_write_prometheus_stalenessdelta: "300"

#### Plugin uptime

    collectd_plugin_uptime: false

#### Plugin users

    collectd_plugin_users: false

#### Plugin vmem

    collectd_plugin_vmem: false
    collectd_plugin_vmem_verbose: "false"

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
