# Copyright 2017, Nate Bogdanowicz
import os.path
import subprocess as sp
from beets import config
from beets.plugins import BeetsPlugin


class MuslyPlugin(BeetsPlugin):
    def __init__(self):
        super(MuslyPlugin, self).__init__()
        config['musly'].add({
        })
        self.register_listener('database_change', self.on_db_change)

    def on_db_change(self, lib, model):
        self.register_listener('cli_exit', self.update)

    def update(self, lib):
        self._log.info('Running musly analysis')
        coll_path = os.path.expanduser(config['musly']['collection'].get())
        music_dir = os.path.expanduser(config['directory'].get())
        sp.call(['musly', '-c', coll_path, '-a', music_dir], stdout=sp.DEVNULL)
