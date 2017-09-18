#!/usr/bin/env python3

# whatTemper.py

from os import path


def whatTemper():
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
            sttemp = str(isfile_text)
            isfile.close

            # DEBUG
            # print("sttemp is", sttemp)

            if str(sttemp) == "hts221":

                sensorPath = ('/sys/bus/iio/devices/iio:device%s' % i)

                # in_temp_raw = open('/sys/bus/iio/devices/iio:device%s/in_temp_raw' % i, "r")
                in_temp_raw = open(sensorPath + '/in_temp_raw', "r")
                flt_raw_input = in_temp_raw.readline()
                InTempRaw = float(flt_raw_input)
                # DEBUG
                # print("InTempRaw =", InTempRaw)
                in_temp_raw.close

                # Read the "in_temp_offset" file
                in_temp_offset = open(sensorPath + '/in_temp_offset', "r")
                flt_offset_input = in_temp_offset.readline()
                InTempOffset = float(flt_offset_input)
                # DEBUG
                # print("InTempOffset =", InTempOffset)
                in_temp_offset.close

                # Read the "in_temp_scale" file
                in_temp_scale = open(sensorPath + '/in_temp_scale', "r")
                flt_scale_input = in_temp_scale.readline()
                InTempScale = float(flt_scale_input)
                # DEBUG
                # print("InTempScale =", InTempScale)
                in_temp_scale.close

                # The next few line are setting up the def and the math for the
                # -- main temperature function
                def phase1(num1, num2):
                    return num1 + num2

                def phase2(num1, num2):
                    return num1 * num2

                # Get the sum of the numbers
                total1 = phase1(InTempRaw, InTempOffset)

                # Multiply the numbers
                total2 = phase2(total1, InTempScale)

                # Format and print the temperature data, should look like 35.51 and
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
