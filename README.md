
# MyBrowse

MyBrowse is a simple webbrowser written in Python3 using GTK and WebKit.

[![Packaging status](https://repology.org/badge/vertical-allrepos/mybrowse.svg)](https://repology.org/project/mybrowse/versions)

## Support

 * #mybrowse on [irc.libera.chat](https://libera.chat) ([webchat](https://web.libera.chat/?channel=#mybrowse), [via Matrix](https://matrix.to/#/#mybrowse:libera.chat))

## Installation

### PyPI

The command

    pip install --user -U mybrowse

will install MyBrowse using pip inside your Home-Directory and can be used to upgrade it too.

### Debian/Ubuntu

Installation on Ubuntu based distributions is possible with a PPA:

    sudo apt-add-repository ppa:tuxifreund/mybrowse
    sudo apt-get install mybrowse

Additionally MyBrowse is present in the [MPR](https://mpr.hunterwittenborn.com/packages/mybrowse). Installation is pretty straightforward:

    git clone https://mpr.hunterwittenborn.com/mybrowse.git && cd mybrowse
    makedeb -s && sudo dpkg -i "$PWD"/mybrowse_*.deb

### Arch

MyBrowse is available via the AUR. To install it just type:

    git clone https://aur.archlinux.org/mybrowse.git && cd mybrowse
    makepkg -si

Or use your prefered AUR-helper. It would be a pleasure, if you’d vote for the AUR under [https://aur.archlinux.org/packages/mybrowse](https://aur.archlinux.org/packages/mybrowse).

## Features

 * loading websites ;)
 * bookmark pages
 * seperate search and addressbar
 * history
 * automatic use of https

## Donating

Donating is currently only possible via Bitcoin: bc1qfg6uy36es7ycsyw5g50wjz45hfs5ke5w8twfap
