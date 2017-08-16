#!/usr/bin/env python

##
# Print a heading.
#
# @var string text
# @return string
##
def heading(text):
    return '-----> ' + text;

##
# Print a single line.
#
# @var string text
# @return string
##
def line(text):
    return '       ' + text;

##
# Print a single new line.
#
# @return string
##
def nl():
    return line('');