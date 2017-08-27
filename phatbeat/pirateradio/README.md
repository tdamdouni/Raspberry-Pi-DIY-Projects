# Interface for Pirate Radio Hardware

Couple of scripts for controlling the Pimoroni Pirate Radio hardware.

## Requirements

- MPD server (I set this up using mopidy)
- [Phat Beat driver](https://github.com/pimoroni/phat-beat)
- [Python MPD client](https://github.com/Mic92/python-mpd2) (installed globally)

# Installation

1. Copy `pirateradio` to `/usr/local/bin/pirateradio` with executable permission:

  ```sh
  $ sudo cp pirateradio /usr/local/bin/pirateradio
  $ sudo chmod ugo+x /usr/local/bin/pirateradio
  ```

2. Copy `pirateradio.service` to `/etc/systemd/system/pirateradio.service`

  ```sh
  $ sudo cp pirateradio.service /etc/systemd/system/pirateradio.service
  ```

3. Enable the pirate radio service.

  ```sh
  $ sudo systemctl enable pirateradio.service  # Will now load automatically on startup
  $ sudo systemctl start pirateradio.service  # To start it this time
  ```
