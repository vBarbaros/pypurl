import unittest
from pypurl.purl import Purl

class GithubPurlTestCase(unittest.TestCase):
    def setUp(self):
        self.purl_obj = Purl()

    def test_github_purl_to_dict_version_success(self):
        purl_with_version = 'pkg:github/package-url/pypurl-spec@244fd47e07d1004f0aed9c'
        r = self.purl_obj.purl_to_dict(purl_with_version)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'github')
        self.assertEqual(r['namespace'], 'package-url')
        self.assertEqual(r['name'], 'pypurl-spec')
        self.assertEqual(r['version'], '244fd47e07d1004f0aed9c')

    def test_github_purl_to_dict_version_qualifier_success(self):
        purl_with_version_qualifiers = 'pkg:github/package-url/pypurl-spec@244fd47e07d1004f0aed9c?param1=one,param2=two'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'github')
        self.assertEqual(r['namespace'], 'package-url')
        self.assertEqual(r['name'], 'pypurl-spec')
        self.assertEqual(r['version'], '244fd47e07d1004f0aed9c')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')

    def test_github_purl_to_dict_version_qualifier_path_success(self):
        purl_with_version_qualifiers_subpath = 'pkg:github/package-url/pypurl-spec@244fd47e07d1004f0aed9c?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'github')
        self.assertEqual(r['namespace'], 'package-url')
        self.assertEqual(r['name'], 'pypurl-spec')
        self.assertEqual(r['version'], '244fd47e07d1004f0aed9c')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')
        self.assertEqual(r['subpath'], '/src/main/sub-path')

    def test_github_purl_to_dict_no_pkg_fail(self):
        purl_with_version_qualifiers_subpath = 'github/package-url/pypurl-spec@244fd47e07d1004f0aed9c?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_github_purl_to_dict_no_type_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:package-url/pypurl-spec@244fd47e07d1004f0aed9c?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_github_purl_to_dict_no_namespace_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:github/pypurl-spec@244fd47e07d1004f0aed9c?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_github_purl_to_dict_no_name_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:github/package-url@244fd47e07d1004f0aed9c?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_github_purl_to_dict_no_type_wrong_url_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:/package-url/pypurl-spec@244fd47e07d1004f0aed9c?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_github_purl_to_dict_no_namespace_wrong_url_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:github//pypurl-spec@244fd47e07d1004f0aed9c?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_github_purl_to_dict_no_name_wrong_url_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:github/package-url/@244fd47e07d1004f0aed9c?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_github_durl_to_dict_all_success(self):
        durl = 'https://github.com/vBarbaros/pypurl/archive/refs/heads/main.zip'
        r = self.purl_obj.durl_to_dict(durl, '244fd47e07d1004f0aed9c', 'param1=one,param2=two', '/src/main/sub-path')
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'github')
        self.assertEqual(r['namespace'], 'vBarbaros')
        self.assertEqual(r['name'], 'pypurl')
        self.assertEqual(r['version'], '244fd47e07d1004f0aed9c')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')
        self.assertEqual(r['subpath'], '/src/main/sub-path')

    def test_github_durl_to_dict_version_qualifier_success(self):
        durl = 'https://github.com/vBarbaros/pypurl/archive/refs/heads/main.zip'
        r = self.purl_obj.durl_to_dict(durl, '244fd47e07d1004f0aed9c', 'param1=one,param2=two')
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'github')
        self.assertEqual(r['namespace'], 'vBarbaros')
        self.assertEqual(r['name'], 'pypurl')
        self.assertEqual(r['version'], '244fd47e07d1004f0aed9c')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')

    def test_github_durl_to_dict_version_success(self):
        durl = 'https://github.com/vBarbaros/pypurl/archive/refs/heads/main.zip'
        r = self.purl_obj.durl_to_dict(durl, '244fd47e07d1004f0aed9c')
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'github')
        self.assertEqual(r['namespace'], 'vBarbaros')
        self.assertEqual(r['name'], 'pypurl')
        self.assertEqual(r['version'], '244fd47e07d1004f0aed9c')

    def test_github_durl_to_dict_main_success(self):
        durl = 'https://github.com/vBarbaros/pypurl/archive/refs/heads/main.zip'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'github')
        self.assertEqual(r['namespace'], 'vBarbaros')
        self.assertEqual(r['name'], 'pypurl')

    def test_github_durl_to_dict_main_wrong_http_fail(self):
        durl = 'https:github.com/vBarbaros/pypurl/archive/refs/heads/main.zip'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r, {})

    def test_github_durl_to_dict_main_wrong_type_fail(self):
        durl = 'https://github/vBarbaros/pypurl/archive/refs/heads/main.zip'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r, {})

    def test_github_durl_to_dict_main_wrong_namespace_fail(self):
        durl = 'https://github.com//pypurl/archive/refs/heads/main.zip'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r, {})

    def test_github_durl_to_dict_main_wrong_name_fail(self):
        durl = 'https://github.com/vBarbaros//archive/refs/heads/main.zip'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r, {})

    def test_github_durl_to_purl_all_success(self):
        durl = 'https://github.com/vBarbaros/pypurl/archive/refs/heads/main.zip'
        r = self.purl_obj.durl_to_purl(durl, '244fd47e07d1004f0aed9c', 'param1=one,param2=two', '/src/main/sub-path')
        p = 'pkg:github/vBarbaros/pypurl@244fd47e07d1004f0aed9c?param1=one,param2=two#/src/main/sub-path'
        self.assertEqual(r, p)

    def test_github_durl_to_purl_version_qualifier_success(self):
        durl = 'https://github.com/vBarbaros/pypurl/archive/refs/heads/main.zip'
        r = self.purl_obj.durl_to_purl(durl, '244fd47e07d1004f0aed9c', 'param1=one,param2=two')
        p = 'pkg:github/vBarbaros/pypurl@244fd47e07d1004f0aed9c?param1=one,param2=two'
        self.assertEqual(r, p)

    def test_github_durl_to_purl_version_success(self):
        durl = 'https://github.com/vBarbaros/pypurl/archive/refs/heads/main.zip'
        r = self.purl_obj.durl_to_purl(durl, '244fd47e07d1004f0aed9c')
        p = 'pkg:github/vBarbaros/pypurl@244fd47e07d1004f0aed9c'
        self.assertEqual(r, p)

    def test_github_durl_to_purl_main_success(self):
        durl = 'https://github.com/vBarbaros/pypurl/archive/refs/heads/main.zip'
        r = self.purl_obj.durl_to_purl(durl)
        p = 'pkg:github/vBarbaros/pypurl'
        self.assertEqual(r, p)

    def test_github_params_to_purl_all_success(self):
        r = self.purl_obj.params_to_purl('github', 'vBarbaros', 'pypurl', '244fd47e07d1004f0aed9c', 'param1=one,param2=two', '/src/main/sub-path')
        p = 'pkg:github/vBarbaros/pypurl@244fd47e07d1004f0aed9c?param1=one,param2=two#/src/main/sub-path'
        self.assertEqual(r, p)

    def test_github_params_to_purl_version_qualifier_success(self):
        r = self.purl_obj.params_to_purl('github', 'vBarbaros', 'pypurl', '244fd47e07d1004f0aed9c', 'param1=one,param2=two')
        p = 'pkg:github/vBarbaros/pypurl@244fd47e07d1004f0aed9c?param1=one,param2=two'
        self.assertEqual(r, p)

    def test_github_params_to_purl_version_success(self):
        r = self.purl_obj.params_to_purl('github', 'vBarbaros', 'pypurl', '244fd47e07d1004f0aed9c')
        p = 'pkg:github/vBarbaros/pypurl@244fd47e07d1004f0aed9c'
        self.assertEqual(r, p)

    def test_github_params_to_purl_main_success(self):
        r = self.purl_obj.params_to_purl('github', 'vBarbaros', 'pypurl')
        p = 'pkg:github/vBarbaros/pypurl'
        self.assertEqual(r, p)

if __name__ == '__main__':
    unittest.main()
