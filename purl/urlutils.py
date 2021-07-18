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
class UrlUtils:
    # pkg:github/package-url/purl-spec@244fd47e07d1004f0aed9c
    # scheme:type/namespace/name@version?qualifiers#subpath
    def __init__(self):
        self.purl_parts = {}

    def get_purl(self, repository, community, component_name, component_version='', url_params={}, subpath=''):
        return None