import argparse
import datetime
import time
import sys
import os

console_rows, console_columns = [int(x) for x in os.popen('stty size', 'r').read().split()]

output_method = None

def stdout_overwrite(s):
    sys.stdout.write(('\r' + s).ljust(console_columns+1,' '))

def valid_datetime(dt):
    for fmt in ('%Y-%m-%dT%H:%M', '%Y-%m-%dT%H:%M:%S',
                '%Y-%m-%d %H:%M', '%Y-%m-%d %H:%M:%S'):
        try:
            return datetime.datetime.strptime(dt, fmt)
        except ValueError:
            pass
    raise argparse.ArgumentTypeError("Invalid date: '{0}'.".format(dt))

def valid_date(d):
    t = 'T00:00'
    return valid_datetime(d + t)

def valid_time(t):
    d = datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%dT')
    return valid_datetime(d + t)

parser = argparse.ArgumentParser(description='Countdown to a specific date, or for a number of seconds.')

group_target = parser.add_mutually_exclusive_group(required=True)

group_target.add_argument('--to-datetime',
    metavar='YYYY-MM-DDTHH:MM:SS',
    type=valid_datetime,
    help='Countdown datetime - format YYYY-MM-DDTHH:MM(:SS)')

group_target.add_argument('--to-date',
    metavar='YYYY-MM-DD',
    type=valid_date,
    help='Countdown date - format YYYY-MM-DD')

group_target.add_argument('--to-time',
    metavar='HH:MM(:SS)',
    type=valid_time,
    help='Countdown time - formath HH:MM(:SS)')

group_target.add_argument('--seconds',
    metavar='<seconds>',
    type=int,
    help='Countdown number of seconds')

args = parser.parse_args()

seconds_time = None

cd_now = datetime.datetime.now()

if args.seconds is not None:
    seconds_time = cd_now + datetime.timedelta(0, args.seconds)

cd_target = args.to_datetime or args.to_date or args.to_time or seconds_time

cd_delta = cd_target - cd_now

if cd_delta.total_seconds() <= 0:
    parser.error("Target date or time should be in the future!")

days, hours, minutes, seconds = cd_delta.days, cd_delta.seconds // 3600, cd_delta.seconds // 60 % 60, cd_delta.seconds % 60

try:
    import scrollphat
    scrollphat.set_brightness(1)

    start_seconds = None

    def scrollphat_output(days, hours, minutes, seconds, total):
        global start_seconds
        start_seconds = start_seconds or total

        bar = int(5 * (float(total) / start_seconds))

        scrollphat.clear_buffer()
        s = str(seconds)
        indent = 2
        if len(s) == 1:
            indent = 4

        scrollphat.write_string(s, indent)

        for y in range(bar):
            scrollphat.set_pixel(0, y, 1)

        scrollphat.update()

    output_method = scrollphat_output
    print("Using Scroll pHAT")
except (ImportError, IOError):
    pass

print("Counting down {days} days, {hours} hours, {minutes} minutes and {seconds} seconds to {datetime}".format(
    datetime=datetime.datetime.strftime(cd_target,'%Y-%m-%dT%H:%M:%S'),
    days=days,
    hours=hours,
    minutes=minutes,
    seconds=seconds))

try:
    while cd_delta.total_seconds() > 0:
        days, hours, minutes, seconds = cd_delta.days, cd_delta.seconds // 3600, cd_delta.seconds // 60 % 60, cd_delta.seconds % 60

        stdout_overwrite("{days} days, {hours} hours, {minutes} minutes and {seconds} seconds remaining until {datetime}".format(
            datetime=datetime.datetime.strftime(cd_target,'%Y-%m-%dT%H:%M:%S'),
            days=days,
            hours=hours,
            minutes=minutes,
            seconds=seconds))
        sys.stdout.flush()

        if output_method is not None and callable(output_method):
            output_method(days, hours, minutes, seconds, cd_delta.total_seconds())

        cd_delta = cd_target - datetime.datetime.now()

        time.sleep(1)

    stdout_overwrite("Countdown reached!")

except KeyboardInterrupt:
    stdout_overwrite("Exiting!")
    pass

