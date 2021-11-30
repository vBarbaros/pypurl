import unittest
from pypurl.purl import Purl


class PypiPurlTestCase(unittest.TestCase):
    def setUp(self):
        self.purl_obj = Purl()
        print('Running npm-registry tests... OK')

    def test_npm_purl_to_dict_version_success(self):
        purl_with_version = 'pkg:npm/@angular/cli@13.0.3'
        r = self.purl_obj.purl_to_dict(purl_with_version)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'npm')
        self.assertEqual(r['namespace'], '@angular')
        self.assertEqual(r['name'], 'cli')
        self.assertEqual(r['version'], '13.0.3')

    def test_npm_purl_to_dict_version_no_namespace_success(self):
        purl_with_version = 'pkg:npm/swiper@7.3.1'
        r = self.purl_obj.purl_to_dict(purl_with_version)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'npm')
        self.assertEqual(r['namespace'], '')
        self.assertEqual(r['name'], 'swiper')
        self.assertEqual(r['version'], '7.3.1')

    def test_npm_purl_to_dict_version_qualifier_success(self):
        purl_with_version_qualifiers = 'pkg:npm/@angular/cli@13.0.3?param1=one,param2=two'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'npm')
        self.assertEqual(r['namespace'], '@angular')
        self.assertEqual(r['name'], 'cli')
        self.assertEqual(r['version'], '13.0.3')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')

    def test_npm_purl_to_dict_version_qualifier_no_namespace_success(self):
        purl_with_version_qualifiers = 'pkg:npm/swiper@7.3.1?param1=one,param2=two'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'npm')
        self.assertEqual(r['namespace'], '')
        self.assertEqual(r['name'], 'swiper')
        self.assertEqual(r['version'], '7.3.1')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')

    def test_npm_purl_to_dict_version_qualifier_path_success(self):
        purl_with_version_qualifiers_subpath = 'pkg:npm/@angular/cli@13.0.3?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'npm')
        self.assertEqual(r['namespace'], '@angular')
        self.assertEqual(r['name'], 'cli')
        self.assertEqual(r['version'], '13.0.3')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')
        self.assertEqual(r['subpath'], '/src/main/sub-path')

    def test_npm_purl_to_dict_version_qualifier_path_no_namespace_success(self):
        purl_with_version_qualifiers_subpath = 'pkg:npm/swiper@7.3.1?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'npm')
        self.assertEqual(r['namespace'], '')
        self.assertEqual(r['name'], 'swiper')
        self.assertEqual(r['version'], '7.3.1')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')
        self.assertEqual(r['subpath'], '/src/main/sub-path')

    def test_npm_purl_to_dict_no_pkg_fail(self):
        purl_with_version_qualifiers_subpath = 'npm/swiper@7.3.1?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_npm_purl_to_dict_no_type_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:swiper@7.3.1?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_npm_purl_to_dict_no_name_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:npm@7.3.1?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_npm_purl_to_dict_no_type_wrong_url_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:/swiper@7.3.1?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_npm_purl_to_dict_no_name_wrong_url_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:npm/@7.3.1?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_npm_durl_to_dict_all_no_namespace_success(self):
        durl = 'https://www.npmjs.com/package/swiper/v/7.3.1'
        r = self.purl_obj.durl_to_dict(durl, '7.3.1', 'param1=one,param2=two', '/src/main/sub-path')
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'npm')
        self.assertEqual(r['namespace'], '')
        self.assertEqual(r['name'], 'swiper')
        self.assertEqual(r['version'], '7.3.1')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')
        self.assertEqual(r['subpath'], '/src/main/sub-path')

    def test_npm_durl_to_dict_all_success(self):
        durl = 'https://www.npmjs.com/package/@angular/cli/v/13.0.3'
        r = self.purl_obj.durl_to_dict(durl, '13.0.3', 'param1=one,param2=two', '/src/main/sub-path')
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'npm')
        self.assertEqual(r['namespace'], '@angular')
        self.assertEqual(r['name'], 'cli')
        self.assertEqual(r['version'], '13.0.3')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')
        self.assertEqual(r['subpath'], '/src/main/sub-path')

    def test_npm_durl_to_dict_version_qualifier_success(self):
        durl = 'https://www.npmjs.com/package/@angular/cli/v/13.0.3'
        r = self.purl_obj.durl_to_dict(durl, '13.0.3', 'param1=one,param2=two')
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'npm')
        self.assertEqual(r['namespace'], '@angular')
        self.assertEqual(r['name'], 'cli')
        self.assertEqual(r['version'], '13.0.3')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')

    def test_npm_durl_to_dict_version_qualifier_no_namespace_success(self):
        durl = 'https://www.npmjs.com/package/swiper/v/7.3.1'
        r = self.purl_obj.durl_to_dict(durl, '7.3.1', 'param1=one,param2=two')
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'npm')
        self.assertEqual(r['namespace'], '')
        self.assertEqual(r['name'], 'swiper')
        self.assertEqual(r['version'], '7.3.1')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')

    def test_npm_durl_to_dict_version_success(self):
        durl = 'https://www.npmjs.com/package/@angular/cli/v/13.0.3'
        r = self.purl_obj.durl_to_dict(durl, '13.0.3')
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'npm')
        self.assertEqual(r['namespace'], '@angular')
        self.assertEqual(r['name'], 'cli')
        self.assertEqual(r['version'], '13.0.3')

    def test_npm_durl_to_dict_version_no_namespace_success(self):
        durl = 'https://www.npmjs.com/package/swiper/v/7.3.1'
        r = self.purl_obj.durl_to_dict(durl, '7.3.1')
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'npm')
        self.assertEqual(r['namespace'], '')
        self.assertEqual(r['name'], 'swiper')
        self.assertEqual(r['version'], '7.3.1')

    def test_npm_durl_to_dict_main_success(self):
        durl = 'https://www.npmjs.com/package/@angular/cli/v/13.0.3'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'npm')
        self.assertEqual(r['namespace'], '@angular')
        self.assertEqual(r['name'], 'cli')

    def test_npm_durl_to_dict_main_no_namespace_success(self):
        durl = 'https://www.npmjs.com/package/swiper/v/7.3.1'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'npm')
        self.assertEqual(r['namespace'], '')
        self.assertEqual(r['name'], 'swiper')

    def test_npm_durl_to_dict_main_wrong_http_fail(self):
        durl = 'https:www.npmjs.com/package/swiper/v/7.3.1'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r, {})

    def test_npm_durl_to_dict_main_wrong_type_fail(self):
        durl = 'https://npmjs/package/swiper/v/7.3.1'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r, {})

    def test_npm_durl_to_dict_main_wrong_namespace_fail(self):
        durl = 'https://www.npmjs.com/package//swiper/v/7.3.1'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r, {})

    def test_npm_durl_to_dict_main_wrong_name_fail(self):
        durl = 'https://www.npmjs.com/package//v/7.3.1'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r, {})

    def test_npm_durl_to_purl_all_success(self):
        durl = 'https://www.npmjs.com/package/@angular/cli/v/13.0.3'
        actual = self.purl_obj.durl_to_purl(durl, '13.0.3', 'param1=one,param2=two', '/src/main/sub-path')
        expect = 'pkg:npm/@angular/cli@13.0.3?param1=one,param2=two#/src/main/sub-path'
        self.assertEqual(expect, actual)

    def test_npm_durl_to_purl_all_no_namespace_success(self):
        durl = 'https://www.npmjs.com/package/swiper/v/7.3.1'
        actual = self.purl_obj.durl_to_purl(durl, '7.3.1', 'param1=one,param2=two', '/src/main/sub-path')
        expect = 'pkg:npm/swiper@7.3.1?param1=one,param2=two#/src/main/sub-path'
        self.assertEqual(expect, actual)

    def test_npm_durl_to_purl_version_qualifier_success(self):
        durl = 'https://www.npmjs.com/package/@angular/cli/v/13.0.3'
        actual = self.purl_obj.durl_to_purl(durl, '13.0.3', 'param1=one,param2=two')
        expect = 'pkg:npm/@angular/cli@13.0.3?param1=one,param2=two'
        self.assertEqual(expect, actual)

    def test_npm_durl_to_purl_version_qualifier_no_namespace_success(self):
        durl = 'https://www.npmjs.com/package/swiper/v/7.3.1'
        actual = self.purl_obj.durl_to_purl(durl, '7.3.1', 'param1=one,param2=two')
        expect = 'pkg:npm/swiper@7.3.1?param1=one,param2=two'
        self.assertEqual(expect, actual)

    def test_npm_durl_to_purl_version_success(self):
        durl = 'https://www.npmjs.com/package/@angular/cli/v/13.0.3'
        actual = self.purl_obj.durl_to_purl(durl, '13.0.3')
        expect = 'pkg:npm/@angular/cli@13.0.3'
        self.assertEqual(expect, actual)

    def test_npm_durl_to_purl_version_no_namespace_success(self):
        durl = 'https://www.npmjs.com/package/swiper/v/7.3.1'
        actual = self.purl_obj.durl_to_purl(durl, '7.3.1')
        expect = 'pkg:npm/swiper@7.3.1'
        self.assertEqual(expect, actual)

    def test_npm_durl_to_purl_main_success(self):
        durl = 'https://www.npmjs.com/package/@angular/cli/v/13.0.3'
        actual = self.purl_obj.durl_to_purl(durl)
        expect = 'pkg:npm/@angular/cli'
        self.assertEqual(expect, actual)

    def test_npm_durl_to_purl_main_no_namespace_success(self):
        durl = 'https://www.npmjs.com/package/swiper/v/7.3.1'
        actual = self.purl_obj.durl_to_purl(durl)
        expect = 'pkg:npm/swiper'
        self.assertEqual(expect, actual)

    def test_npm_params_to_purl_all_success(self):
        r = self.purl_obj.params_to_purl('npm', '', 'swiper', '7.3.1', 'param1=one,param2=two', '/src/main/sub-path')
        p = 'pkg:npm/swiper@7.3.1?param1=one,param2=two#/src/main/sub-path'
        self.assertEqual(r, p)

    def test_npm_params_to_purl_version_qualifier_success(self):
        r = self.purl_obj.params_to_purl('npm', '', 'swiper', '7.3.1', 'param1=one,param2=two')
        p = 'pkg:npm/swiper@7.3.1?param1=one,param2=two'
        self.assertEqual(r, p)

    def test_npm_params_to_purl_version_success(self):
        r = self.purl_obj.params_to_purl('npm', '', 'swiper', '7.3.1')
        p = 'pkg:npm/swiper@7.3.1'
        self.assertEqual(r, p)

    def test_npm_params_to_purl_main_success(self):
        r = self.purl_obj.params_to_purl('npm', '', 'swiper')
        p = 'pkg:npm/swiper'
        self.assertEqual(r, p)


if __name__ == '__main__':
    unittest.main()
