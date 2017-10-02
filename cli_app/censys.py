from censys.websites import CensysWebsites


class CensysWebsitesAdapter(object):

    websites_api = CensysWebsites()

    def __init__(self, api_id, api_secret):
        self.websites_api = CensysWebsites(api_id=api_id, api_secret=api_secret)

    def is_website(self, query):
        if list(self.websites_api.search(query)):
            return True
        return False

