#!/usr/bin/python
'''*****************************************************************************************************************
    Pi Remind (Pimoroni Blinkt version)
    By John M. Wargo
    www.johnwargo.com

    This application connects to a Google Calendar and determines whether there are any appointments in the next
    few minutes and flashes some LEDs if there are. The project uses a Raspberry Pi Zero W device with a Pimoroni
    Blinkt LED Display board to display an obnoxious reminder every minute, changing color at 10 minutes (WHITE),
    5 minutes (YELLOW) and 2 minutes (RED?).

    Google Calendar example code: https://developers.google.com/google-apps/calendar/quickstart/python
    Unicorn HAT example code: https://github.com/pimoroni/unicorn-hat/tree/master/python/examples
********************************************************************************************************************'''

from __future__ import print_function

import datetime
import os
import random
import sys
import time

import blinkt as lights
import httplib2
import oauth2client
import pytz
from apiclient import discovery
from dateutil import parser
from oauth2client import client
from oauth2client import tools

try:
    import argparse

    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

# Google says: If modifying these scopes, delete your previously saved credentials at ~/.credentials/client_secret.json
# On the pi, it's in /root/.credentials/
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Pi Remind'
CALENDAR_ID = 'primary'
HASH = '#'
HASHES = '########################################'

# Reminder thresholds
FIRST_THRESHOLD = 5  # minutes, WHITE lights before this
# RED for anything less than (and including) the second threshold
SECOND_THRESHOLD = 2  # minutes, YELLOW lights before this

# COLORS
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 127, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)

# constants used in the app to display status
CHECKING_COLOR = BLUE
SUCCESS_COLOR = GREEN
FAILURE_COLOR = RED


def all_off():
    lights.set_all(0, 0, 0)
    lights.show()


def all_on(color):
    lights.set_all(color[0], color[1], color[2])
    lights.show()


def flash(flash_count, delay, color):
    # light all of the LEDs in a RGB single color. Repeat 'flash_count' times
    # keep illuminated for 'delay' value
    for index in range(flash_count):
        all_on(color)
        time.sleep(delay)
        all_off()
        time.sleep(delay)


def do_random(flash_count, delay):
    for index in range(flash_count):
        for i in range(8):
            lights.set_pixel(i, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        lights.show()
        time.sleep(delay)


def zip_zip(flash_count, color):
    all_off()
    for index in range(flash_count):
        for y in range(4):
            lights.set_pixel(y, color[0], color[1], color[2])
            lights.set_pixel(7 - y, color[0], color[1], color[2])
            lights.show()
            time.sleep(.1)
        for y in range(4):
            lights.set_pixel(y, BLACK[0], BLACK[1], BLACK[2])
            lights.set_pixel(7 - y, BLACK[0], BLACK[1], BLACK[2])
            lights.show()
            time.sleep(.1)


# def up_down(color, delay):
#     # An interesting pattern, I decided not to use it
#     for y in range(8):
#         lights.set_pixel(7 - y, color[0], color[1], color[2])
#         lights.show()
#         time.sleep(delay)
#     for y in range(8):
#         lights.set_pixel(y, BLACK[0], BLACK[1], BLACK[2])
#         lights.show()
#         time.sleep(delay)


def set_activity_light(color, increment):
    # used to turn on one LED at a time across the row of lights. The app uses this as an unobtrusive
    # indicator when it connects to Google to check the calendar. Its intended as a subtle reminder that things
    # are still working.
    global current_activity_light
    # turn off (clear) any lights that are on
    all_off()
    if increment:
        # OK. Which light will we be illuminating?
        if current_activity_light < 1:
            # start over at the beginning when you're at the end of the row
            current_activity_light = 8
        # increment the current light (to the next one)
        current_activity_light -= 1
    # set the pixel color
    lights.set_pixel(current_activity_light, color[0], color[1], color[2])
    # show the pixel
    lights.show()


def get_credentials():
    # taken from https://developers.google.com/google-apps/calendar/quickstart/python
    global credentials
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        print('Creating', credential_dir)
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'pi_remind.json')
    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else:  # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to', credential_path)
    return credentials


def has_reminder(event):
    # Return true if there's a reminder set for the event
    # First, check to see if there is a default reminder set
    # Yes, I know I could have done this and the next check without using variables
    # this approach just makes the code easier to understand
    has_default_reminder = event['reminders'].get('useDefault')
    if has_default_reminder:
        # if yes, then we're good
        return True
    else:
        # are there overrides set for reminders?
        overrides = event['reminders'].get('overrides')
        if overrides:
            # OK, then we have a reminder to use
            return True
    # if we got this far, then there must not be a reminder set
    return False


def get_next_event(search_limit):
    # modified from https://developers.google.com/google-apps/calendar/quickstart/python
    # get all of the events on the calendar from now through 10 minutes from now
    print(datetime.datetime.now(), 'Getting next event')
    # this 'now' is in a different format (UTC)
    now = datetime.datetime.utcnow()
    then = now + datetime.timedelta(minutes=search_limit)
    # turn on a sequential CHECKING_COLOR LED to show that you're requesting data from the Google Calendar API
    set_activity_light(CHECKING_COLOR, True)
    try:
        # ask Google for the calendar entries
        events_result = service.events().list(
            # get all of them between now and 10 minutes from now
            calendarId=CALENDAR_ID,
            timeMin=now.isoformat() + 'Z',
            timeMax=then.isoformat() + 'Z',
            singleEvents=True,
            orderBy='startTime').execute()
        # turn on the SUCCESS_COLOR LED so you'll know data was returned from the Google calendar API
        set_activity_light(SUCCESS_COLOR, False)
        # Get the event list
        event_list = events_result.get('items', [])
        # did we get a return value?
        if not event_list:
            # no? Then no upcoming events at all, so nothing to do right now
            print(datetime.datetime.now(), 'No entries returned')
            return None
        else:
            # what time is it now?
            current_time = pytz.utc.localize(datetime.datetime.utcnow())
            # loop through the events in the list
            for event in event_list:
                # we only care about events that have a start time
                start = event['start'].get('dateTime')
                # return the first event that has a start time
                # so, first, do we have a start time for this event?
                if start:
                    # When does the appointment start?
                    # Convert the string it into a Python dateTime object so we can do math on it
                    event_start = parser.parse(start)
                    # does the event start in the future?
                    if current_time < event_start:
                        # only use events that have a reminder set
                        if has_reminder(event):
                            # no? So we can use it
                            event_summary = event['summary'] if 'summary' in event else 'No Title'
                            print('Found event:', event_summary)
                            print('Event starts:', start)
                            # figure out how soon it starts
                            time_delta = event_start - current_time
                            # Round to the nearest minute and return with the object
                            event['num_minutes'] = time_delta.total_seconds() // 60
                            return event
    except:
        # well, something went wrong
        # not much else we can do here except to skip this attempt and try again later
        print('Error connecting to calendar:', sys.exc_info()[0], '\n')
        # light up the array with FAILURE_COLOR LEDs to indicate a problem
        flash(1, 2, FAILURE_COLOR)
        # now set the current_activity_light to FAILURE_COLOR to indicate an error state
        # with the last reading
        set_activity_light(FAILURE_COLOR, False)

    # if we got this far and haven't returned anything, then there's no appointments in the specified time
    # range, or we had an error, so...
    return None


def main():
    # initialize the lastMinute variable to the current time to start
    last_minute = datetime.datetime.now().minute
    # on startup, just use the previous minute as lastMinute
    if last_minute == 0:
        last_minute = 59
    else:
        last_minute -= 1

    # infinite loop to continuously check Google Calendar for future entries
    while 1:
        # get the current minute
        current_minute = datetime.datetime.now().minute
        # is it the same minute as the last time we checked?
        if current_minute != last_minute:
            # reset last_minute to the current_minute, of course
            last_minute = current_minute
            # we've moved a minute, so we have work to do
            # get the next calendar event (within the specified time limit [in minutes])
            next_event = get_next_event(10)
            # do we get an event?
            if next_event is not None:
                num_minutes = next_event['num_minutes']
                if num_minutes != 1:
                    print('Starts in', int(num_minutes), 'minutes\n')
                else:
                    print('Starts in 1 minute\n')
                # is the appointment between 10 and 5 minutes from now?
                if num_minutes >= FIRST_THRESHOLD:
                    # Flash the lights in WHITE
                    flash(1, 0.25, WHITE)
                    # set the activity light to WHITE as an indicator
                    set_activity_light(WHITE, False)
                # is the appointment less than 5 minutes but more than 2 minutes from now?
                elif num_minutes > SECOND_THRESHOLD:
                    # Flash the lights YELLOW
                    flash(2, 0.25, YELLOW)
                    # set the activity light to YELLOW as an indicator
                    set_activity_light(YELLOW, False)
                # hmmm, less than 2 minutes, almost time to start!
                else:
                    # flash the lights in random colors
                    do_random(int(4 - num_minutes) * 2, .5)
                    # set the activity light
                    set_activity_light(ORANGE, False)
        # wait a second then check again
        time.sleep(1)


# now tell the user what we're doing...
print('\n')
print(HASHES)
print(HASH, 'Pi Remind (Zero W & Blinkt)         ', HASH)
print(HASH, 'By John M. Wargo (www.johnwargo.com)', HASH)
print(HASHES)

# Initialize the Google Calendar API stuff
credentials = get_credentials()
http = credentials.authorize(httplib2.Http())
service = discovery.build('calendar', 'v3', http=http)

print("Setting Blinkt settings")
# set LED brightness to half
lights.set_brightness(0.25)
# clears the LEDs when the application closes
lights.set_clear_on_exit()

# flash some LEDs just for fun...
# lets the user know the hardware is working
zip_zip(1, RED)
zip_zip(1, GREEN)
zip_zip(1, BLUE)

# The app flashes a GREEN light in the first row every time it connects to Google to check the calendar.
# The LED increments every time until it gets to the other side then starts over at the beginning again.
# The current_activity_light variable keeps track of which light lit last. At start it's at -1 and goes from there.
current_activity_light = 8
set_activity_light(SUCCESS_COLOR, True)

print('\nApplication initialized\n')

# Now see what we're supposed to do next
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nExiting application\n')
        sys.exit(0)
