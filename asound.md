This is a horrible, hacky, proof of concept mess for Pi VU Meter on Volumio
It details steps with the old phatmeter library, but should work with PiVuMeter too,
simply change "ameter" to "pivumeter" and link the right lib accordingly

# udev rules permissions

REQUIRED: Create `/etc/udev/rules.d/60-i2c.rules` with the contents:

```
KEREL=="i2c-1", GROUP="i2C", MODE="0777"
```

This allows MPD, which uses the `mpd` user and `sound` group, to gain access to the i2c bus.

# mpd config

There must be a better way to do this/let MPD run with both audio/i2c groups?

mpd.conf just has "device "softvolume"" specified with other options commented out. Throws errors about missing PCM but vol works.
`/boot/config.txt` must include: `dtoverlay=i2s-mmap` and `dtoverlay=hifiberry-dac`

# alsa config

Contents of `/etc/asound.conf` as follows:

```
ctl.!default {
        type hw
        card 1
}

pcm.dmixer {
        type dmix
        ipc_key 1024
        ipc_perm 0666
        slave.pcm 'hw:1,0'
        slave {
                period_time 0
                period_size 1024
                buffer_size 8192
        }
        bindings {
                0 0
                1 1
        }
}

ctl.dmixer {
        type hw
        card 1
}

pcm.softvolume {
        type meter
        slave.pcm "softvol"
        scopes.0 ameter
}

pcm.softvol {
        type softvol
        slave.pcm "dmixer"
        control {
                name "SoftMaster"
                card 1
                device 0
        }
}

pcm_scope.ameter {
        type ameter
        decay_ms 500
        peak_ms 400
        brightness 128
}

pcm_scope_type.ameter {
        lib /usr/local/lib/libphatmeter.so
}

pcm.ameter {
        type meter
        slave.pcm 'hw:1,0' #can be hw or hw:0,1 etc...
        scopes.0 ameter
}

pcm.dsp0 ameter
```