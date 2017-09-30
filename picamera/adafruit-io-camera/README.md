# Adafruit IO Raspberry Pi Camera
A Node.js Adafruit IO CLI that allows you to send live images to Adafruit IO, with the
option to send images when motion is detected.

## Installation
Make sure you have [Node.js][1] **v4.0.0 or higher** installed on your Raspberry Pi.

```console
$ node -v
v4.0.0
```
Install `forever`, `forever-service`, and `adafruit-io-camera` on your Raspberry Pi using `npm`.

```console
$ npm install --global --no-optional forever forever-service adafruit-io-camera
```

## Usage

The camera commands will always be prefixed with `adafruit-io camera`, and you can append `help` to any
command to get more info about that command.

### Authentication

```console
$ adafruit-io camera config help
Usage: adafruit-io camera config [options]

Commands:
  help  Show help

Options:
  -u, --username  Adafruit IO Username                                [required]
  -k, --key       Adafruit IO Key                                     [required]
```

You can then use your Adafruit IO `username` and `key` to authenticate yourself.

```console
$ adafruit-io camera config --username testing_username --key xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### Commands

```console
$ adafruit-io camera help
Usage: adafruit-io camera <command> [options]

Commands:
  config   Configure Adafruit IO Auth
  install  Install camera service (linux only)
  remove   Remove camera service (linux only)
  start    Start camera daemon
  restart  Restart camera daemon
  stop     Stop camera daemon
  help     Show help

Options:
  -f, --feed       Adafruit IO Camera Feed Name               [default: "picam"]
  -m, --motion     Motion Tracking                   [boolean] [default: "true"]
  -t, --threshold  Motion Threshold                              [default: "21"]
  -c, --change     Motion Minimum Change                         [default: "10"]
  -s, --seconds    Motion Minimum Seconds                         [default: "1"]
  -r, --rate       Timelapse Capture Rate (seconds)               [default: "2"]
  -h, --hflip      Camera Horizontal Flip           [boolean] [default: "false"]
  -v, --vflip      Camera Vertical Flip             [boolean] [default: "false"]
```

**Starting the Daemon:**
```console
$ adafruit-io camera start
                                      ▄▄
                                    ▄████
                                  ▄███████
                                 █████████▌
                                ███████████
                               ████████████▌
              ███████████████▄ ████████████▌
               █████████████████████▀▀█████ ▄▄▄▄▄▄▄
                ▐██████████████████   █████████████████▄▄
                  ▀█████████  ▀▀███  ██████████████████████
                    █████████▄▄  ▐████▀    ▐█████████████▀
                      ▀▀███████████████▄▄█████████████▀
                       ▄███████   ██  ▀████████████▀
                      ███████▀  ▄████  ▐█████▄
                     █████████████████▄▄██████▄
                    ███████████████████████████
                   ██████████████ ▐████████████▌
                  ▐██████████▀▀    ▀███████████▌
                  █████▀▀            ▀█████████▌
                                        ▀██████
                                           ▀███
----------------------------------------------------------------------
                           adafruit io
----------------------------------------------------------------------
[info] starting camera...
[info] camera daemon started and is pushing images to Adafruit IO
```

**Stopping the Daemon:**
```console
$ adafruit-io camera stop
[info] stopping camera...
```

**Starting the Daemon with Options:**
```console
$ adafruit-io camera start --motion --vflip --rate 2
                                      ▄▄
                                    ▄████
                                  ▄███████
                                 █████████▌
                                ███████████
                               ████████████▌
              ███████████████▄ ████████████▌
               █████████████████████▀▀█████ ▄▄▄▄▄▄▄
                ▐██████████████████   █████████████████▄▄
                  ▀█████████  ▀▀███  ██████████████████████
                    █████████▄▄  ▐████▀    ▐█████████████▀
                      ▀▀███████████████▄▄█████████████▀
                       ▄███████   ██  ▀████████████▀
                      ███████▀  ▄████  ▐█████▄
                     █████████████████▄▄██████▄
                    ███████████████████████████
                   ██████████████ ▐████████████▌
                  ▐██████████▀▀    ▀███████████▌
                  █████▀▀            ▀█████████▌
                                        ▀██████
                                           ▀███
----------------------------------------------------------------------
                           adafruit io
----------------------------------------------------------------------
[info] starting camera...
[info] camera daemon started and is pushing images to Adafruit IO
```

**Installing the Service with Options:**
This will start the camera service on boot.
```console
$ adafruit-io camera install --motion --hflip
                                      ▄▄
                                    ▄████
                                  ▄███████
                                 █████████▌
                                ███████████
                               ████████████▌
              ███████████████▄ ████████████▌
               █████████████████████▀▀█████ ▄▄▄▄▄▄▄
                ▐██████████████████   █████████████████▄▄
                  ▀█████████  ▀▀███  ██████████████████████
                    █████████▄▄  ▐████▀    ▐█████████████▀
                      ▀▀███████████████▄▄█████████████▀
                       ▄███████   ██  ▀████████████▀
                      ███████▀  ▄████  ▐█████▄
                     █████████████████▄▄██████▄
                    ███████████████████████████
                   ██████████████ ▐████████████▌
                  ▐██████████▀▀    ▀███████████▌
                  █████▀▀            ▀█████████▌
                                        ▀██████
                                           ▀███
----------------------------------------------------------------------
                           adafruit io
----------------------------------------------------------------------
[info] installing service...
[info] camera service is now installed and pushing images to Adafruit IO
```

## License
Copyright (c) 2015 [Adafruit Industries][2]. Licensed under the [MIT license][3].

[Adafruit][2] invests time and resources providing this open source code. Please support
Adafruit and open-source hardware by purchasing products from [Adafruit][2].


[1]: https://nodejs.org
[2]: https://adafruit.com
[3]: /LICENSE?raw=true
