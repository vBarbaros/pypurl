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
    # pkg:github/package-url/purl-spec@244fd47e07d1004f0aed9c
    # scheme:type/namespace/name@version?qualifiers#subpath
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

    def to_purl(self, type, namespace, name, version='', qualifiers='', subpath=''):
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