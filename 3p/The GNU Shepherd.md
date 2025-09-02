---
title: "The GNU Shepherd"
source: "https://www.gnu.org/software/shepherd/"
author:
published:
created: 2025-05-17
description:
tags:
  - "clippings"
---
The Shepherd is a service manager written in [Guile Scheme](https://www.gnu.org/software/guile) that looks after the herd of daemons running on the system. It can be used as an “init” system (PID 1) and also by unprivileged users to manage per-user daemons. It supports several daemon startup mechanisms—including *inetd*, systemd-style *socket activation*, and *timers* —and comes with a handy [collection of services](https://www.gnu.org/software/shepherd/manual/html_node/Service-Collection.html): syslog, log rotation, and more. The Shepherd is configured in Guile Scheme and can be extended in the same language. It builds on a simple memory-safe and callback-free programming model.

The Shepherd is developed jointly with [Guix](https://guix.gnu.org/). It runs as PID 1 on [Guix System](https://guix.gnu.org/manual/devel/en/html_node/Getting-Started-with-the-System.html) and manages user services for [Guix Home](https://guix.gnu.org/manual/devel/en/html_node/Home-Configuration.html).

[Try it!](https://www.gnu.org/software/shepherd/download)

## What does it look like?

The [`herd`](https://www.gnu.org/software/shepherd/manual/html_node/Invoking-herd.html) command interacts with a running [`shepherd`](https://www.gnu.org/software/shepherd/manual/html_node/Invoking-shepherd.html) process; as a user or system administrator, it is your entry point to service management:

```shell
$ sudo herd status tor
● Status of tor:
  It is running since Mon 02 Dec 2024 09:06:26 AM CET (3 days ago).
  Main PID: 257
  Command: /gnu/store/r6yp8g0mjxmdd26hvl01byp2zm41bj5h-tor -f /gnu/store/aj4qbf1rmk1bhn48alfmnwh018k48hw0-torrc
  It is enabled.
  Provides: tor
  Requires: user-processes loopback syslogd
  Custom action: configuration
  Will be respawned.

Recent messages (use '-n' to view more or less):
  2024-12-04 20:16:28 Dec 04 20:16:28.000 [notice] We now have enough directory information to build circuits.
  2024-12-04 21:23:25 Dec 04 21:23:25.000 [notice] Heartbeat: Tor's uptime is 1 day 17:59 hours, with 18 circuits open. I've sent 53.59 MB and received 272.47 MB. I've received 1732 connections on IPv4 and 0 on IPv6. I've made 45 connections with IPv4 and 0 with IPv6.
  2024-12-04 21:23:25 Dec 04 21:23:25.000 [notice] While not bootstrapping, fetched this many bytes: 355778 (consensus network-status fetch); 789909 (microdescriptor fetch)
```
```
$ sudo herd status tor
● Status of tor:
  It is running since Mon 02 Dec 2024 09:06:26 AM CET (3 days ago).
  Main PID: 257
  Command: /gnu/store/r6yp8g0mjxmdd26hvl01byp2zm41bj5h-tor -f /gnu/store/aj4qbf1rmk1bhn48alfmnwh018k48hw0-torrc
  It is enabled.
  Provides: tor
  Requires: user-processes loopback syslogd
  Custom action: configuration
  Will be respawned.

Recent messages (use '-n' to view more or less):
  2024-12-04 20:16:28 Dec 04 20:16:28.000 [notice] We now have enough directory information to build circuits.
  2024-12-04 21:23:25 Dec 04 21:23:25.000 [notice] Heartbeat: Tor's uptime is 1 day 17:59 hours, with 18 circuits open. I've sent 53.59 MB and received 272.47 MB. I've received 1732 connections on IPv4 and 0 on IPv6. I've made 45 connections with IPv4 and 0 with IPv6.
  2024-12-04 21:23:25 Dec 04 21:23:25.000 [notice] While not bootstrapping, fetched this many bytes: 355778 (consensus network-status fetch); 789909 (microdescriptor fetch)
```
```
$ herd status log-rotation 
● Status of log-rotation:
  It is running since 05:59:48 PM (6 hours ago).
  Timed service.
  Periodically running Scheme code.
  It is enabled.
  Provides: log-rotation
  Custom actions: trigger files
  Will not be respawned.

Upcoming timer alarms:
  Sun 08 Dec 2024 10:00:00 PM CET (in 4 days)
  Sun 15 Dec 2024 10:00:00 PM CET (in 11 days)
  Sun 22 Dec 2024 10:00:00 PM CET (in 18 days)
  Sun 29 Dec 2024 10:00:00 PM CET (in 25 days)
  Sun 05 Jan 2025 10:00:00 PM CET (in 32 days)
```
```
$ sudo herd status system-log
● Status of system-log:
  It is running since Mon 02 Dec 2024 09:06:23 AM CET (3 days ago).
  Running value is "#<system-log 7fcb03a9fb00>".
  It is enabled.
  Provides: system-log syslogd
  Will not be respawned.
  Log files: /var/log/messages /dev/tty12 /var/log/debug /var/log/secure /dev/console

Recent messages (use '-n' to view more or less):
  2024-12-04 23:43:08 localhost shepherd[1]: /var/log/ntpd.log  ntpd
  2024-12-04 23:43:08 localhost shepherd[1]: /var/log/guix-daemon.log   guix-daemon
  2024-12-04 23:43:08 localhost sudo: pam_unix(sudo:session): session closed for user root
  2024-12-04 23:44:21 localhost sudo:     ludo : TTY=pts/0 ; PWD=/home/ludo/src/guix ; USER=root ; COMMAND=/home/ludo/.guix-home/profile/bin/herd status system-log
  2024-12-04 23:44:21 localhost sudo: pam_unix(sudo:session): session opened for user root(uid=0) by (uid=1000)
```
```
# herd files log-rotation
/var/log/messages       system-log
/dev/tty12      system-log
/var/log/debug  system-log
/var/log/secure system-log
/dev/console    system-log
/var/log/guix-publish.log       guix-publish
/var/log/avahi-daemon.log       avahi-daemon
/var/log/dbus-daemon.log        dbus-system
/var/log/ntpd.log       ntpd
/var/log/guix-daemon.log        guix-daemon
```

As a system administrator or distro developer, you [define services](https://www.gnu.org/software/shepherd/manual/html_node/Defining-Services.html) in a configuration file written in Scheme:

```
(define sshd
  (service
    '(sshd ssh-daemon)                ;the secure shell daemon
    #:start (make-inetd-constructor   ;start on demand
             '("/usr/sbin/sshd" "-D" "-i")
             (list (endpoint
                    (make-socket-address AF_INET INADDR_ANY 22))
                   (endpoint
                    (make-socket-address AF_INET6 IN6ADDR_ANY 22)))
             #:max-connections 10)
    #:stop (make-inetd-destructor)
    #:respawn? #t))

(register-services (list sshd))
(start-in-the-background '(sshd))
```

New to Scheme? Get started in a few minutes with the [Scheme Crash Course](https://guix.gnu.org/cookbook/en/html_node/A-Scheme-Crash-Course.html).

From writing your configuration to extending the Shepherd, and from extending it to [contributing to it](https://www.gnu.org/software/shepherd/contribute), there’s only a small step. An entire [programming interface](https://www.gnu.org/software/shepherd/manual/html_node/Services.html) is at your disposal; if you’re adventurous, you can even [fiddle with a running `shepherd`](https://www.gnu.org/software/shepherd/manual/html_node/REPL-Service.html)! Concurrency in `shepherd` is made simple by [following the *concurrent sequential processes* (CSP) model](https://www.gnu.org/software/shepherd/manual/html_node/Service-Internals.html) using [Fibers](https://github.com/wingo/fibers/). Surely, that makes it the *coolest init system to hack on*.

## Licensing

The Shepherd is free software; you can redistribute it and/or modify it under the terms of the [GNU General Public License](https://www.gnu.org/licenses/gpl.html), version 3 or any later version.

## History

The Shepherd was formerly known as GNU dmd. dmd was initially developed by Wolfgang Jährling, with input from other GNU hackers. It was first released [in 2003](https://lists.gnu.org/archive/html/guile-user/2003-04/msg00007.html), making it one of the first init systems departing from the venerable System V approach. Its development was then closely related to the GNU Hurd, although it has always supported GNU/Linux as well.

After a looong period of freeze, it was [revived in 2013](https://lists.gnu.org/archive/html/guix-devel/2013-09/msg00168.html). It saw its [first positively-numbered release in December 2013](https://lists.gnu.org/archive/html/gnu-system-discuss/2013-12/msg00000.html). It has since been used as the init system (PID 1) of [Guix System](https://guix.gnu.org/).

In January 2016, GNU dmd was [renamed to GNU Shepherd](https://lists.gnu.org/archive/html/guix-devel/2016-01/msg00274.html) to avoid confusion with a same-named project.

## Credits

The Shepherd’s logo was designed by Luis Felipe López Acevedo. The [graphics](https://codeberg.org/shepherd/graphics) are Copyright © 2024 Luis Felipe López Acevedo and distributed under the terms of the [CC-BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

Stylesheet derived from earlier work by Ricardo Wurmus.