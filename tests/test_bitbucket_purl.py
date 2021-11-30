import unittest
from pypurl.purl import Purl


class BitbucketPurlTestCase(unittest.TestCase):
    def setUp(self):
        self.purl_obj = Purl()
        print('Running BitBucket-repository tests... OK')

    def test_bitbucket_purl_to_dict_version_success(self):
        purl_with_version = 'pkg:bitbucket/pypy/numpy@4f9778cd49a4'
        r = self.purl_obj.purl_to_dict(purl_with_version)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'bitbucket')
        self.assertEqual(r['namespace'], 'pypy')
        self.assertEqual(r['name'], 'numpy')
        self.assertEqual(r['version'], '4f9778cd49a4')

    def test_bitbucket_purl_to_dict_version_qualifier_success(self):
        purl_with_version_qualifiers = 'pkg:bitbucket/pypy/numpy@4f9778cd49a4?param1=one,param2=two'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'bitbucket')
        self.assertEqual(r['namespace'], 'pypy')
        self.assertEqual(r['name'], 'numpy')
        self.assertEqual(r['version'], '4f9778cd49a4')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')

    def test_bitbucket_purl_to_dict_version_qualifier_path_success(self):
        purl_with_version_qualifiers_subpath = 'pkg:bitbucket/pypy/numpy@4f9778cd49a4?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'bitbucket')
        self.assertEqual(r['namespace'], 'pypy')
        self.assertEqual(r['name'], 'numpy')
        self.assertEqual(r['version'], '4f9778cd49a4')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')
        self.assertEqual(r['subpath'], '/src/main/sub-path')

    def test_bitbucket_purl_to_dict_no_pkg_fail(self):
        purl_with_version_qualifiers_subpath = 'bitbucket/pypy/numpy@4f9778cd49a4?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_bitbucket_purl_to_dict_no_type_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:pypy/numpy@4f9778cd49a4?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_bitbucket_purl_to_dict_no_namespace_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:bitbucket/numpy@4f9778cd49a4?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_bitbucket_purl_to_dict_no_name_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:bitbucket/pypy@4f9778cd49a4?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_bitbucket_purl_to_dict_no_type_wrong_url_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:/pypy/numpy@4f9778cd49a4?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_bitbucket_purl_to_dict_no_namespace_wrong_url_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:bitbucket//numpy@4f9778cd49a4?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_bitbucket_purl_to_dict_no_name_wrong_url_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:bitbucket/pypy/@4f9778cd49a4?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_bitbucket_durl_to_dict_all_success(self):
        durl = 'https://bitbucket.org/pypy/numpy/get/4f9778cd49a4.zip'
        r = self.purl_obj.durl_to_dict(durl, '4f9778cd49a4', 'param1=one,param2=two', '/src/main/sub-path')
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'bitbucket')
        self.assertEqual(r['namespace'], 'pypy')
        self.assertEqual(r['name'], 'numpy')
        self.assertEqual(r['version'], '4f9778cd49a4')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')
        self.assertEqual(r['subpath'], '/src/main/sub-path')

    def test_bitbucket_durl_to_dict_version_qualifier_success(self):
        durl = 'https://bitbucket.org/pypy/numpy/get/4f9778cd49a4.zip'
        r = self.purl_obj.durl_to_dict(durl, '4f9778cd49a4', 'param1=one,param2=two')
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'bitbucket')
        self.assertEqual(r['namespace'], 'pypy')
        self.assertEqual(r['name'], 'numpy')
        self.assertEqual(r['version'], '4f9778cd49a4')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')

    def test_bitbucket_durl_to_dict_version_success(self):
        durl = 'https://bitbucket.org/pypy/numpy/get/4f9778cd49a4.zip'
        r = self.purl_obj.durl_to_dict(durl, '4f9778cd49a4')
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'bitbucket')
        self.assertEqual(r['namespace'], 'pypy')
        self.assertEqual(r['name'], 'numpy')
        self.assertEqual(r['version'], '4f9778cd49a4')

    def test_bitbucket_durl_to_dict_main_success(self):
        durl = 'https://bitbucket.org/pypy/numpy/get/4f9778cd49a4.zip'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'bitbucket')
        self.assertEqual(r['namespace'], 'pypy')
        self.assertEqual(r['name'], 'numpy')

    def test_bitbucket_durl_to_dict_main_wrong_http_fail(self):
        durl = 'https:bitbucket.org/pypy/numpy/get/4f9778cd49a4.zip'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r, {})

    def test_bitbucket_durl_to_dict_main_wrong_type_fail(self):
        durl = 'https://bitbucket/pypy/numpy/get/4f9778cd49a4.zip'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r, {})

    def test_bitbucket_durl_to_dict_main_wrong_namespace_fail(self):
        durl = 'https://bitbucket.org//numpy/get/4f9778cd49a4.zip'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r, {})

    def test_bitbucket_durl_to_dict_main_wrong_name_fail(self):
        durl = 'https://bitbucket.org/pypy//get/4f9778cd49a4.zip'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r, {})

    def test_bitbucket_durl_to_purl_all_success(self):
        durl = 'https://bitbucket.org/pypy/numpy/get/4f9778cd49a4.zip'
        r = self.purl_obj.durl_to_purl(durl, '4f9778cd49a4', 'param1=one,param2=two', '/src/main/sub-path')
        p = 'pkg:bitbucket/pypy/numpy@4f9778cd49a4?param1=one,param2=two#/src/main/sub-path'
        self.assertEqual(r, p)

    def test_bitbucket_durl_to_purl_version_qualifier_success(self):
        durl = 'https://bitbucket.org/pypy/numpy/get/4f9778cd49a4.zip'
        r = self.purl_obj.durl_to_purl(durl, '4f9778cd49a4', 'param1=one,param2=two')
        p = 'pkg:bitbucket/pypy/numpy@4f9778cd49a4?param1=one,param2=two'
        self.assertEqual(r, p)

    def test_bitbucket_durl_to_purl_version_success(self):
        durl = 'https://bitbucket.org/pypy/numpy/get/4f9778cd49a4.zip'
        r = self.purl_obj.durl_to_purl(durl, '4f9778cd49a4')
        p = 'pkg:bitbucket/pypy/numpy@4f9778cd49a4'
        self.assertEqual(r, p)

    def test_bitbucket_durl_to_purl_main_success(self):
        durl = 'https://bitbucket.org/pypy/numpy/get/4f9778cd49a4.zip'
        r = self.purl_obj.durl_to_purl(durl)
        p = 'pkg:bitbucket/pypy/numpy'
        self.assertEqual(r, p)

    def test_bitbucket_params_to_purl_all_success(self):
        r = self.purl_obj.params_to_purl('bitbucket', 'pypy', 'numpy', '4f9778cd49a4', 'param1=one,param2=two',
                                         '/src/main/sub-path')
        p = 'pkg:bitbucket/pypy/numpy@4f9778cd49a4?param1=one,param2=two#/src/main/sub-path'
        self.assertEqual(r, p)

    def test_bitbucket_params_to_purl_version_qualifier_success(self):
        r = self.purl_obj.params_to_purl('bitbucket', 'pypy', 'numpy', '4f9778cd49a4', 'param1=one,param2=two')
        p = 'pkg:bitbucket/pypy/numpy@4f9778cd49a4?param1=one,param2=two'
        self.assertEqual(r, p)

    def test_bitbucket_params_to_purl_version_success(self):
        r = self.purl_obj.params_to_purl('bitbucket', 'pypy', 'numpy', '4f9778cd49a4')
        p = 'pkg:bitbucket/pypy/numpy@4f9778cd49a4'
        self.assertEqual(r, p)

    def test_bitbucket_params_to_purl_main_success(self):
        r = self.purl_obj.params_to_purl('bitbucket', 'pypy', 'numpy')
        p = 'pkg:bitbucket/pypy/numpy'
        self.assertEqual(r, p)


if __name__ == '__main__':
    unittest.main()
