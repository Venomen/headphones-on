#!/usr/local/bin/python3
# -*- encoding: utf-8 -*-
#
#  Copyright (c) 2020 - Dawid Deręgowski @ deregowski.net

import json
import urllib.parse
import urllib.request
import schedule
import sys
import configparser
import emoji

# loading config

status = ""
config = configparser.ConfigParser()
config.sections()
config.read('config.ini')

status_dump = config['python']['status_dump']
json_dump = config['python']['json_dump']
headphones = config['python']['headphones']

webhook_url = config['python']['webhook_url']
webhook_data_avatar = config['python']['webhook_data_avatar']
webhook_data_alias = config['python']['webhook_data_alias']
webhook_data_text = config['python']['webhook_data_text']

# main functions


def check_connection():
    connection_file = open(json_dump, 'r')
    conn_string = json.loads(open(json_dump).read())

    for key in conn_string['SPBluetoothDataType']:
        for value in key['device_title']:
            if headphones in value:
                if 'attrib_Yes' in value[headphones]['device_isconnected']:
                    global status
                    status = "connected"
                else:
                    status = "disconnected"
                    save_status_file = open(status_dump, 'w')
                    save_status_file.write("down")
                    save_status_file.close()

    connection_file.close()


def send_notification():

    read_status_file = open(status_dump, 'r')

    data = urllib.parse.urlencode(
        {"avatar": webhook_data_avatar,
         "alias": webhook_data_alias,
         "text": webhook_data_text})
    data = data.encode('ascii')

    if "disconnected" not in status and "sent" not in read_status_file:
        save_status_file = open(status_dump, 'w')
        save_status_file.write("sent")
        save_status_file.close()

        req = urllib.request.Request(webhook_url, data)
        with urllib.request.urlopen(req) as response:
            response.read()

    read_status_file.close()
    sys.exit(0)


# 1min check scheduler

schedule.every(1).seconds.do(check_connection)
schedule.every(1).seconds.do(send_notification)

# start all

if __name__ == '__main__':

    
    while True:
        try:
            schedule.run_pending()
        except urllib.error.URLError as e:
            ResponseData = e.read().decode("utf8", 'ignore')
            print("ERROR:", ResponseData)
        except ValueError:
            print("ERROR: Problem with dump.json!")
            sys.exit(1)
        except KeyboardInterrupt as e:
            print(emoji.emojize(':headphone:'), "headphones-on | Ctrl+C pressed. 1 more to exit!", emoji.emojize(':headphone:'))
            sys.exit(1)
