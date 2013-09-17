from __future__ import unicode_literals

import logging

from gmusicapi import Mobileclient, Webclient, CallFailure

logger = logging.getLogger('mopidy.backends.gmusic')


class GMusicSession(object):

    def __init__(self):
        super(GMusicSession, self).__init__()
        logger.info('Mopidy uses Google Music')
        self.api = Mobileclient()

    def login(self, username, password, deviceid):
        if self.api.is_authenticated():
            self.api.logout()
        try:
            self.api.login(username, password)
        except CallFailure as error:
            logger.error(u'Failed to login as "%s": %s', username, error)
        if self.api.is_authenticated():
            if deviceid is None:
                self.deviceid = self.get_deviceid(username, password)
            else:
                self.deviceid = deviceid
        else:
            return False

    def logout(self):
        if self.api.is_authenticated():
            return self.api.logout()
        else:
            return True

    def get_all_songs(self):
        if self.api.is_authenticated():
            return self.api.get_all_songs()
        else:
            return {}

    def get_stream_url(self, song_id):
        if self.api.is_authenticated():
            try:
                return self.api.get_stream_urls(song_id)[0]
            except CallFailure as error:
                logger.error(u'Failed to lookup "%s": %s', song_id, error)

    def get_all_playlist_ids(self):
        if self.api.is_authenticated():
            return self.api.get_all_playlist_ids()
        else:
            return {}

    def get_playlist_songs(self, playlist_id):
        if self.api.is_authenticated():
            return self.api.get_playlist_songs(playlist_id)
        else:
            return {}

    def get_deviceid(self, username, password):
        logger.warning(u'No mobile device ID configured. Trying to detect one.')
        webapi = Webclient()
        webapi.login(username, password)
        devices = webapi.get_registered_devices()
        deviceid = None
        for device in devices:
            if device['type'] == 'PHONE' and device['id'][0:2] == u'0x':
                # Omit the '0x' prefix
                deviceid = device['id'][2:]
                break
        webapi.logout()
        if deviceid is None:
            logger.error(u'No valid mobile device ID found. Playing songs will not work.')
        else:
            logger.info(u'Using mobile device ID %s', deviceid)
        return deviceid
