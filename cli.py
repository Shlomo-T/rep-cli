import click
from cli_app.censys_adapter import CensysWebsitesAdapter
from censys.base import CensysUnauthorizedException
from cli_app.utils import *


@click.group()
def cli():
    """rep cli built in order to let users research easily about ipv4 addresses and domains using Censys services"""
    pass


@cli.command()
@click.argument('censys-credentials')
def configure(censys_credentials):
    """
    Stores your Censys credentials locally for sending Censys api requests.
    censys_credentials: Censys credentials in the format of <api-id>|<api-secret>
    """
    credentials = censys_credentials.split('|')
    if len(credentials) == 2 and '' not in credentials:
        try:
            # Create instance of adapter to verify authentication automatically
            CensysWebsitesAdapter(*credentials)
            set_censys_credentials(credentials)
            click.echo('Your credentials stored successfully!')
        except CensysUnauthorizedException as e:
            click.echo('Failed to authenticate your credentials: %s' % e.message)
        except Exception as e:
            click.echo('Something messed up: %s' % e.message)
        return
    click.echo('Credentials not in the format!')


@cli.command()
@click.option('--nocache', default=False, help='a flag to determine if to use cache or not')
@click.argument('source')
def scan(nocache, source):
    """
    Scan web source to detect if its a website (the source must be ipv4 address or a domain).
    In case it does a website, the source will be scanned and the title and top 10 keywords will return back as a result
    --nocache: flag that determines if to pull/store results in inner cache.
    """
    censys_credentials = get_censys_credentials()
    if not censys_credentials:
        click.echo('You must provide censys credentials!')
        return
    censys_adapter = CensysWebsitesAdapter(*censys_credentials)
    cache = CacheManager()
    # If the source already saved to cache return it to the user (better performance even if --nocache supplied as True)
    if cache.has_key(source):
        result = cache.get(source)
        click.echo('Result : %s' % result)
    elif censys_adapter.website_detection(source):
        result = parse_website_content(source)
        if not nocache:
            cache.set(source, result)
            click.echo("Results saved to cache")
        click.echo('Result : %s' % result)
    else:
        click.echo("This source is not a website.")
    cache.close()

@cli.command()
def clear_cache():
    """
    Clear all saved results from cache.
    """
    cache = CacheManager()
    result = cache.clear_cache()
    cache.close()
    if result:
        click.echo('Cache has cleared successfully!')
        return
    click.echo('Failed to clear cache!')

