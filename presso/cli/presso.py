import argparse
import asyncio
import logging
import sys

from pydoc import locate

import toml

from presso.core import util
from presso.core.eventqueue import EventQueue


def run(args):
    manifest = toml.load(args.manifest)
    # Setup logger
    log_format = '[%(levelname)s|%(module)s|%(asctime)s] %(message)s'
    log_level = getattr(logging, manifest['log']['level'].upper(), None)
    logging.basicConfig(filename=manifest['log']['file'], format=log_format, level=log_level)
    # Set portfolio type
    util.IS_REALTIME = manifest['realtime']

    # Load dataevents
    dataevents = {}
    for dataevent in manifest['dataevents']:
        module = locate(dataevent['module'])
        dataevents[dataevent['name']] = module(
            dataevent['data_path'],
            dataevent['history_file'],
            dataevent['config']
        )

    # Load connectors
    connectors = {}
    for connector in manifest['connectors']:
        module = locate(connector['module'])(
            {name: dataevents[name] for name in connector['dataevents']},
            connector['config']
        )
        connectors[connector['name']] = module

    # Load statistics
    statistics = {}
    for stat in manifest['statistics']:
        module = locate(stat['module'])(stat['config'])
        statistics[stat['name']] = module

    # Load portfolio
    portfolio = locate(manifest['module'])(connectors, statistics, manifest['config'])

    # Load alphas
    for alpha in manifest['alphas']:
        module = locate(alpha['module'])(
            alpha['name'],
            portfolio,
            dataevents[alpha['main_dataevent']],
            {name: dataevents[name] for name in alpha['dataevents']},
            alpha['config']
        )
        dataevents[alpha['main_dataevent']].addAlpha(module)

    # Start portfolio
    loop = asyncio.get_event_loop()
    event_queue = EventQueue.getInstance()
    async def main():
        # Let DataEvents to run first
        await asyncio.sleep(2)
        await event_queue.consume()
    # Press ENTER to stop eventloop and run statistics
    def stop():
        for dataevent in dataevents.values():
            dataevent.shutdown()
        asyncio.wait(asyncio.sleep(1))
        loop.stop()
    loop.add_reader(sys.stdin, stop)
    try:
        loop.run_until_complete(main())
    except RuntimeError as error:
        if str(error) == 'Event loop stopped before Future completed.':
            print('Event Loop Stopped')
            util.LOG.info('Event Loop Stopped')
        else:
            util.LOG.exception(error)
    portfolio.runStatistics()

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='action')
    subparsers.required = True

    run_parser = subparsers.add_parser('run', help='run a portfolio')
    run_parser.add_argument('manifest', type=open, help='TOML manifest file')
    run_parser.set_defaults(func=run)

    create_parser = subparsers.add_parser('create', help='TODO: create components')
    args = parser.parse_args()
    args.func(args)
