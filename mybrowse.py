#!/usr/bin/python3
import gi
gi.require_version('WebKit2', '4.0')
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, WebKit2
import configparser
import os
import sys

browser_id = 'MyBrowse 0.1'

conf_dir = f"{os.path.expanduser('~')}/.config/mybrowse/"

if not os.path.exists(conf_dir):
        try:
                os.makedirs(conf_dir)
        except OSError as e:
                print(e)
                pass

config = configparser.ConfigParser()
config.read(conf_dir + 'mybrowse.cfg')
searchengine = config['General']['search']
startpage = config['General']['home']
if len(sys.argv) > 1:
        starturl = sys.argv[1]
else:
        starturl = startpage

class Browser(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='MyBrowse')

        self.view = WebKit2.WebView()

        self.vbox = Gtk.Box(orientation=Gtk.STYLE_CLASS_VERTICAL)
        self.vbox.expand = True
        self.vbox.set_spacing(10)
        #self.set_icon_from_file(conf_dir + 'mybrowse.png')

        self.menu = Gtk.Box(orientation=Gtk.STYLE_CLASS_HORIZONTAL)
        self.menu.expand = False
        self.back = Gtk.Button()
        self.back_arrow = Gtk.Image.new_from_icon_name('go-previous', Gtk.IconSize.SMALL_TOOLBAR)
        self.back.add(self.back_arrow)
        self.menu.add(self.back)
        self.forward = Gtk.Button()
        self.forward_arrow = Gtk.Image.new_from_icon_name('go-next', Gtk.IconSize.SMALL_TOOLBAR)
        self.forward.add(self.forward_arrow)
        self.menu.add(self.forward)
        self.reload = Gtk.Button()
        self.reload_arrow = Gtk.Image.new_from_icon_name('view-refresh', Gtk.IconSize.SMALL_TOOLBAR)
        self.reload.add(self.reload_arrow)
        self.menu.add(self.reload)
        self.home = Gtk.Button()
        self.home_arrow = Gtk.Image.new_from_icon_name('go-home', Gtk.IconSize.SMALL_TOOLBAR)
        self.home.add(self.home_arrow)
        self.menu.add(self.home)
        self.addressbar = Gtk.Entry()
        self.addressbar.set_text(starturl)
        self.addressbar.set_width_chars(75)
        self.menu.add(self.addressbar)
        self.bookmarker = Gtk.Button()
        self.bookmarker_symbol = Gtk.Image.new_from_icon_name('bookmark-new', Gtk.IconSize.SMALL_TOOLBAR)
        self.bookmarker.add(self.bookmarker_symbol)
        self.menu.add(self.bookmarker)
        self.searchbar = Gtk.SearchEntry()
        self.menu.add(self.searchbar)

        self.addressbar.connect("activate", self.change_url)
        self.back.connect("clicked", self.go_back)
        self.forward.connect("clicked", self.go_forward)
        self.reload.connect("clicked", self.go_reload)
        self.home.connect("clicked", self.go_home)
        self.searchbar.connect("activate", self.search)
        self.bookmarker.connect("clicked", self.set_bookmark)
        self.vbox.add(self.menu)

        self.sw = Gtk.ScrolledWindow()
        self.sw.add(self.view)

        self.vbox.pack_start(self.sw, True, True, 0)
        self.add(self.vbox)
        self.view.load_uri(starturl)
        self.view.connect("notify::uri", self.change_uri)
        self.view.connect("notify::title", self.change_title)

    def change_url(self, widget):
        url = self.addressbar.get_text()
        if not ":" in url:
           url = "https://" + url
        self.view.load_uri(url)

    def change_title(self, widget, data, *arg):
            title = widget.get_title()
            self.set_title(title + ' - MyBrowse')

    def change_uri(self, widget, data, *arg):
            uri = widget.get_uri()
            self.addressbar.set_text(uri)

    def go_back(self, widget):
        self.view.go_back()

    def go_forward(self, widget):
        self.view.go_forward()

    def go_reload(self, widget):
        self.view.reload()

    def go_home(self, widget):
        self.addressbar.set_text(startpage)
        self.view.load_uri(startpage)

    def search(self, searchbar):
        searchstring = self.searchbar.get_text()
        self.view.load_uri(searchengine + searchstring)

    def set_bookmark(self, widget):
        url = self.addressbar.get_text()
        title = self.view.get_title()
        bm_file =  open(conf_dir + 'bookmarks.html', 'a')
        bm_file.write('<a href="' + url + '">' + title + '</a><br>\r\n')


if __name__ == "__main__":
    browser = Browser()
    browser.set_default_size(1024, 704)
    browser.connect("delete-event", Gtk.main_quit)
    browser.show_all()
    Gtk.main()
