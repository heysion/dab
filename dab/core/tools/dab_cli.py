import sys
import optparse
import pdb

from dab_models import Package
from dab_dbconnection import dbconn
from dab_main import DABCli

class Usage(Exception):
    def __init__(self, msg=None, no_error=False):
        Exception.__init__(self, msg, no_error)



def parse_options(args):
    parser = optparse.OptionParser()

    parser.add_option("-u", "--update-vver", action="store_true", dest="update_verb_version",
                      help=optparse.SUPPRESS_HELP)

    parser.add_option("-n", "--packagename", type="string",
                      dest="package_name", default=None,
                      help=optparse.SUPPRESS_HELP)

    parser.add_option("-m", "--main-version", type="string", dest="main_version",
                      default=None,
                      help=optparse.SUPPRESS_HELP)

    parser.add_option("", "--build-all", action="store_true", dest="build_all_package",
                      default=False,
                      help=optparse.SUPPRESS_HELP)


    (options, args) = parser.parse_args()

    return options

def echo_usage():
    pass

def run_main(argv):
    try:
        options = parse_options(sys.argv[1:])
        cli = DABCli(options)
        cli.run()
    except Usage as status :
        (msg, no_error) = status
        if no_error:
            out = sys.stdout
            ret = 0
        else:
            out = sys.stderr
            ret = 2
        if msg:
            print >> out, msg
        return ret


if __name__ == "__main__":
    run_main(sys.argv)
    pass
