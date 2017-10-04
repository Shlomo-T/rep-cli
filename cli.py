import click
from cli_app.censys_adapter import CensysWebsitesAdapter
from censys.base import CensysUnauthorizedException
from cli_app.utils import *

@click.group()
def cli():
    """rep cli built in order to let users research easily about ipv4 addresses and domains using censys service"""
    pass


@cli.command()
@click.argument('censys-credentials')
def configure(censys_credentials):
    """
    Stores your Censys credentials locally for sending Censys api requests
    :param censys_credentials:  help='Censys credentials in the format of <api-id>|<api-secret>'
    :return:
    """
    # TODO: store credentials in local cache
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
            print e
        return
    click.echo('Credentials not in the format!')


@cli.command()
@click.option('--nocache', default=False, help='a flag to determine if to use cache or not')
@click.argument('source')
def scan(nocache, source):
    """
    Scan the source to detect if its a website. In case it does return title and top 10 words on the website.
    --nocache flag detemines if to pull/store results in inner cache.
    :param nocache:
    :param source: 'ipv4 or domain address to scan'
    :return:
    """
    #TODO: detect if the source is valid website or not, in case it does process the website and return result,
    # otherwise echo message to notify the user about the source

    censys_credentials = get_censys_credentials()
    censys_adapter = CensysWebsitesAdapter(*censys_credentials)
    if censys_adapter.is_website(source):
        result = parse_website_content(source)
        if not nocache:
            cache = CacheManager()
            cache.set(source, result)
            cache.close()
            click.echo("Results saved to cache")
        click.echo('Result : %s' % result)
        return
    click.echo("This source is not a website.")

@cli.command()
def clear_cache():
    """
    Clear all saved results from cache.
    :return:
    """
    cache = CacheManager()
    result = cache.clear_cache()
    cache.close()
    if result:
        click.echo('Cache has cleared successfully!')
        return
    click.echo('Failed to clear cache!')

