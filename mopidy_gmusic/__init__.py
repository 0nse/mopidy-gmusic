from __future__ import unicode_literals

import os

from mopidy import config, ext


__version__ = '1.0.0'


class GMusicExtension(ext.Extension):

    dist_name = 'Mopidy-GMusic'
    ext_name = 'gmusic'
    version = __version__

    def get_default_config(self):
        conf_file = os.path.join(os.path.dirname(__file__), 'ext.conf')
        return config.read(conf_file)

    def get_config_schema(self):
        schema = super(GMusicExtension, self).get_config_schema()
        schema['username'] = config.String()
        schema['password'] = config.Secret()
        schema['deviceid'] = config.String(optional=True)
        schema['all_access'] = config.Boolean(optional=True)
        schema['refresh_library'] = config.Integer(minimum=-1, optional=True)
        schema['refresh_playlists'] = config.Integer(minimum=-1, optional=True)
        schema['show_radio_stations_browse'] = config.Boolean(optional=True)
        schema['show_radio_stations_playlist'] = config.Boolean(optional=True)
        schema['max_radio_stations'] = config.Integer(minimum=0, optional=True)
        schema['max_radio_tracks'] = config.Integer(minimum=1, optional=True)
        return schema

    def setup(self, registry):
        from .actor import GMusicBackend
        from .scrobbler_frontend import GMusicScrobblerFrontend
        registry.add('backend', GMusicBackend)
        registry.add('frontend', GMusicScrobblerFrontend)
