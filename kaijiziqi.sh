#!/bin/bash

LANG=en
for zou in `chkconfig --list|grep 3:on|awk '{print $1}'`;do chkconfig --level 3 $zou off;done
for zou in crond network rsyslog sshd ; do chkconfig --level 3 $zou on;done
chkconfig --list|grep 3:on
