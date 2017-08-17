# Heroku buildpack: Typekit

This is the unofficial [Heroku buildpack](http://devcenter.heroku.com/articles/buildpacks) for apps that make use of Typekit.

## Why

If you've got an app, on Heroku, that uses Typekit for its fonts, you may have run into the issue whereby because you're not allowed to whitelist the `*.herokuapp.com`, that your fonts will not load on any of your apps, or review apps.

This package resolves this issue by checking, and updating, your Typekit account by whitelisting the app, or review app's, domain automatically when a new deployment is triggered.

The entire process is non-blocking, so, if for some reason it doesn't work, your site will still be deployed regardless. The buildpack will provide useful information for any errors, and I'm always available on [Twitter](https://twitter.com/jedkirby) for some one-to-one help.

## Initial Setup

There are two **environment variables** which are required for all the types of updates that are possible, so these should be added to _all_ of your apps where you'd like to update the whitelisted domains automatically:

- `TYPEKIT_KIT_ID` - This is the ID of the Typekit Kit you'd like to update the whitelisted domains of.
- `TYPEKIT_API_KEY` - This is a unique Typekit API Key, and can be generated [on the account page](https://typekit.com/account/tokens).

Once added, you should see something similar to the following:

![Heroku Environment Settings](assets/heroku-env-settings.png?raw=true "Heroku Environment Settings")

## Setup: Review Apps

Then, to enable this process on Review Apps, you'll need to update the `app.json` file, which should be in the root of your project, to add the following Heroku-specific variable to the `env` list:

```json
{
    "env": {
        "HEROKU_APP_NAME": {"required": true}
    }
}
```

And the following to the `buildpacks` array, merging them with any existing properties if required:

```json
{
    "buildpacks": [
        {
            "url": "https://github.com/jedkirby/heroku-buildpack-typekit"
        }
    ]
}
```
