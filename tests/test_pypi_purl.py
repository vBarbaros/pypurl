import unittest
from pypurl.purl import Purl


class PypiPurlTestCase(unittest.TestCase):
    def setUp(self):
        self.purl_obj = Purl()
        print('Running pypi-repository tests... OK')

    def test_pypi_purl_to_dict_version_success(self):
        purl_with_version = 'pkg:pypi/notificationcenter@1.0.0b2'
        r = self.purl_obj.purl_to_dict(purl_with_version)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'pypi')
        self.assertEqual(r['namespace'], '')
        self.assertEqual(r['name'], 'notificationcenter')
        self.assertEqual(r['version'], '1.0.0b2')

    def test_pypi_purl_to_dict_version_qualifier_success(self):
        purl_with_version_qualifiers = 'pkg:pypi/notificationcenter@1.0.0b2?param1=one,param2=two'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'pypi')
        self.assertEqual(r['namespace'], '')
        self.assertEqual(r['name'], 'notificationcenter')
        self.assertEqual(r['version'], '1.0.0b2')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')

    def test_pypi_purl_to_dict_version_qualifier_path_success(self):
        purl_with_version_qualifiers_subpath = 'pkg:pypi/notificationcenter@1.0.0b2?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'pypi')
        self.assertEqual(r['namespace'], '')
        self.assertEqual(r['name'], 'notificationcenter')
        self.assertEqual(r['version'], '1.0.0b2')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')
        self.assertEqual(r['subpath'], '/src/main/sub-path')

    def test_pypi_purl_to_dict_no_pkg_fail(self):
        purl_with_version_qualifiers_subpath = 'pypi/notificationcenter@1.0.0b2?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_pypi_purl_to_dict_no_type_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:notificationcenter@1.0.0b2?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_pypi_purl_to_dict_no_namespace_success(self):
        purl_with_version_qualifiers_subpath = 'pkg:pypi/notificationcenter@1.0.0b2?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'pypi')
        self.assertEqual(r['namespace'], '')
        self.assertEqual(r['name'], 'notificationcenter')
        self.assertEqual(r['version'], '1.0.0b2')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')
        self.assertEqual(r['subpath'], '/src/main/sub-path')

    def test_pypi_purl_to_dict_no_name_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:pypi@1.0.0b2?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_pypi_purl_to_dict_no_type_wrong_url_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:/notificationcenter@1.0.0b2?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_pypi_purl_to_dict_no_name_wrong_url_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:pypi/@1.0.0b2?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_pypi_durl_to_dict_all_success(self):
        durl = 'https://pypi.org/project/notificationcenter/1.0.0b2/'
        r = self.purl_obj.durl_to_dict(durl, '1.0.0b2', 'param1=one,param2=two', '/src/main/sub-path')
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'pypi')
        self.assertEqual(r['namespace'], '')
        self.assertEqual(r['name'], 'notificationcenter')
        self.assertEqual(r['version'], '1.0.0b2')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')
        self.assertEqual(r['subpath'], '/src/main/sub-path')

    def test_pypi_durl_to_dict_version_qualifier_success(self):
        durl = 'https://pypi.org/project/notificationcenter/1.0.0b2/'
        r = self.purl_obj.durl_to_dict(durl, '1.0.0b2', 'param1=one,param2=two')
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'pypi')
        self.assertEqual(r['namespace'], '')
        self.assertEqual(r['name'], 'notificationcenter')
        self.assertEqual(r['version'], '1.0.0b2')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')

    def test_pypi_durl_to_dict_version_success(self):
        durl = 'https://pypi.org/project/notificationcenter/1.0.0b2/'
        r = self.purl_obj.durl_to_dict(durl, '1.0.0b2')
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'pypi')
        self.assertEqual(r['namespace'], '')
        self.assertEqual(r['name'], 'notificationcenter')
        self.assertEqual(r['version'], '1.0.0b2')

    def test_pypi_durl_to_dict_main_success(self):
        durl = 'https://pypi.org/project/notificationcenter/1.0.0b2/'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'pypi')
        self.assertEqual(r['namespace'], '')
        self.assertEqual(r['name'], 'notificationcenter')

    def test_pypi_durl_to_dict_main_wrong_http_fail(self):
        durl = 'https:pypi.org/project/notificationcenter/1.0.0b2/'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r, {})

    def test_pypi_durl_to_dict_main_wrong_type_fail(self):
        durl = 'https://pypi/project/notificationcenter/1.0.0b2/'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r, {})

    def test_pypi_durl_to_dict_main_wrong_namespace_fail(self):
        durl = 'https://pypi.org//notificationcenter/1.0.0b2/'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r, {})

    def test_pypi_durl_to_dict_main_wrong_name_fail(self):
        durl = 'https://pypi.org/project//1.0.0b2/'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r, {})

    def test_pypi_durl_to_purl_all_success(self):
        durl = 'https://pypi.org/project/notificationcenter/1.0.0b2/'
        actual = self.purl_obj.durl_to_purl(durl, '1.0.0b2', 'param1=one,param2=two', '/src/main/sub-path')
        expect = 'pkg:pypi/notificationcenter@1.0.0b2?param1=one,param2=two#/src/main/sub-path'
        self.assertEqual(expect, actual)

    def test_pypi_durl_to_purl_version_qualifier_success(self):
        durl = 'https://pypi.org/project/notificationcenter/1.0.0b2/'
        r = self.purl_obj.durl_to_purl(durl, '1.0.0b2', 'param1=one,param2=two')
        p = 'pkg:pypi/notificationcenter@1.0.0b2?param1=one,param2=two'
        self.assertEqual(r, p)

    def test_pypi_durl_to_purl_version_success(self):
        durl = 'https://pypi.org/project/notificationcenter/1.0.0b2/'
        r = self.purl_obj.durl_to_purl(durl, '1.0.0b2')
        p = 'pkg:pypi/notificationcenter@1.0.0b2'
        self.assertEqual(r, p)

    def test_pypi_durl_to_purl_main_success(self):
        durl = 'https://pypi.org/project/notificationcenter/1.0.0b2/'
        r = self.purl_obj.durl_to_purl(durl)
        p = 'pkg:pypi/notificationcenter'
        self.assertEqual(r, p)

    def test_pypi_params_to_purl_all_success(self):
        r = self.purl_obj.params_to_purl('pypi', '', 'notificationcenter', '1.0.0b2', 'param1=one,param2=two',
                                         '/src/main/sub-path')
        p = 'pkg:pypi/notificationcenter@1.0.0b2?param1=one,param2=two#/src/main/sub-path'
        self.assertEqual(r, p)

    def test_pypi_params_to_purl_version_qualifier_success(self):
        r = self.purl_obj.params_to_purl('pypi', '', 'notificationcenter', '1.0.0b2', 'param1=one,param2=two')
        p = 'pkg:pypi/notificationcenter@1.0.0b2?param1=one,param2=two'
        self.assertEqual(r, p)

    def test_pypi_params_to_purl_version_success(self):
        r = self.purl_obj.params_to_purl('pypi', '', 'notificationcenter', '1.0.0b2')
        p = 'pkg:pypi/notificationcenter@1.0.0b2'
        self.assertEqual(r, p)

    def test_pypi_params_to_purl_main_success(self):
        r = self.purl_obj.params_to_purl('pypi', '', 'notificationcenter')
        p = 'pkg:pypi/notificationcenter'
        self.assertEqual(r, p)


if __name__ == '__main__':
    unittest.main()
