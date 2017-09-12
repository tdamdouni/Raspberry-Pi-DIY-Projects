README
======

What it is
----------

This project implements a systemd service polling one or more GPIO-pins
for an interrupt (i.e. a value change). For every interrupt, it either
calls a configured program, or writes the event into a fifo (pipe).

Technically, the service does not poll but uses the same named system-call,
so the service does not consume any ressources.


Version Juli 10, 2017
---------------------

  - new global configuration option *fifo*
  - new gpio-specific configuration option *bounce_time*
  - it is now possible to set global defaults for gpio-specific options


Version February 24, 2017
-------------------------

Initial version.

Installation
------------

The service is implemented in python 2 but has no additional prerequisites,
so a standard Raspbian installation will do fine.

To install the service, run

    git clone https://github.com/bablokb/gpio-poll-service
    cd gpio-poll-service
    sudo tools/install

This will install the necessary files and enable (but not start) the service.

To start the service (after proper configuration), run

    sudo systemctl start gpio-poll.service

This will also happen after a reboot automatically.


Configuration
-------------

To configure the service, you have to edit `/etc/gpio-poll.conf`. This file
has one `[GLOBAL]` section for

  - global options
  - defaults for gpio-specific options
  - list of gpios to monitor

Global options are:

  - `debug`: if set to `1`, the service will write various messages
     to the system log
  - `fifo`: if set to `1`, the service will write all events to the
     fifo `/var/run/gpio-poll.fifo` instead of executing gpio-specific
     commands

For every GPIO listed in the global section, you have to add an individual
section named `[GPIOxx]` with xx being the number of the GPIO. If you
omit the section, the service configures the global defaults for the pin.

The service supports the following parameters for every section:

  - `active_low`: this configures the value-state of the pin if set to low
  - `edge`: detect changes. Can be either `both`, `rising` or `falling`
  - `ignore_initial`: don't report initial state
  - `bounce_time`: if not null, ignore all events within the given time
     range in seconds for this pin.
  - `command`: the command to execute on interrupt (ignored if global option
     `fifo` is `1`)

For all these values you can set defaults in the global section. So if
you want to monitor multiple gpios and process them identically, you just
need to list the options once in the global section.

The `command` is called with four parameters:

  - the pin number
  - the current value (`0` or `1`).
  - the *switch time* (time since last interrupt with opposite value)
  - the *repeat time* (time since last interrupt with the same value)

If you use the timing values (e.g. to check if a button was pressed for
at least five seconds) you should apply some sanity checks. Timings of
the first reported interrupt are measured from service startup and are
therefore probably meaningless. Also, switch time is only relevant if
edge=both.

Be aware that time values are not strictly increasing and during system
startup you might have to expect larger jumps in time values
(especially if a Pi updates it's time via ntp).

Note that unless you set `ignore_initial: 1` the interrupt
will also trigger on startup and call the configured command.

Since the "edge"-configuration does not work without faults, the service
will filter all invalid values read from the GPIO (e.g. if edge==rsing it
will filter all states read with value=0).


Fifo mode vs. command mode
--------------------------

Using the global option `fifo` prevents the asynchronous execution of the
gpio-specific commands. All events are written in first-in-first-out order
to the fifo (pipe) `/var/run/gpio-poll.fifo`. To consume the events, create a
program that reads from the pipe and processes the events.

Since the gpio-poll service runs as root, all commands are executed with
root permission. Using a pipe, you can consume the events from programs
running with user-level permissions.

The directory `examples/fifo-test` contains a simple bash-script reading
from the named pipe.

Examples
--------

In the `examples`-directory you will find a script called `gpio-shutdown`.
This script will notify the desktop user of failing power supply and
initiate shutdown. If AC comes back soon enough, the script cancels
the shutdown and informs the user accordingly. You need of course some
additional electronics to monitor the power supply and set the appropriate
GPIO-pin for the service.

For the example to work, you have to install additional packages:

   sudo apt-get update
   sudo apt-get -y install libnotify-bin notification-daemon

You should also copy the `gpio-shutdown`-script to `/usr/local/sbin`
and configure the service as documented in the script.
