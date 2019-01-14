import shlex
import diskspace
import argparse

from . import argpar, utils, path


def shell():
    arguments = argpar.getarg()
    parser = argpar.Arguments(description="Making it possible to use Linux df & du command on Windows", add_help=False)
    parser.add_argument('--help', action='help', default=argparse.SUPPRESS, help='Show this help message and exit.')
    parser.add_argument('-v', '--version', action='store_true', help='Show the version number and exit')
    parser.add_argument('-e', '--exclude', nargs='+', help='Exclude name or file extensions matching arguments', default=None)
    parser.add_argument('-o', '--only', nargs='+', help='Only include name or file extensions matching arguments', default=None)
    parser.add_argument('-h', '--human', action='store_true', help='Convert bytes in to readable format')
    parser.add_argument('-nf', '--nofolders', action='store_true', help='Ingore folders')
    parser.add_argument('-ns', '--nostats', action='store_true', help="Don't display disk space at top")

    try:
        args = parser.parse_args(shlex.split(arguments))
    except Exception as e:
        utils.exitcode(e)

    if args.version:
        utils.exitcode(diskspace.__version__)

    if args.nofolders:
        nofolders = False
    else:
        nofolders = True

    if args.nostats:
        nostats = False
    else:
        nostats = True

    if args.exclude and args.only:
        utils.exitcode("You can't define what to exclude and what to only include at the same time.")

    print(path.ShowPath(
        include_folder=nofolders,
        include_stats=nostats,
        exclude=args.exclude,
        human=args.human,
        whitelist=args.only
    ).pretty_print)


def main():
    try:
        shell()
    except KeyboardInterrupt:
        print('\nCancelling...')


if __name__ == '__main__':
    main()
