# Lightweight solution to build / handle Package URLs

### Install:
`cd pypurl` and 
`pip3 install -e .`

### Run Tests:
`pytest tests`

### Main concepts:

The definition for each components is:

#### scheme 
```
this is the URL scheme with the constant value of "pkg". One of the 
primary reason for this single scheme is to facilitate the future official 
registration of the "pkg" scheme for package URLs. Required.
```

#### type (required)
```
the package "type" or package "protocol" such as github, bitbucket, 
maven, npm, nuget, gem, pypi, etc.
```

#### namespace
```
some name prefix such as a Maven groupid, a Docker image owner, a GitHub user 
or organization. Optional and type-specific.
```

#### name (required)
```
the name of the package.
```

#### version (optional) 
```
the version of the package.
```

#### qualifiers (optional) 
```
extra qualifying data for a package such as an OS, architecture, a distro, etc. 
Type-specific.
```

#### subpath (optional) 
```
extra subpath within a package, relative to the package root.
```

## Current `type` Support: 
* GitHub, 
* BitBucket

## How to Use:

```
# install the package
$ cd pypurl/
$ pip install -e .


# enter interpreter mode
$ python


# import main module
>>> from pypurl.purl import Purl
>>> po = Purl()


# parse the Download URL to dictionary
>>> po.durl_to_dict('https://github.com/vBarbaros/pypurl/archive/refs/heads/main.zip')
{'scheme': 'pkg', 'type': 'github', 'namespace': 'vBarbaros', 'name': 'pypurl'}


# obtain the PURL from the Download URL only
>>> durl = 'https://github.com/vBarbaros/pypurl/archive/refs/heads/main.zip'
>>> po.durl_to_purl(durl)
'pkg:github/vBarbaros/pypurl'


# obtain the PURL from the Download URL + version number/hash-commit
>>> durl = 'https://github.com/vBarbaros/pypurl/archive/refs/heads/main.zip'
>>> po.durl_to_purl(durl, '244fd47e07d1004f0aed9c')
'pkg:github/vBarbaros/pypurl@244fd47e07d1004f0aed9c'


# obtain the PURL from the Download URL + version number/hash-commit + qualifiers
>>> po.durl_to_purl(durl, '244fd47e07d1004f0aed9c', 'param1=one&param2=two&param3=three')
'pkg:github/vBarbaros/pypurl@244fd47e07d1004f0aed9c?param1=one&param2=two&param3=three'


# obtain the PURL from the Download URL + version number/hash-commit + qualifiers + subpath
>>> po.durl_to_purl(durl, '244fd47e07d1004f0aed9c', 'param1=one&param2=two&param3=three', 'some/dummy/path')
'pkg:github/vBarbaros/pypurl@244fd47e07d1004f0aed9c?param1=one&param2=two&param3=three#some/dummy/path'


# parse the PURL containing main fields (+ version) to dictionary
>>> purl = 'pkg:github/vBarbaros/pypurl@244fd47e07d1004f0aed9c'
>>> po.purl_to_dict(purl)
{'scheme': 'pkg', 'type': 'github', 'namespace': 'vBarbaros', 'name': 'pypurl', 'version': '244fd47e07d1004f0aed9c'}


# parse the PURL containing all possible fields, to dictionary
>>> purl = 'pkg:github/vBarbaros/pypurl@244fd47e07d1004f0aed9c?param1=one&param2=two&param3=three#some/dummy/path'
>>> po.purl_to_dict(purl)
{'scheme': 'pkg', 'type': 'github', 'namespace': 'vBarbaros', 'name': 'pypurl', 'version': '244fd47e07d1004f0aed9c', 'qualifiers': 'param1=one&param2=two&param3=three', 'subpath': 'some/dummy/path'}

```