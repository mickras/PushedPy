# PushedPy
PushedPy is a simple Python wrapper for the Pushed.co API, that allows you to send push notifications, in real-time, to iOS and Android devices + Chrome, Firefox and Safari browsers.

## Usage

```
import Pushed

pushed_obj = Pushed("MyAppKey", "MyAppSecret")
r = pushed_obj.Notification("My message to send as a push notification")
print(r)
```
