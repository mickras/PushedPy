# PushedPy
PushedPy is a simple Python wrapper for the Pushed.co API, that allows you to send push notifications, in real-time, to iOS and Android devices + Chrome, Firefox and Safari browsers.

To send push notifications through Pushed.co, you need two things:
* Create an account on https://pushed.co/
* If you want to send push notifications to a mobile device, you need to download the Pushed.co app to the device.

Pushed.co is a paid service, but they offer a sandbox plan that gives you the ability to send up to 1.000 messages pr. month, for free.

## Installation

```
pip install PushedPy
```

## Basic usage
To send a push notification in it's simplest form, simply do:

```
import Pushed

pushed_obj = Pushed("MyAppKey", "MyAppSecret")
r = pushed_obj.Notification("My message to send as a push notification")
print(r)
```

To send a push notification including an attached URL, add the URL when calling
the Notification function:

```
r = pushed_obj.Notification("My push message", "http://mysite.com")
```

## Get and create apps
To retrieve a list of all apps associated with your Pushed account, or to create a new app, you need to set your Pushed userID and API key (You find these in the account settings on pushed.co):

```
pushed_obj.pushed_id = "Pushed userid"
pushed_obj.pushed_apikey = "Pushed API key"

# Return a JSON string with details about your apps:
my_apps = pushed_obj.GetApps()

# Create a new app:
r = pushed_obj.CreateApp("App name", "App description")
```

By default, a new app is created as private, but if you want it to be public, add
True to the function call:

```
r = pushed_obj.CreateApp("App name", "App description", True)
```

## Get and create channels
Just like when retrieving or creating apps, you need to make sure you have set your pushed userID and API key, before you can get or create channels:

```
pushed_obj.pushed_id = "Pushed userid"
pushed_obj.pushed_apikey = "Pushed API key"

# Return a JSON string with details about all your channels:
my_channels = pushed_obj.GetChannels()
```

To create a new channel, you need the app_alias of the app you want the channel to be created in. You can find this in your account settings on pushed.co, or by using the GetApps() function. Once you got the app_alias, a new channel can be created with:

```
r = pushed_obj.CreateChannel("app_alias", "MyNewChannelName")
```

Just like when creating an app, a new channel is set as private, as default. If you want it to be public (accesbile by all pushed users), add True to the function call:

```
r = pushed_obj.CreateChannel("app_alias", "MyNewChannelName", True)
```
