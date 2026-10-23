"""The settings unit of the defaults with the configs of the addon."""

__all__ = ("SqlSettings",)

from ingots.defaults.settings import Settings
from ingots.puer import Slot

from .configs import SqlConfigs


class SqlSettings(Settings):
    """The settings unit, with the addon's :class:`SqlConfigs`."""

    configs = Slot(SqlConfigs)
