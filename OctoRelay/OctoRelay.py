#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial
import time
import argparse
import command as com

port = 'com1'
baudrate = 9600
global maxCharCommand

def TurnOnOffLights(strCommand):
    relay = 0
    percentDeviation = 0.2

    print("[-] Command is --> Turn {} lights <--".format(strCommand))
    print("[-] Start Process...")
    print("[-] Relay number is: {}".format(relay))

    if (strCommand == "Off" or strCommand == "off"):
        print("[-] Send command to Arduino to get light sensor value.")
        resp = sendCommand("getLightSensorValue", "")
        print("[-] Recieve from Arduino light sensor value and save it.")
        brightness = int(resp)
        print("[-] Brightness value is: {}.".format(brightness))
        print("[-] Send turn off command to Arduino.")
        resp = sendCommand("turnOffLights", "")
        print("[-] Recieve turn off response off Arduino.")
        resp = sendCommand("getLightSensorValue", "")
        nBrightness  = int(resp)
        print("[-] New brightness value is: {}.".format(nBrightness))
        if ((abs(nBrightness - brightness) / brightness)>=percentDeviation):
            print ("[-] It's look like to have turn off lights.")
        else:
             print ("[-] It's look like still the lights are on.")

    elif (strCommand == "On" or strCommand == "on"):
        print("[-] Send command to Arduino to get light sensor value.")


def sendCommand(strCommand, value):
    response = 1
    objCommand = com.command(strCommand)
    objCommand.maxCharCommand = maxCharCommand
    objCommand.isValidCommand = com.commandValidation(objCommand.name)
    objCommand.value = com.makeCommandNameCompatible(value, maxCharCommand)
    objCommand.name = com.makeCommandNameCompatible(objCommand.name, maxCharCommand)
    if (objCommand.isValidCommand):
        ArduinoSerial = serial.Serial(port, baudrate)
        print(str(objCommand.name) + str(objCommand.value))
        ArduinoSerial.write(str.encode(str(objCommand.name) + str(objCommand.value)))
        time.sleep(2)
        #read response
        ArduinoSerial.close() 
    return response

if __name__ == "__main__":
    maxCharCommand = 30
    print("\nOctaRelay")
    parser = argparse.ArgumentParser()

    parser.add_argument("--TurnOnOffLights", type=str, dest="TurnOnOffLights",
                        help="Turn on/off the relay of led lights ")
    args = parser.parse_args()

    if args.TurnOnOffLights:
        TurnOnOffLights(args.TurnOnOffLights)