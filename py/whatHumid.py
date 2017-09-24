#!/usr/bin/env python3

# whatHumid.py

from os import path


def whatHumid():
    # set the main loop count to 0
    i = 0

    # The main loop is set to 4, and may need to be increased. I have not seen
    # an EGW3K with more than 4 devices.
    while i < 4:

        folderPath = ('/sys/bus/iio/devices/iio:device%s/name' % i)

        # DEBUG
        # print('/sys/bus/iio/devices/iio:device%s/name' % i)

        if path.exists(folderPath) and path.isfile(folderPath):

            # DEBUG
            # print("First IF Loop")

            isfile = open(folderPath, "r")
            isfile_text = isfile.readline().strip()
            sthumid = str(isfile_text)
            isfile.close

            # DEBUG
            # print("sthumid is", sthumid)

            if str(sthumid) == "hts221":

                sensorPath = ('/sys/bus/iio/devices/iio:device%s' % i)

                # Read the "in_humid_raw" file
                in_humid_raw = open(sensorPath + '/in_humidityrelative_raw', "r")
                flt_raw_input = in_humid_raw.readline()
                InHumidRaw = float(flt_raw_input)
                # DEBUG
                # print("InHumidRaw =", InHumidRaw)
                in_humid_raw.close

                # Read the "in_humid_offset" file
                in_humid_offset = open(sensorPath + '/in_humidityrelative_offset', "r")
                flt_offset_input = in_humid_offset.readline()
                InHumidOffset = float(flt_offset_input)
                # DEBUG
                # print("InHumidOffset =", InHumidOffset)
                in_humid_offset.close

                # Read the "in_humid_scale" file
                in_humid_scale = open(sensorPath + '/in_humidityrelative_scale', "r")
                flt_scale_input = in_humid_scale.readline()
                InHumidScale = float(flt_scale_input)
                # DEBUG
                # print("InHumidScale =", InHumidScale)
                in_humid_scale.close

                # The next few line are setting up the def and the math for the
                # -- main temperature function
                def phase1(num1, num2):
                    return num1 + num2

                def phase2(num1, num2):
                    return num1 * num2

                # Get the sum of the numbers
                total1 = phase1(InHumidRaw, InHumidOffset)

                # Multiply the numbers
                total2 = phase2(total1, InHumidScale)

                # Format and print the humidity data, should look like 85.42 and
                # is in degrees celcius
                # print(format(total2, ',.2f'))
                return(format(total2, ',.2f'))

                # No need to run anymore
                exit()

            else:
                # DEBUG
                # print("second Else loop")
                # print("The file that this program is looking for cannot be found")
                pass

        else:
            # DEBUG
            # print("first Else loop")
            # print("The file that this program is looking for cannot be found")
            pass

        # need to add the counter so that the main loop will continue
        i = i + 1
