#!/usr/bin/env python

import dbus, gobject
from dbus.mainloop.glib import DBusGMainLoop

dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

bus = dbus.SessionBus()
obj = bus.get_object("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject")
purple = dbus.Interface(obj, "im.pidgin.purple.PurpleInterface")

def received_im_msg(account, sender, message, conversation, flags):
    print sender, "said:", message

def buddy_signed_on(buddy):
    buddy_alias = purple.PurpleBuddyGetAlias(buddy)
    buddy_name = purple.PurpleBuddyGetName(buddy)
    buddy_account = purple.PurpleBuddyGetAccount(buddy)
#    conv = purple.PurpleConversationNew(PURPLE_CONV_TYPE_IM, buddy_name)
    conv = purple.PurpleConversationNew(1, buddy_account, buddy_name)
    print "signed:", buddy, buddy_name

def conversation_created(conv):
    print "conversation:", conv


bus.add_signal_receiver(received_im_msg,
                        dbus_interface="im.pidgin.purple.PurpleInterface",
                        signal_name="ReceivedImMsg")

bus.add_signal_receiver(buddy_signed_on,
                        dbus_interface="im.pidgin.purple.PurpleInterface",
                        signal_name="BuddySignedOn")

bus.add_signal_receiver(conversation_created,
                        dbus_interface="im.pidgin.purple.PurpleInterface",
                        signal_name="ConversationCreated")


loop = gobject.MainLoop()
loop.run()
