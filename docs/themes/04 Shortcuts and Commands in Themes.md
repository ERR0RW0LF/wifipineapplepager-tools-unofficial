# Shortcuts and Commands in Themes
If you ever looked at the `theme.json` of wargames you may have seen `commands` and `payload_shortcuts` in `_unused`.

This chapter will explain how to use commands and payload shortcuts in your theme which can be triggered from the UI.

## Commands
To use commands in your theme first you will need to move the `commands` out of the `_unused` section
```diff

+ "commands" : {
+   "restart_pineapd": "service pineapd restart",
+   "restart_networking": "service network restart",
+   "reboot": "reboot",
+   "log_temps": "/root/battest.sh > /tmp/temps.log",
+   "restart_go": "service pineapplepager restart"
+ },
  "_unused" : {
-     "commands" : {
-       "restart_pineapd": "service pineapd restart",
-       "restart_networking": "service network restart",
-       "reboot": "reboot",
-       "log_temps": "/root/battest.sh > /tmp/temps.log",
-       "restart_go": "service pineapplepager restart"
-     },
  
      "payload_shortcuts": {
        "test1": "/root/payloads/user/cat1/test1",
        "test2": "/root/payloads/user/cat1/test2"
      },
  
      "simple_images": {
      }
    }
```
