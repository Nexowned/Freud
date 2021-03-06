import logging
from discord.ext.commands import Bot
from .events import Events

log = logging.getLogger(__name__)


def setup(bot: Bot) -> None:
    """Event cog load"""
    bot.add_cog(Events(bot))
    log.info("Cog loaded: Events")
