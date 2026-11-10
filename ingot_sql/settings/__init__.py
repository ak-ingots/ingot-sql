"""The settings unit of the defaults with the configs of the addon."""

__all__ = ("SqlSettingsUnit",)

from ingots.defaults.settings import SettingsUnit
from ingots.puer import Slot

from .configs import SqlConfigs


class SqlSettingsUnit(SettingsUnit):
    """The settings unit, with the addon's :class:`SqlConfigs`."""

    configs = Slot(SqlConfigs)
