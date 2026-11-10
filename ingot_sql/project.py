"""The project of the addon: what an application inherits from."""

__all__ = ("SqlProject",)

from ingots.defaults import Project
from ingots.puer import Slot

from .logging import SqlLoggingUnit
from .settings import SqlSettingsUnit


class SqlProject(Project):
    """
    The project of the defaults with the addon's :class:`SqlSettingsUnit` and
    :class:`SqlLoggingUnit`. An application inherits from it and sets its own
    ``env_configs_prefix``; the addon run on its own (``python -m ingot_sql``)
    keeps the prefix of the defaults, ``INGOT``.
    """

    settings = Slot(SqlSettingsUnit)
    logging = Slot(SqlLoggingUnit)
