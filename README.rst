``beets-musly`` is a ``beets`` plugin that allows you to automatically run a ``musly`` music similarity analysis any time your music library is updated.


Configuration
-------------

First, make sure to enable the plugin by adding it to the ``plugins`` list in your ``beets`` configuration. You can open the config file manually or run ``beet config --edit``::

    plugins: [...] musly

You should also tell the plugin the path of your ``musly`` collection file. For example::

    musly:
        collection: ~/.config/musly/collection.musly

Now every time your ``beets`` database changes, this collection file will be updated.
