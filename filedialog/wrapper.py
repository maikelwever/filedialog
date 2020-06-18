import os
import sys

from filedialog.exceptions import NoImplementationFoundException


def which(command):
    for d in os.environ['PATH'].split(':'):
        if os.path.exists(d):
            for binary in os.listdir(d):
                if binary == command:
                    return os.path.join(d, command)


if sys.platform == 'linux':
    probably_kde = os.environ.get('DESKTOP_SESSION', '').lower() == 'kde' or \
            os.environ.get('XDG_CURRENT_DESKTOP', '').lower() == 'kde'

    kdialog_binary = which('kdialog')
    zenity_binary = which('zenity')

    if kdialog_binary and (probably_kde or not zenity_binary):
        from filedialog.kdialog import *
    elif zenity_binary:
        from filedialog.zenity import *
    else:
        raise NoImplementationFoundException()

else:
    raise NoImplementationFoundException()


__all__ = ['open_file', 'open_multiple', 'save_file', 'choose_folder']

