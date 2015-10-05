*************
Mopidy-GMusic
*************

.. image:: https://img.shields.io/pypi/v/Mopidy-GMusic.svg?style=flat
    :target: https://pypi.python.org/pypi/Mopidy-GMusic/
    :alt: Latest PyPI version

.. image:: https://img.shields.io/pypi/dm/Mopidy-GMusic.svg?style=flat
    :target: https://pypi.python.org/pypi/Mopidy-GMusic/
    :alt: Number of PyPI downloads

.. image:: https://img.shields.io/travis/mopidy/mopidy-gmusic/develop.svg?style=flat
    :target: https://travis-ci.org/mopidy/mopidy-gmusic
    :alt: Travis CI build status

.. image:: https://img.shields.io/coveralls/mopidy/mopidy-gmusic/develop.svg?style=flat
   :target: https://coveralls.io/r/mopidy/mopidy-gmusic
   :alt: Test coverage

`Mopidy <http://www.mopidy.com/>`_ extension for playing music from
`Google Play Music <https://play.google.com/music/>`_.


Dependencies
============

You must have a Google account, and either:

- have some music uploaded to your Google Play Music library, or

- have a subscription for Google Play Music All Access.


Installation
============

Install the Mopidy-GMusic extension by running::

    pip install mopidy-gmusic


Configuration
=============

Before starting Mopidy, you must add your Google username and password to your
Mopidy configuration file::

    [gmusic]
    username = alice
    password = secret

If you use 2-step verification to access your Google account, which you should,
you must create an application password in your Google account for
Mopidy-GMusic. See Google's docs on `how to make an app password
<https://support.google.com/accounts/answer/185833>`_ if you're not already
familiar with this.

All Access subscribers may enable All Access integration by adding this line::

    [gmusic]
    all_access = true

All Access radios are available as browsable content or playlist. The following
are the default config values::

    [gmusic]
    # show radio stations in content browser
    show_radio_stations_browse = true
    # show radio stations as playlists
    show_radio_stations_playlist = false
    # limit the number of radio stations, 0 = unlimited
    max_radio_stations = 0
    # limit the number or tracks for each radio station
    max_radio_tracks = 25

Google Play Music requires all clients to provide a device ID. By default,
Mopidy-GMusic will use your system's MAC address as the device ID. As Google
`puts some limits <https://support.google.com/googleplay/answer/3139562>`_ on
how many different devices you can associate with an account, you might want to
control what device ID is used. You can set the ``gmusic/deviceid`` config to
e.g. the device ID from your phone where you also use Google Play Music::

    [gmusic]
    deviceid = 0123456789abcdef

The Android device ID is a 16 character long string identifying the Android
device registered for Google Play Music, excluding the ``0x`` prefix. You can
obtain this ID by dialing ``*#*#8255#*#*`` on your phone (see the aid) or using
this `app <https://play.google.com/store/apps/details?id=com.evozi.deviceid>`_
(see the Google Service Framework ID Key).

On iOS the device ID is an UUID with the ``ios:`` prefix included. (TODO:
Include instructions on how to retrieve this.)


Usage
=====

The extension is enabled by default if all dependencies are
available. You can simply browse through your library and search for
tracks, albums, and artists. Google Play Music playlists are imported
as well. You can even add songs from your All Access subscription to
your library. Mopidy will able to play them.


Project resources
=================

- `Source code <https://github.com/mopidy/mopidy-gmusic>`_
- `Issue tracker <https://github.com/mopidy/mopidy-gmusic/issues>`_


Changelog
=========

v1.0.0 (UNRELEASED)
-------------------

- Require Mopidy >= 1.0.
- Require gmusicapi >= 6.0.
- Update to work with new playback API in Mopidy 1.0. (PR: #75)
- Update to work with new search API in Mopidy 1.0.
- Fix crash when tracks lack album or artist information. (Fixes: #74, PR: #24,
  also thanks to PRs #27, #64)
- Log error on login failure instead of swallowing the error. (PR: #36)
- Add support for All Access search and lookup (PR: #34)
- Add dynamic playlist based on top rated tracks.
- Add support for radio stations in browser and/or as playlists.
- Add support for browsing artists and albums in the cached library.
- Add cover art to ``Album.images`` model field.
- Add background refreshing of library and playlists. (Fixes: #21)
- Fix authentication issues. (Fixes: #82, #87)
- Add LRU cache for All Access albums and tracks.
- Increment Google's play count when 2/3 of the track has been played. (PR:
  #51)
- Let gmusicapi use the device's MAC address as device ID by default.


v0.3.0 (2014-01-28)
-------------------

- Issue #19: Public playlist support
- Issue #16: All playlist files are playable now
- Require Mopidy >= 0.18.


v0.2.2 (2013-11-11)
-------------------

- Issue #17: Fixed a bug regarding various artist albums
  (compilations)
- Issue #18: Fixed Google Music API playlist call for version 3.0.0
- Issue #16 (partial): All Access tracks in playlists are playable now


v0.2.1 (2013-10-11)
-------------------

- Issue #15: Fixed a bug regarding the translation of Google album
  artists to Mopidy album artists


v0.2 (2013-10-11)
-----------------

- Issue #12: Now able to play music from Google All Access
- Issue #9: Switched to the Mobileclient API of Google Music API
- Issue #4: Generate Album and Artist Search Results


v0.1.1 (2013-09-23)
-------------------

- Issue #11: Browsing the library fixed by implementing find_exact()


v0.1 (2013-09-16)
-----------------

- Initial release
