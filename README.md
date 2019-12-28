# PushedPy
PushedPy is a simple Python wrapper for the Pushed.co API, that allows you to send push notifications, in real-time, to iOS and Android devices + Chrome, Firefox and Safari browsers.

To send push notifications through Pushed.co, you need two things:
* Create an account on https://pushed.co/
* If you want to send push notifications to a mobile device, you need to download the Pushed.co app to the device.

Pushed.co is a paid service, but they offer a sandbox plan that gives you the ability to send up to 1.000 messages pr. month, for free.

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
