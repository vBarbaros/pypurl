"""
The definition for each components is:

scheme: this is the URL scheme with the constant value of "pkg". One of the primary reason for this single scheme is to
        facilitate the future official registration of the "pkg" scheme for package URLs. Required.

type: the package "type" or package "protocol" such as maven, npm, nuget, gem, pypi, etc. Required.

namespace: some name prefix such as a Maven groupid, a Docker image owner, a GitHub user or organization.
           Optional and type-specific.

name: the name of the package. Required.

version: the version of the package. Optional.

qualifiers: extra qualifying data for a package such as an OS, architecture, a distro, etc. Optional and type-specific.

subpath: extra subpath within a package, relative to the package root. Optional.
"""

from purl.purlutils import PurlUtils


class Purl:
    """

    """
    def __init__(self):
        self.utils = PurlUtils()

    def purl_to_dict(self, purl):
        purl_list = purl.split(':')
        if len(purl_list) != 2:
            return {}

        self.utils.purl_parts['scheme'] = purl_list[0]

        tmp_lst = purl_list[1].split('?')
        self.utils.parse_host_part(tmp_lst[0])
        if len(tmp_lst) == 2 and self.utils.purl_parts != {}:
            self.utils.parse_params_part(tmp_lst[1])

        return self.utils.purl_parts

    def durl_to_dict(self, download_url, version='', qualifiers='', subpath=''):
        """

        :param download_url:
        :param version:
        :param qualifiers:
        :param subpath:
        :return:
        """
        durl_list = download_url.split('://')
        print(durl_list)
        durl_info_list = durl_list[1].split('/')
        print(durl_info_list)

        durl_dict = {}
        durl_dict['scheme'] = 'pkg'
        durl_dict['type'] = durl_info_list[0].split('.')[0]
        durl_dict['namespace'] = durl_info_list[1]
        durl_dict['name'] = durl_info_list[2]

        if version == '' or version is None:
            return durl_dict

        durl_dict['version'] = version

        if qualifiers == '' or qualifiers is None:
            return durl_dict

        durl_dict['qualifiers'] =  str(qualifiers)

        if subpath == '' or subpath is None:
            return durl_dict

        durl_dict['subpath'] = str(subpath)
        return durl_dict


    def params_to_purl(self, type, namespace, name, version='', qualifiers='', subpath=''):
        """

        :param type:
        :param namespace:
        :param name:
        :param version:
        :param qualifiers:
        :param subpath:
        :return:
        """
        purl = ''
        if type == '' or type is None or \
                namespace == '' or namespace is None or \
                name == '' or name is None:
            return purl

        purl = 'pkg:' + str(type) + '/' + str(namespace) + '/' + str(name)

        # add optional params
        if version == '' or version is None:
            return purl

        purl = purl + '@' + str(version)

        if qualifiers == '' or qualifiers is None:
            return purl

        purl = purl + '?' + str(qualifiers)

        if subpath == '' or subpath is None:
            return purl

        purl = purl + '#' + str(subpath)
        return purl

    def dict_to_purl(self, dict):
        """

        :param dict:
        :return:
        """
        purl = ''
        try:
            if dict['type'] == '' or dict['type'] is None or \
                    dict['namespace'] == '' or dict['namespace'] is None or \
                    dict['name'] == '' or dict['name'] is None:
                return purl

            purl = 'pkg:' + str(dict['type']) + '/' + str(dict['namespace']) + '/' + str(dict['name'])
        except KeyError:
            return {}

        try:
            # add optional params
            if dict['version'] == '' or dict['version'] is None:
                return purl

            purl = purl + '@' + str(dict['version'])

            if dict['qualifiers'] == '' or dict['qualifiers'] is None:
                return purl

            purl = purl + '?' + str(dict['qualifiers'])

            if dict['subpath'] == '' or dict['subpath'] is None:
                return purl

            purl = purl + '#' + str(dict['subpath'])
        except KeyError:
            return purl

        return purl
