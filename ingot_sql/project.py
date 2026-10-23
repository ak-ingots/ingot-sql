"""The project of the addon: what an application inherits from."""

__all__ = ("SqlProject",)

from ingots.defaults import Project
from ingots.puer import Slot

from .logging import SqlLogging
from .settings import SqlSettings


class SqlProject(Project):
    """
    The project of the defaults with the addon's :class:`SqlSettings` and
    :class:`SqlLogging`. An application inherits from it and sets its own
    ``env_configs_prefix``; the addon run on its own (``python -m ingot_sql``)
    keeps the prefix of the defaults, ``INGOT``.
    """

    settings = Slot(SqlSettings)
    logging = Slot(SqlLogging)
