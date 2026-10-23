"""The configs of the addon, named ``SQL_*``."""

__all__ = ("SqlConfigs",)

import logging

from ingots.defaults.settings.configs import Configs, LogLevelConfig


class SqlConfigs(Configs):
    """The configs of the defaults with those of SQL databases."""

    SQL_LOGGING_LEVEL = LogLevelConfig(logging.INFO)
