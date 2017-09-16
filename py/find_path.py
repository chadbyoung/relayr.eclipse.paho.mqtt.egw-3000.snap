#!/usr/bin/env python3

from os import path


def folderLocate():

    # set the main loop count to 0
    i = 0

    # DEBUG
    # set the divider to 1k
    # div1k = 1000

    # The main loop is set to 4, and may need to be increased. I have not seen
    # an EGW3K with more than 4 devices.
    while i < 4:

        # DEBUG
        print("Primary while loop #", i)

        # DEBUG
        # PATH = "/sys/bus/iio/devices/iio:device%s/name" % i

        # if path.exists('./device%s/name' % i) and
        # -- path.isfile('./device%s/name' % i):
        if path.exists('/sys/bus/iio/devices/iio:device%s/name' % i) and \
                path.isfile('/sys/bus/iio/devices/iio:device%s/name' % i):

            # DEBUG
            print("First IF Loop")
            # print("The path exists and it is a file")
            # print("PATH =", PATH)

            # fline = open('./device%s/name' % i, "r")
            isfile = open('/sys/bus/iio/devices/iio:device%s/name' % i, "r")
            isfile_text = isfile.readline().strip()
            sttemp = str(isfile_text)
            isfile.close

            # DEBUG
            print("sttemp is", sttemp)

        else:
            # DEBUG
            # print("first Else loop")
            # print("The file that this program is looking for cannot be found")
            pass
        # need to add the counter so that the main loop will continue
        i = i + 1
