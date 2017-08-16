#!/usr/bin/env python

import os;

##
# Cycle through all the environment variables, and
# include those that are whitelisted.
#
# @var string directory
# @var list whitelist
#
# @return void
##
def load(directory, whitelist):
    if directory:
        for name in os.listdir(directory):
            if name in whitelist:
                os.environ[name] = open(
                    os.path.abspath(
                        os.path.join(
                            directory,
                            name
                        )
                    )
                ).read();
