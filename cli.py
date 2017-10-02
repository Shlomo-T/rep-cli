import click


@click.command()
@click.argument('censys-credentials')
def configure(censys_credentials):
    """
    Stores your Censys credentials locally for sending Censys api requests
    :param censys_credentials:  help='Censys credentials in the format of <api-id>|<api-secret>'
    :return:
    """
    # TODO: store credentials in local cache
    click.echo('Your credentials stored successfully!')


@click.command()
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
    pass

@click.command()
def clear_cache():
    """
    Clear all values from cache.
    :return:
    """
    #TODO: clear cache and notify the user
    click.echo('Cache has cleared successfully!')

