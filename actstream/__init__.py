try:
    from actstream.signals import action
except ImportError:
    pass

__version_info__ = {
    'major': 0,
    'minor': 5,
    'micro': 0,
    'releaselevel': 'final',
    'serial': 1
}


def get_version(release_level=True):
    """
    Return the formatted version information
    """
    vers = ["%(major)i.%(minor)i.%(micro)i" % __version_info__]
    if release_level and __version_info__['releaselevel'] != 'final':
        vers.append('%(releaselevel)s%(serial)i' % __version_info__)
    return ''.join(vers)


__version__ = get_version()
__author__ = 'Justin Quick <justquick@gmail.com>'
default_app_config = 'actstream.apps.ActstreamConfig'
