# Lightweight solution to build / handle Package URLs

## Current `type` Support: 
* GitHub 
* Gitlab 
* BitBucket
* PyPi
* npm

### Main concepts:

The definition for each component is:

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


## How to Use:
```
# install the package
$ cd pypurl/
$ pip install -e .


# enter interpreter mode
$ python


# import main module
>>> from pypurl.purl import Purl
>>> p = Purl()


# parse the Download URL to dictionary
>>> p.durl_to_dict('https://github.com/vBarbaros/pypurl/archive/refs/heads/main.zip')
{'scheme': 'pkg', 'type': 'github', 'namespace': 'vBarbaros', 'name': 'pypurl'}


# obtain the PURL from the Download URL only
>>> durl = 'https://github.com/vBarbaros/pypurl/archive/refs/heads/main.zip'
>>> p.durl_to_purl(durl)
'pkg:github/vBarbaros/pypurl'


# obtain the PURL from the Download URL + version number/hash-commit
>>> durl = 'https://github.com/vBarbaros/pypurl/archive/refs/heads/main.zip'
>>> p.durl_to_purl(durl, '244fd47e07d1004f0aed9c')
'pkg:github/vBarbaros/pypurl@244fd47e07d1004f0aed9c'


# obtain the PURL from the Download URL + version number/hash-commit + qualifiers
>>> p.durl_to_purl(durl, '244fd47e07d1004f0aed9c', 'param1=one&param2=two&param3=three')
'pkg:github/vBarbaros/pypurl@244fd47e07d1004f0aed9c?param1=one&param2=two&param3=three'


# obtain the PURL from the Download URL + version number/hash-commit + qualifiers + subpath
>>> p.durl_to_purl(durl, '244fd47e07d1004f0aed9c', 'param1=one&param2=two&param3=three', 'some/dummy/path')
'pkg:github/vBarbaros/pypurl@244fd47e07d1004f0aed9c?param1=one&param2=two&param3=three#some/dummy/path'


# parse the PURL containing main fields (+ version) to dictionary
>>> purl = 'pkg:github/vBarbaros/pypurl@244fd47e07d1004f0aed9c'
>>> p.purl_to_dict(purl)
{'scheme': 'pkg', 'type': 'github', 'namespace': 'vBarbaros', 'name': 'pypurl', 'version': '244fd47e07d1004f0aed9c'}


# parse the PURL containing all possible fields, to dictionary
>>> purl = 'pkg:github/vBarbaros/pypurl@244fd47e07d1004f0aed9c?param1=one&param2=two&param3=three#some/dummy/path'
>>> p.purl_to_dict(purl)
{'scheme': 'pkg', 'type': 'github', 'namespace': 'vBarbaros', 'name': 'pypurl', 'version': '244fd47e07d1004f0aed9c', 'qualifiers': 'param1=one&param2=two&param3=three', 'subpath': 'some/dummy/path'}

```

### Install:
```
$ cd pypurl 
$ pip install -e .
```

### Run Tests:
```
$ python -m unittest tests/*.py

# Expected output
...
Ran 138 tests in 0.009s

OK

```


## Credits

While this module represents a simple exercise of mine based on some struggles I heard of people having when working 
with PURLs, the [purl-specs](https://github.com/package-url/purl-spec) page helped me define the roadmap of 
this module


## TODO
- add support for other repositories, besides the currently implemented (GitHub, Gitlab, BitBucket, PyPi)


## [License](https://github.com/vBarbaros/pypurl/blob/main/LICENSE)

MIT © [Victor Barbaros, 2021](https://github.com/vBarbaros)
