#Lightweight solution to build / handle Package URLs

###Install:
`cd pypurl` and 
`pip3 install -e .`

###Run Tests:
`pytest tests`

###Main concepts:

The definition for each components is:

####scheme: 
this is the URL scheme with the constant value of "pkg". One of the primary reason for this single scheme is to
        facilitate the future official registration of the "pkg" scheme for package URLs. Required.

####type (required): 
the package "type" or package "protocol" such as maven, npm, nuget, gem, pypi, etc.

####namespace: 
some name prefix such as a Maven groupid, a Docker image owner, a GitHub user or organization.
           Optional and type-specific.

####name (required): 
the name of the package.

####version (optional): 
the version of the package.

####qualifiers (optional): 
extra qualifying data for a package such as an OS, architecture, a distro, etc. Type-specific.

####subpath (optional): 
extra subpath within a package, relative to the package root.