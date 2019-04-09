#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse

def TurnOnOffLedLights(command):
    #region Realays
    relay = 0
    #endregion

    #region Init Messages
    print("[-] Command is --> Turn {} lights <--".format(command))
    print("[-] Start Process...")
    print("[-] Relay number is: {}".format(relay))
    #endregion

    if (command == "Off" or command == "off"):
        print("[-] Send command to Arduino to get light sensor value.")
        #send command
        print("[-] Recieve from Arduino light sensor value and save it.")
        lummen = 0;
        print("[-] Send turn off command to Arduino.")
        print("[-] Recieve turn off response off Arduino.")
    elif (command == "On" or command == "on"):
        print("[-] Send command to Arduino to get light sensor value.")
        #send command
        print("[-] Recieve from Arduino light sensor value and save it.")

        print("[-] Send turn on command to Arduino.")
        print("[-] Recieve turn on response off Arduino.")

if __name__ == "__main__":

    print("\nOctaRelay")
    parser = argparse.ArgumentParser()

    parser.add_argument("--TurnOnOffLedLights", type=str, dest="TurnOnOffLedLights",
                        help="Turn on/off the relay of led lights ")
    args = parser.parse_args()

    if args.TurnOnOffLedLights:
        TurnOnOffLedLights(args.TurnOnOffLedLights)