#!/usr/bin/python

import dbus, gobject, gconf
from dbus.mainloop.glib import DBusGMainLoop

client = gconf.client_get_default()

dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)

bus = dbus.SessionBus()
obj = bus.get_object("im.pidgin.purple.PurpleService", "/im/pidgin/purple/PurpleObject")
purple = dbus.Interface(obj, "im.pidgin.purple.PurpleInterface")


def received_im_msg(account, sender, message, conversation, flags):
    print(sender, "said:", message)

def buddy_signed_on(buddy):
    buddy_alias = purple.PurpleBuddyGetAlias(buddy)
    buddy_name = purple.PurpleBuddyGetName(buddy)
    buddy_account = purple.PurpleBuddyGetAccount(buddy)
    print("signed:", buddy, buddy_name)

def conversation_created(conv):
    print("conversation:", conv)

bus.add_signal_receiver(received_im_msg,
    dbus_interface="im.pidgin.purple.PurpleInterface",
    	signal_name="ReceivedImMsg")

bus.add_signal_receiver(buddy_signed_on,
	dbus_interface="im.pidgin.purple.PurpleInterface",
    	signal_name="BuddySignedOn")

bus.add_signal_receiver(conversation_created,
	dbus_interface="im.pidgin.purple.PurpleInterface",
    	signal_name="ConversationCreated")

try:
	from gi.repository import Gtk
except: # Can't use ImportError, as gi.repository isn't quite that nice...
	import gtk as Gtk



def on_button_clicked(widget):
	buddy_name = client.get_string("/apps/buddy_applet/buddy_name")
	print (buddy_name)
	account = purple.PurpleAccountsFind('stokito@ya.ru', 'prpl-jabber')
#	buddy = purple.PurpleFindBuddy(account, 'stokito@gmail.com')
#	buddy_alias = purple.PurpleBuddyGetAlias(buddy)
#	buddy_name = purple.PurpleBuddyGetName(buddy)
	conv = purple.PurpleConversationNew(1, account, buddy_name)
	purple.PurpleConvImSend(purple.PurpleConvIm(conv), "Ignore.")


def applet_factory(applet, iid, data = None):
	client.set_string("/apps/buddy_applet/buddy_name", "stokito@gmail.com")
	buddy_name = client.get_string("/apps/buddy_applet/buddy_name")
	print (buddy_name)
	button = Gtk.Button(buddy_name)
	button.connect("clicked", on_button_clicked)
	applet.add(button)
#	applet.set_background_widget(applet)
	applet.show_all()
	return True
