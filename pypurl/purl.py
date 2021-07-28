import pypurl.purlutils as utils


class Purl:
    """ Provides essential functionality to decompose any purl into components
    or build a purl from passed parameters.
    """

    def __init__(self):
        self.type = ''

    def purl_to_dict(self, purl):
        return utils.parse_purl(purl, {})

    def durl_to_dict(self, download_url, version='', qualifiers='', subpath=''):
        purl_dict = utils.parse_durl(download_url)
        return utils.build_purl_dict_from_params_optionals(purl_dict, version, qualifiers, subpath)

    def durl_to_purl(self, download_url, version='', qualifiers='', subpath=''):
        purl_dict = utils.parse_durl(download_url)
        purl_dict = utils.build_purl_dict_from_params_optionals(purl_dict, version, qualifiers, subpath)
        return self.dict_to_purl(purl_dict)

    def dict_to_purl(self, dict):
        purl = utils.build_host_part(dict)
        return utils.build_params_part(dict, purl)

    def params_to_purl(self, type, namespace, name, version='', qualifiers='', subpath=''):
        return utils.build_purl_from_params(type, namespace, name, version, qualifiers, subpath)
