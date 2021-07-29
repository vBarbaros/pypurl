def parse_purl(purl, purl_dict):
    purl_list = purl.split(':')
    if len(purl_list) != 2:
        return {}

    purl_dict['scheme'] = purl_list[0]

    tmp_lst = purl_list[1].split('?')

    host_list = tmp_lst[0].split('/')
    if len(host_list) < 3:
        return {}

    purl_postname = []
    for i in range(len(host_list)):
        if i == 0:
            purl_dict['type'] = host_list[i]
        if i == 1:
            purl_dict['namespace'] = host_list[i]
        if i == 2:
            purl_postname = host_list[i].split('@')
            purl_dict['name'] = purl_postname[0]

    if purl_dict['type'] == '' or purl_dict['namespace'] == '' or purl_dict['name'] == '':
        return {}

    if len(purl_postname) == 2:
        purl_dict['version'] = purl_postname[1]

    if purl_dict != {} and len(tmp_lst) == 2:
        parse_params_part(tmp_lst[1], purl_dict)
    return purl_dict


def parse_params_part(purl_params, purl_dict):
    params_list = purl_params.split('#')
    for i in range(len(params_list)):
        if i == 0:
            purl_dict['qualifiers'] = params_list[i]
        if i == 1:
            purl_dict['subpath'] = params_list[i]
    return purl_dict


def build_host_part(purl_dict):
    purl = ''
    try:
        if purl_dict['type'] == '' or purl_dict['type'] is None or \
                purl_dict['namespace'] == '' or purl_dict['namespace'] is None or \
                purl_dict['name'] == '' or purl_dict['name'] is None:
            return ''

        purl = 'pkg:' + str(purl_dict['type']) + '/' + str(purl_dict['namespace']) + '/' + str(purl_dict['name'])
    except KeyError:
        return ''
    return purl


def build_params_part(purl_dict, purl):
    try:
        # add optional params
        if purl_dict['version'] == '' or purl_dict['version'] is None:
            return purl

        purl = purl + '@' + str(purl_dict['version'])

        if purl_dict['qualifiers'] == '' or purl_dict['qualifiers'] is None:
            return purl

        purl = purl + '?' + str(purl_dict['qualifiers'])

        if purl_dict['subpath'] == '' or purl_dict['subpath'] is None:
            return purl

        purl = purl + '#' + str(purl_dict['subpath'])
    except KeyError:
        return purl
    return purl


def parse_durl(download_url):
    durl_list = download_url.split('://')
    if len(durl_list) < 2:
        return {}

    durl_info_list = durl_list[1].split('/')
    if len(durl_info_list) < 3:
        return {}

    purl_dict = {}
    purl_dict['scheme'] = 'pkg'

    type_lst = durl_info_list[0].split('.')
    if len(type_lst) < 2:
        return {}
    purl_dict['type'] = type_lst[0]

    if durl_info_list[1] == '':
        return {}
    purl_dict['namespace'] = durl_info_list[1]

    if durl_info_list[2] == '':
        return {}
    purl_dict['name'] = durl_info_list[2]
    return purl_dict


def build_purl_from_params(type, namespace, name, version, qualifiers, subpath):
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


def build_purl_dict_from_params_optionals(purl_dict, version, qualifiers, subpath):
    if version == '' or version is None:
        return purl_dict

    purl_dict['version'] = version

    if qualifiers == '' or qualifiers is None:
        return purl_dict

    purl_dict['qualifiers'] = str(qualifiers)

    if subpath == '' or subpath is None:
        return purl_dict

    purl_dict['subpath'] = str(subpath)
    return purl_dict