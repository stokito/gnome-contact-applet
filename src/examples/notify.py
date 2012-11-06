#!/usr/bin/python
import sys
import pynotify
 
if __name__ == "__main__":
    pynotify.init("My Application Name")

    n = pynotify.Notification(
        "Burhan Uddin",
        "What is life? Full of of care? We have no time to stand or stare!",
        "notification-message-im")
#    n.set_urgency(pynotify.URGENCY_LOW)
#    n.set_urgency(pynotify.URGENCY_NORMAL)
#    n.set_urgency(pynotify.URGENCY_CRITICAL)
 #   n.set_timeout(pynotify.NOTIFY_EXPIRES_NEVER)
    n.show()

