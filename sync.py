#!/usr/bin/env python3

import time
import subprocess
import os


def set_identity(name, email):
    subprocess.check_call(
        'git config --global user.name "{}"'.format(name).split())
    subprocess.check_call(
        'git config --global user.email "{}"'.format(email).split())


def mode():
    output = subprocess.check_output('git annx info'.split()).decode()
    return output.splitlines()[0].split(':')[1].strip()


def _do_sync():
    os.chdir('/data')
    subprocess.check_call(
        'git annex add .'.split())
    if mode() == 'indirect':
        subprocess.call(
            'git commit -a -m'.split() +
            ['"from {}"'.format(os.uname().nodename)])
    subprocess.check_call('git annex sync'.split())


def sync(every=60):
    while True:
        _do_sync()
        time.sleep(every)


main = sync


if __name__ == '__main__':
    set_identity('test user', 'test@example.com')
    main()
