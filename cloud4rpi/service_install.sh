#!/bin/bash

readonly PYTHON_PATH=/usr/bin/python

quit_on_error() {
    test "0" = $? || {
        exit 1
    }
}

put_systemd_script(){
    local INIT_MODULE_PATH=/lib/systemd/system/$1
    echo "Writing init script to $INIT_MODULE_PATH..."
    cat > "$INIT_MODULE_PATH" <<EOF
[Unit]
Description=Cloud4RPi daemon
After=network.target

[Service]
Type=idle
ExecStart=$PYTHON_PATH $SCRIPT_PATH

[Install]
WantedBy=multi-user.target
EOF
    quit_on_error

    echo "Setting permissions..."
    chmod 644 "$INIT_MODULE_PATH"
    quit_on_error
}

put_systemv_script(){
    local INIT_MODULE_PATH=/etc/init.d/$1
    echo "Writing init script to $INIT_MODULE_PATH..."
    cat > "$INIT_MODULE_PATH" <<EOF
#!/bin/sh

### BEGIN INIT INFO
# Provides:          cloud4rpi
# Required-Start:    \$local_fs \$network \$named \$time \$syslog
# Required-Stop:     \$local_fs \$network \$named \$time \$syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Cloud4RPi demon
# Description:       Cloud4RPi-enabled user script
#                    (https://cloud4rpi.io/)
### END INIT INFO

SCRIPT=$SCRIPT_PATH
RUNAS=root

PIDFILE=/var/run/cloud4rpi.pid
LOGFILE=/var/log/cloud4rpi.log

start() {
  if is_running; then
    echo 'Service is already running' >&2
    exit 1
  fi
  echo 'Starting service...' >&2

  # Clears the old log
  echo '--- Service started at' "\$(date)" '---' > "\$LOGFILE"

  sudo -u \$RUNAS $PYTHON_PATH -u "\$SCRIPT" >> \$LOGFILE 2>>\$LOGFILE &
  PID=\$!

  ERROR_LEVEL=0
  if [ -z \$PID ]; then
    echo 'Failed to run.' >&2
    ERROR_LEVEL=1
  else
    echo \$PID > "\$PIDFILE"
    echo 'Service started.' >&2
  fi
  echo 'See the log for details:' \$LOGFILE >&2
  exit \$ERROR_LEVEL
}

stop() {
  if ! is_running; then
    echo 'Service not running' >&2
    return 0
  fi
  echo 'Stopping service...' >&2
  
  if ! kill \$(cat "\$PIDFILE"); then
    echo 'Failed to stop.' >&2
    exit 1
  fi
  rm -f "\$PIDFILE"
  echo 'Service stopped' >&2
  echo '--- Service stopped at' "\$(date)" '---' >> "\$LOGFILE"
}

uninstall() {
  printf "Do you really want to uninstall Cloud4RPi service? That cannot be undone. [yes|no] "
  read -r REPLY
  if [ "\$REPLY" = "yes" ]; then
    stop
    echo "Notice: log file was not removed: '\$LOGFILE'" >&2
    update-rc.d -f cloud4rpi remove
    rm -fv "\$0"
  fi
}

is_running() {
    [ -f "\$PIDFILE" ] && ps \$(cat "\$PIDFILE") > /dev/null 2>&1
}

case "\$1" in
  start) start ;;
  stop) stop ;;
  uninstall) uninstall ;;
  restart) stop; start ;;
  status)
    if is_running; then
        echo "Running"
    else
        echo "Stopped"
        exit 1
    fi
    ;;
  *)
    echo "Usage: \$0 {start|stop|status|restart|uninstall}"
esac
EOF
    quit_on_error

    echo "Setting permissions..."
    chmod 755 "$INIT_MODULE_PATH"
    quit_on_error
}

install_sysv() {
    local SERVICE_NAME=cloud4rpi

    put_systemv_script $SERVICE_NAME

    echo "Installing init script links..."
    update-rc.d "$SERVICE_NAME" defaults
    quit_on_error

    echo "All done!"
    echo "Usage example:"
    echo -e "  $ sudo service \e[1m$SERVICE_NAME\e[0m start|stop|status|restart|uninstall"
}

install_sysd() {
    local SERVICE_NAME=cloud4rpi.service

    put_systemd_script $SERVICE_NAME

    echo "Configuring systemd..."
    systemctl daemon-reload
    systemctl enable "$SERVICE_NAME"
    quit_on_error

    echo "All done!"
    echo "Usage example:"
    echo -e "  $ sudo systemctl start|stop|status \e[0m$SERVICE_NAME\e[1m"
}

main() {
    SCRIPT_PATH=$(readlink -f "$1")

    if [ ! -f "$SCRIPT_PATH" ]; then
        echo "Usage: sudo path/to/service_install.sh path/to/target_script.py"
        echo "Invalid script path. Make sure it exists."
        exit 1
    fi

    chmod +x "$SCRIPT_PATH"
    quit_on_error

    case $(ps -p 1 -o comm=) in
        "init") install_sysv ;;
        "systemd") install_sysd ;;
        *)
            echo "Unfortunately we can\'t automate service installation on your system."
            exit 1
    esac
    exit 0
}

main "$1"
