"""The logging unit of the defaults with the logger of the addon."""

__all__ = ("SqlLoggingUnit",)

import typing as t

from ingots.defaults.logging import LoggingUnit

if t.TYPE_CHECKING:
    from ..project import SqlProject


class SqlLoggingUnit(LoggingUnit):
    """
    The logging unit, with the logger of the addon, ``ingot_sql``, at
    ``SQL_LOGGING_LEVEL``.
    """

    project: "SqlProject"

    @t.override
    def build_loggers(self) -> dict[str, dict[str, t.Any]]:
        level = self.project.settings.configs.SQL_LOGGING_LEVEL
        addon = {"level": level, "handlers": ["default"], "propagate": False}
        return {**super().build_loggers(), "ingot_sql": addon}
