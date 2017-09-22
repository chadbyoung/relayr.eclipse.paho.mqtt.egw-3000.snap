#!/usr/bin/env python3

# whatPress.py

from os import path


def whatPress():
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
            stpress = str(isfile_text)
            isfile.close

            # DEBUG
            # print("sttemp is", sttemp)

            if str(stpress) == "lps22hb":

                sensorPath = ('/sys/bus/iio/devices/iio:device%s' % i)

                # Read the "in_pressure_raw" file
                in_press_raw = open(sensorPath + '/in_pressure_raw', "r")
                flt_raw_input = in_press_raw.readline()
                InPressRaw = float(flt_raw_input)
                # DEBUG
                # print("InPressRaw =", InPressRaw)
                in_press_raw.close

                # Read the "in_pressure_scale" file
                in_press_scale = open(sensorPath + '/in_pressure_scale', "r")
                flt_scale_input = in_press_scale.readline()
                InPressScale = float(flt_scale_input)
                # DEBUG
                # print("InPressScale =", InPressScale)
                in_press_scale.close

                # The next few line are setting up the def and the math for the
                # -- main pressure function

                def calculate(num1, num2, num3):
                    return num1 * num2 * num3

#                def phase1(num1, num2):
#                    return num1 + num2

#                def phase2(num1, num2):
#                    return num1 * num2

                # multiply constant
                multiply = 10

                # Calculate the pressure
                total = calculate(InPressRaw, InPressScale, multiply)

                # Get the sum of the numbers
#                total1 = phase1(InTempRaw, InTempOffset)

                # Multiply the numbers
#                total2 = phase2(total1, multiply)

                # Format and print the temperature data, should look like 35.51 and
                # is in degrees celcius
                # print(format(total2, ',.2f'))
#                return(format(total2, ',.2f'))
                return(format(total, ',.2f'))

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
