#!/usr/bin/env python

import argparse
import json
import os
import subprocess
import time
import threading

def import_crt(list, index):
    count = 0
    for sn in list:
        try:
            print("Processing serial number: {}".format(sn))
            with open("%s/device.json" % sn) as f:
                hash = json.load(f)['data']['hash']
                crt = "%s/cert/client.crt" % sn
                key = "%s/cert/private.key" % sn
                p12 = "%s/cert/key.p12" % sn
                cmd = [OPENSSL, 'pkcs12', '-export',
                       '-in', crt, '-inkey', key,
                       '-name', sn.lower(),
                       '-out', p12,
                       '-passin', "pass:%s" % hash, '-passout', "pass:%s" % PASSWORD]
                print(' '.join(cmd))
                subprocess.check_output(cmd)

                cmd = [KEY_TOOL, '-importkeystore',
                       '-srckeystore', p12, '-srcstoretype', 'pkcs12', '-srcstorepass', PASSWORD,
                       '-destkeystore', "%s.%s" % (OUTFILE, index), '-deststoretype', 'pkcs12', '-deststorepass', PASSWORD,
                       '-alias', sn.lower()]
                print(' '.join(cmd))
                subprocess.check_output(cmd)
                count += 1
                print("Index: {}, Count: {}, pkcs12 key: {}".format(index, count, sn))
        except Exception as e:
            print("Error processing {}: {}".format(sn, e))
    thread.remove(index)

if __name__ == '__main__':
    print("Script started")
    parser = argparse.ArgumentParser()
    parser.add_argument("-keytool", help="set custom keytool path", default='keytool')
    parser.add_argument("-openssl", help="set custom openssl path", default='openssl')
    parser.add_argument("-out", help="set custom openssl path", default='keystore.jks')
    parser.add_argument("-password", help="set password", default='password')
    parser.add_argument("-max_crt", help="set max crt in one part", default=50)
    parser.add_argument("-max_thread", help="set max crt in one part", default=50)

    args = parser.parse_args()

    KEY_TOOL = args.keytool
    OPENSSL = args.openssl
    OUTFILE = args.out
    PASSWORD = args.password
    MAX_CRT = int(args.max_crt)
    MAX_THREAD = int(args.max_thread)

    print("Parsed arguments:")
    print("KEY_TOOL: {}".format(KEY_TOOL))
    print("OPENSSL: {}".format(OPENSSL))
    print("OUTFILE: {}".format(OUTFILE))
    print("PASSWORD: {}".format(PASSWORD))
    print("MAX_CRT: {}".format(MAX_CRT))
    print("MAX_THREAD: {}".format(MAX_THREAD))

    thread = []
    devices = []
    for dir in os.listdir(os.getcwd()):
        if os.path.isdir(dir):
            if os.path.isfile("%s/device.json" % dir):
                devices.append(dir)

    devices.sort()
    print("Devices found:", devices)

    num_thread = (len(devices) // MAX_CRT) + 1
    for i in range(1, num_thread):
        while len(thread) > MAX_THREAD:
            time.sleep(1)
        begin = i * MAX_CRT - MAX_CRT
        end = i * MAX_CRT
        if end > len(devices):
            end = len(devices)
        list = devices[begin:end]
        print("Starting thread {} for devices {} to {}".format(i, begin, end))
        t = threading.Thread(target=import_crt, args=(list, i,))
        t.daemon = True
        t.start()
        thread.append(i)

    while len(thread) > 0:
        time.sleep(1)
        print("Threads running:", len(thread))

    for i in range(1, num_thread):
        jks_part = "%s.%s" % (OUTFILE, i)
        cmd = [KEY_TOOL, '-importkeystore',
               '-srckeystore', jks_part, '-srcstoretype', 'pkcs12', '-srcstorepass', PASSWORD,
               '-destkeystore', OUTFILE, '-deststoretype', 'pkcs12', '-deststorepass', PASSWORD]
        print(' '.join(cmd))
        subprocess.check_output(cmd)
    print("Script completed")
