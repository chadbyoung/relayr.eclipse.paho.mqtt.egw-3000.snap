#!/usr/bin/env python3

# this section will be edited depending on the location of the sensor
FILE_PATH = "/sys/bus/iio/devices/iio:device0/name"
FILE_RAW = "/sys/bus/iio/devices/iio:device0/in_temp_raw"
FILE_OFFSET = "/sys/bus/iio/devices/iio:device0/in_temp_offset"
FILE_SCALE = "/sys/bus/iio/devices/iio:device0/in_temp_scale"

def readTemp():

    # Read the "in_temp_raw" file
    in_temp_raw = open(FILE_RAW, "r")
    flt_raw_input = in_temp_raw.readline()
    InTempRaw = float(flt_raw_input)
    in_temp_raw.close

    # Read the "in_temp_offset" file
    in_temp_offset = open(FILE_OFFSET, "r")
    flt_offset_input = in_temp_offset.readline()
    InTempOffset = float(flt_offset_input)
    in_temp_offset.close

    # Read the "in_temp_scale" file
    in_temp_scale = open(FILE_SCALE, "r")
    flt_scale_input = in_temp_scale.readline()
    InTempScale = float(flt_scale_input)
    in_temp_scale.close

    def phase1(num1, num2):
        return num1 + num2

    def phase2(num1, num2):
        return num1 * num2

    # Get the sum of the numbers
    total1 = phase1(InTempRaw, InTempOffset)

    # Multiply the numbers
    total2 = phase2(total1, InTempScale)

#    print("test.py")
    print(format(total2, ',.2f'))
    return(format(total2, ',.2f'))
