#!/usr/bin/env python

class Heroku():

    def __init__(self, name):
        self.name = name;
        self.domain = '.herokuapp.com';

    ##
    # Build the complete Heroku app's URL.
    #
    # @return string
    ##
    def url(self):
        return self.name + self.domain;
