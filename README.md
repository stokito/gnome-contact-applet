gnome-contact-applet
====================

Quick access for contact from panel: start a conversation in Pidgin or send email

You can install GNOME on your Ubuntu by command:
 sudo apt-get install gnome-session-fallback  gnome-panel

You can build debian package by command:
 dpkg-buildpackage -rfakeroot -b

Currently applet will fail if Pidgin is not started yet.
For debug please start Pidgin first, and then run command:
 ./contact-factory3.py -d


Applet created by panel-applet-generator https://github.com/palfrey/panel-applet-generator
 sudo ./panel-applet-generator.py --name=contact --description="Quick access for contact from panel: start a conversation in Pidgin or send email" --icon=contact-applet.svg --maintainer="Sergey Ponomarev" --email=stokito@gmail.com --category=Network
