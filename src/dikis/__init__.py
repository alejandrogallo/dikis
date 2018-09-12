
import sys
import logging

import click
from click import echo
import dikis.app
import dikis.dicts


__version__ = '0.1.0'


@click.group()
@click.help_option('--help', '-h')
@click.version_option(version=__version__)
@click.option(
    '-d', '--dic',
    help='Dictinoary to use',
    default='aramorph'
)
@click.option(
    '--debug',
    is_flag=True,
    help='enable debug logging'
)
def main(debug, dic):
    """Main entry point"""
    logging.basicConfig(level=logging.WARNING)
    logger = logging.getLogger(__name__)
    if debug:
        logger.setLevel(logging.DEBUG)
        logger.debug("Enabled debug output")

    dikis.dicts.set_dict_from_name(dic)


@main.command('gui')
def gui():
    dikis.app.Gui(dikis.dicts.get_dict())
