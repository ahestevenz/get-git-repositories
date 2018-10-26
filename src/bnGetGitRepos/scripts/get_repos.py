"""Command line script to sync git repositories."""
from __future__ import print_function

from builtins import input
import argparse
import cProfile as profile
import logging
import datetime
import os

# local 
from bnGetGitRepos import bnGetGitRepos

__author__ = [ "Ariel Hernandez <ariel.h.estevenz@ieee.org>" ]
__copyright__ = "Copyright 2018 Bleiben. All rights reserved."
__license__ = """Proprietary"""


def _main(args):
    """Actual program (without command line parsing). This is so we can profile.
    Parameters
    ----------
    args: namespace object as returned by ArgumentParser.parse_args()
    """

    reposync = bnGetGitRepos.bnGetGitRepos(json_file = args['json_file'], clone_ssh = args['clone_ssh'], reset_repos = args['reset_repos'])  
    reposync.update_repos()

    return 0
    

def main():
    """CLI for syncronized git repositories"""

    # Module specific
    argparser = argparse.ArgumentParser(description='Welcome')
    argparser.add_argument('-j', '--json_file', help='JSON file with repos information (default: "%(default)s")', required=False,
                           default='/Users/ahestevenz/.userfiles/conf/repos.json')
    argparser.add_argument('-ssh', '--clone_ssh', help='flag to enable clone repositories throw SSH key (default: "%(default)s")', required=False,
                           default=False, type=bool)
    argparser.add_argument('-r', '--reset_repos', help='flag to reset all the repositories (default: "%(default)s")', required=False,
                           default=False, type=bool)

    # Default Args
    argparser.add_argument('-v', '--verbose', help='Increase logging output  (default: INFO)'
                            '(can be specified several times)', action='count', default=1)
    argparser.add_argument('-p', '--profile', help='Run with profiling and store '
                            'output in given file', metavar='output.prof')
    args = vars(argparser.parse_args())

    FORMAT = '%(asctime)s - %(levelname)s - %(module)s - %(funcName)s - %(lineno)d - %(message)s'
    _V_LEVELS = [logging.INFO, logging.DEBUG]
    loglevel = min(len(_V_LEVELS)-1, args['verbose'])
    logging.basicConfig(format=FORMAT, level = _V_LEVELS[loglevel])

    if args['profile'] is not None:
        logging.info("Start profiling")
        r = 1
        profile.runctx("r = _main(args)", globals(), locals(), filename=args['profile'])
        logging.info("Done profiling")
    else:
        logging.info("Running without profiling")
        r = _main(args)

    logging.shutdown()

    return r

if __name__ == '__main__':
    exit(main())
