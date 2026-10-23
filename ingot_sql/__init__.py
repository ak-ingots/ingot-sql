"""
ingot-sql: Typed tables and typical queries for SQL databases in Ingots
applications, with raw SQL and the driver at hand: what the addons of the
SQL databases build on. An application inherits from :class:`SqlProject`, or
joins the units of the addon, ``settings`` and ``logging``, with those of
its other addons.
"""

__all__ = ("SqlProject",)

from .project import SqlProject
