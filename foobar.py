import logging
import subprocess

import slapd

# env LD_PRELOAD="/home/eloi/dev/python-libfaketime/libfaketime/
# vendor/libfaketime/src/libfaketime.so.1"
# FAKETIME="2020-10-10 12:15:00" python foobar.py

# reexec_if_needed(remove_vars=False)

# with fake_time('2000-01-01 10:00:05') as fake:

process = subprocess.run("date", capture_output=True)
print(process.stdout.decode())

process = slapd.Slapd(log_level=logging.DEBUG)
process.start()
process.init_tree()
print(process.slapcat().stdout.decode())
process.stop()
