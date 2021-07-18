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
class PurlUtils:
    # pkg:github/package-url/purl-spec@244fd47e07d1004f0aed9c
    # scheme:type/namespace/name@version?qualifiers#subpath
    def __init__(self):
        self.purl_parts = {}

    def parse_host_part(self, purl_main):
        host_list = purl_main.split('/')
        if len(host_list) < 3:
            self.purl_parts = {}
            return 1

        purl_postname = []
        for i in range(len(host_list)):
            if i == 0:
                self.purl_parts['type'] = host_list[i]
            if i == 1:
                self.purl_parts['namespace'] = host_list[i]
            if i == 2:
                purl_postname = host_list[i].split('@')
                self.purl_parts['name'] = purl_postname[0]

        if len(purl_postname) == 2:
            self.purl_parts['version'] = purl_postname[1]

    def parse_params_part(self, purl_params):
        params_list = purl_params.split('#')
        for i in range(len(params_list)):
            if i == 0:
                self.purl_parts['qualifiers'] = params_list[i]
            if i == 1:
                self.purl_parts['subpath'] = params_list[i]