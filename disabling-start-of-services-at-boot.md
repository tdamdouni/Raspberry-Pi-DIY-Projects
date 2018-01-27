_https://raspberrypi.stackexchange.com/questions/26346/disabling-start-of-services-at-boot_

`update-rc.d -f the-service remove`

disable some services with `update-rc.d -f your-service-to-disable remove` or use crontab and put this in filename.sh then `service your-service-to-disable stop` and in crontab use `@reboot /path/to/filename.sh`