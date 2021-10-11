#!/usr/bin/env python3

import flask
import RPi.GPIO as GPIO
import sys

#channel = 11
#GPIO.setmode(GPIO.BCM)  
# Setup your channel
#GPIO.setup(channel, GPIO.OUT)
#GPIO.output(channel, GPIO.LOW)

# To test the value of a pin use the .input method
#channel_is_on = GPIO.input(channel)  # Returns 0 if OFF or 1 if ON

#if channel_is_on:
    # Do something here

def get_gpio_state(pin):
    try:
        ret = {}
        if GPIO.gpio_function(pin) == 1:
            ret["mode"] = "input"
            GPIO.setup(pin, GPIO.IN)
        else:
            ret["mode"] = "output"
            GPIO.setup(pin, GPIO.OUT)
        ret["value"] = str(GPIO.input(pin))
    except:
        ret = {}
    return ret

def get_all_gpio_state():
    ret = {}
    for i in range(1, 41):
        pin_info = get_gpio_state(i)
        if pin_info:
            ret[str(i)] = pin_info
    return ret

def main():
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True

    @app.route('/', methods=['GET'])
    def home():
        return "lulu"
    
    @app.route('/gpio', methods=['GET'])
    def codes():
        return str(get_all_gpio_state())
    
    @app.route('/gpio/<pin>', methods=['GET'])
    def code(pin):
        return str(get_gpio_state(int(pin)))

    app.run(host="0.0.0.0")


if __name__ == '__main__':
    GPIO.setmode(GPIO.BOARD)
    #print(get_all_gpio_state())
    main()