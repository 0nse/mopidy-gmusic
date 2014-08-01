import unittest

import mock

from mopidy_gmusic import GMusicExtension, actor as backend_lib


class ExtensionTest(unittest.TestCase):

    @staticmethod
    def get_config(ext):
        config = ext.get_config_schema()
        config['all_access'] = False
        config['show_radio_stations_browse'] = True
        config['show_radio_stations_playlist'] = False
        config['max_radio_stations'] = 0
        config['max_radio_tracks'] = 25
        return {'gmusic': config}

    def test_get_default_config(self):
        ext = GMusicExtension()

        config = ext.get_default_config()

        self.assertIn('[gmusic]', config)
        self.assertIn('enabled = true', config)
        self.assertIn('all_access = false', config)
        self.assertIn('show_radio_stations_browse = true', config)
        self.assertIn('max_radio_stations = 0', config)
        self.assertIn('max_radio_tracks = 25', config)

    def test_get_config_schema(self):
        ext = GMusicExtension()

        schema = ext.get_config_schema()

        self.assertIn('username', schema)
        self.assertIn('password', schema)
        self.assertIn('deviceid', schema)
        self.assertIn('refresh_library', schema)
        self.assertIn('refresh_playlists', schema)
        self.assertIn('all_access', schema)
        self.assertIn('show_radio_stations_browse', schema)
        self.assertIn('show_radio_stations_playlist', schema)
        self.assertIn('max_radio_stations', schema)
        self.assertIn('max_radio_tracks', schema)

    def test_get_backend_classes(self):
        registry = mock.Mock()

        ext = GMusicExtension()
        ext.setup(registry)

        registry.add.assert_called_once_with(
            'backend', backend_lib.GMusicBackend)

    def test_init_backend(self):
        ext = GMusicExtension()
        backend = backend_lib.GMusicBackend(
            ExtensionTest.get_config(ext), None)
        self.assertIsNotNone(backend)
        backend.on_start()
        backend.on_stop()
