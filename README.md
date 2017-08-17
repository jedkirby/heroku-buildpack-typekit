# Heroku buildpack: Typekit

This is the unofficial [Heroku buildpack](http://devcenter.heroku.com/articles/buildpacks) for apps that make use of Typekit.

## Why

If you've got an app, on Heroku, that uses Typekit for its fonts, you may have run into the issue whereby because you're not allowed to whitelist the `*.herokuapp.com`, that your fonts will not load on any of your apps, or review apps.

This package resolves this issue by checking, and updating, your Typekit account by whitelisting the app, or review app's, domain automatically when a new deployment is triggered.

The entire process is non-blocking, so, if for some reason it doesn't work, your site will still be deployed regardless. The buildpack will provide useful information for any errors, and I'm always available on [Twitter](https://twitter.com/jedkirby) for some one-to-one help.

## Initial Setup

There are two **environment variables** which are required for all the types of updates that are possible, so these should be added to _all_ of your apps where you'd like to update the whitelisted domains automatically:

- `TYPEKIT_API_KEY` - This is a unique Typekit API Key, and can be generated [on the account page](https://typekit.com/account/tokens).
- `TYPEKIT_KIT_ID` - This is the ID of the Typekit Kit you'd like to update the whitelisted domains of.

Once added, you should see something similar to the following:

![Heroku Typekit Settings](assets/heroku-typekit-settings.png?raw=true "Heroku Typekit Settings")

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

## Setup: Pipelines (Development, Staging & Production)

Because the pipeline stage apps work differetly to review apps, it means we need to manually add a environment variable to each of the stage apps. You will only need to do this if you're wanting to use the `*.herokuapp.com` sub-domain as apposed to a custom domain - if you're using a custom domain, you should add it to Typekit manually.

The following environment variable is required, and it should match the name that's been given to the pipeline stage app during creation:

- `HEROKU_APP_NAME` - Name given to the pipeline stage app.

You should have something similar to the below image, where you can see the pipeline stage app name is `hdt-develop` and the value of the `HEROKU_APP_NAME` variable is also `hdt-develop`:

![Heroku App Name](assets/heroku-app-name.png?raw=true "Heroku App Name")

## Usage

Once you've followed the above [Initial Setup](#initial-setup) and either one or both of the [Review Apps](#setup-review-apps) / [Pipeline](#setup-pipelines-development-staging--production) guide(s) has been followed, you'll be good to either re-deploy an existing build, create a new review app, or push new code.

You should see something similar to the following image within the build log for a successful whitelist of the domain to Typekit:

![Heroku Typekit Domain Added](assets/heroku-typekit-domain-added-confirm.png?raw=true "Heroku Typekit Domain Added")

## Development

The following information only applies if you're forking and hacking on this buildpack for your own purposes.

### Pull Requests

Please submit all pull requests against develop as the base branch, and use either `feature` or `bugfix` branches.

## License

**jedkirby/heroku-buildpack-typekit** is licensed under the MIT license. See the [LICENSE](LICENSE) file for more details.
