Changelog
-------

Here's a log of all the changes that have happened to this package.

1.1.0 - Latest
------

#### Add

- Added a Heroku class for neatly encapsulating Heroku methods [James Kirby]
- Docblocks for the entire Typekit class [James Kirby]
- Added a changelog [James Kirby]
- Added a license [James Kirby]
- Added a readme file [James Kirby]

#### Fix

- Removed Python compiled files from repository [James Kirby]
- Adding missing EOF new line to the output file [James Kirby]
- Returning boolean responses for the `add` & `publish` methods, instead of an object [James Kirby]
- Removed new line from output to bring inline with Heroku's styling [James Kirby]
- Unable to catch `StandardError` for all errors, so removing to be a catch-all [James Kirby]

1.0.1 - 2017-08-16
------

#### Fix

- Spelling mistake in kit pubished confirmation message [James Kirby]


1.0.0 - 2017-08-16
------

First stable release of `jedkirby/heroku-buildpack-typekit`.
