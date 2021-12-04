import unittest
from pypurl.purl import Purl


class RubyGemPurlTestCase(unittest.TestCase):
    def setUp(self):
        self.purl_obj = Purl()
        print('Running ruby-gem-repository tests... OK')

    def test_ruby_gem_purl_to_dict_version_success(self):
        purl_with_version = 'pkg:gem/aws-partitions@1.463.0'
        actual = self.purl_obj.purl_to_dict(purl_with_version)
        self.assertEqual(actual['scheme'], 'pkg')
        self.assertEqual(actual['type'], 'gem')
        self.assertEqual(actual['namespace'], '')
        self.assertEqual(actual['name'], 'aws-partitions')
        self.assertEqual(actual['version'], '1.463.0')

    def test_ruby_gem_purl_to_dict_version_qualifier_success(self):
        purl_with_version_qualifiers = 'pkg:gem/aws-partitions@1.463.0?param1=one,param2=two'
        actual = self.purl_obj.purl_to_dict(purl_with_version_qualifiers)
        self.assertEqual(actual['scheme'], 'pkg')
        self.assertEqual(actual['type'], 'gem')
        self.assertEqual(actual['namespace'], '')
        self.assertEqual(actual['name'], 'aws-partitions')
        self.assertEqual(actual['version'], '1.463.0')
        self.assertEqual(actual['qualifiers'], 'param1=one,param2=two')

    def test_ruby_gem_purl_to_dict_version_qualifier_path_success(self):
        purl_with_version_qualifiers_subpath = 'pkg:gem/aws-partitions@1.463.0?param1=one,param2=two#/src/main/sub-path'
        actual = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(actual['scheme'], 'pkg')
        self.assertEqual(actual['type'], 'gem')
        self.assertEqual(actual['namespace'], '')
        self.assertEqual(actual['name'], 'aws-partitions')
        self.assertEqual(actual['version'], '1.463.0')
        self.assertEqual(actual['qualifiers'], 'param1=one,param2=two')
        self.assertEqual(actual['subpath'], '/src/main/sub-path')

    def test_ruby_gem_purl_to_dict_no_pkg_fail(self):
        'pkg:gem/aws-partitions@1.463.0'
        purl_with_version_qualifiers_subpath = 'gem/aws-partitions@1.463.0?param1=one,param2=two#/src/main/sub-path'
        actual = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(actual, {})

    def test_ruby_gem_purl_to_dict_no_type_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:aws-partitions@1.463.0?param1=one,param2=two#/src/main/sub-path'
        actual = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(actual, {})

    def test_ruby_gem_purl_to_dict_no_namespace_success(self):
        purl_with_version_qualifiers_subpath = 'pkg:gem/aws-partitions@1.463.0?param1=one,param2=two#/src/main/sub-path'
        actual = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(actual['scheme'], 'pkg')
        self.assertEqual(actual['type'], 'gem')
        self.assertEqual(actual['namespace'], '')
        self.assertEqual(actual['name'], 'aws-partitions')
        self.assertEqual(actual['version'], '1.463.0')
        self.assertEqual(actual['qualifiers'], 'param1=one,param2=two')
        self.assertEqual(actual['subpath'], '/src/main/sub-path')

    def test_ruby_gem_purl_to_dict_no_name_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:gem@1.463.0?param1=one,param2=two#/src/main/sub-path'
        actual = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(actual, {})

    def test_ruby_gem_purl_to_dict_no_type_wrong_url_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:/aws-partitions@1.463.0?param1=one,param2=two#/src/main/sub-path'
        actual = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(actual, {})

    def test_ruby_gem_purl_to_dict_no_name_wrong_url_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:gem/@1.463.0?param1=one,param2=two#/src/main/sub-path'
        actual = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(actual, {})

    def test_ruby_gem_durl_to_dict_all_success(self):
        durl = 'https://rubygems.org/downloads/aws-partitions-1.463.0.gem'
        actual = self.purl_obj.durl_to_dict(durl, '1.463.0', 'param1=one,param2=two', '/src/main/sub-path')
        self.assertEqual(actual['scheme'], 'pkg')
        self.assertEqual(actual['type'], 'gem')
        self.assertEqual(actual['namespace'], '')
        self.assertEqual(actual['name'], 'aws-partitions')
        self.assertEqual(actual['version'], '1.463.0')
        self.assertEqual(actual['qualifiers'], 'param1=one,param2=two')
        self.assertEqual(actual['subpath'], '/src/main/sub-path')

    def test_ruby_gem_durl_to_dict_version_qualifier_success(self):
        durl = 'https://rubygems.org/downloads/aws-partitions-1.463.0.gem'
        actual = self.purl_obj.durl_to_dict(durl, '1.463.0', 'param1=one,param2=two')
        self.assertEqual(actual['scheme'], 'pkg')
        self.assertEqual(actual['type'], 'gem')
        self.assertEqual(actual['namespace'], '')
        self.assertEqual(actual['name'], 'aws-partitions')
        self.assertEqual(actual['version'], '1.463.0')
        self.assertEqual(actual['qualifiers'], 'param1=one,param2=two')

    def test_ruby_gem_durl_to_dict_version_success(self):
        durl = 'https://rubygems.org/downloads/aws-partitions-1.463.0.gem'
        actual = self.purl_obj.durl_to_dict(durl, '1.463.0')
        self.assertEqual(actual['scheme'], 'pkg')
        self.assertEqual(actual['type'], 'gem')
        self.assertEqual(actual['namespace'], '')
        self.assertEqual(actual['name'], 'aws-partitions')
        self.assertEqual(actual['version'], '1.463.0')

    def test_ruby_gem_durl_to_dict_main_success(self):
        durl = 'https://rubygems.org/downloads/aws-partitions-1.463.0.gem'
        actual = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(actual['scheme'], 'pkg')
        self.assertEqual(actual['type'], 'gem')
        self.assertEqual(actual['namespace'], '')
        self.assertEqual(actual['name'], 'aws-partitions')

    def test_ruby_gem_durl_to_dict_main_wrong_http_fail(self):
        durl = 'https:rubygems.org/downloads/aws-partitions-1.463.0.gem'
        actual = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(actual, {})

    def test_ruby_gem_durl_to_dict_main_wrong_type_fail(self):
        durl = 'https://rubygems/downloads/aws-partitions-1.463.0.gem'
        actual = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(actual, {})

    def test_ruby_gem_durl_to_dict_main_wrong_namespace_fail(self):
        durl = 'https://rubygems.org//aws-partitions-1.463.0.gem'
        actual = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(actual, {})

    def test_ruby_gem_durl_to_dict_main_wrong_name_fail(self):
        durl = 'https://rubygems.org/downloads/1.463.0.gem'
        actual = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(actual, {})

    def test_ruby_gem_durl_to_purl_all_success(self):
        durl = 'https://rubygems.org/downloads/aws-partitions-1.463.0.gem'
        actual = self.purl_obj.durl_to_purl(durl, '1.463.0', 'param1=one,param2=two', '/src/main/sub-path')
        expect = 'pkg:gem/aws-partitions@1.463.0?param1=one,param2=two#/src/main/sub-path'
        self.assertEqual(expect, actual)

    def test_ruby_gem_durl_to_purl_version_qualifier_success(self):
        durl = 'https://rubygems.org/downloads/aws-partitions-1.463.0.gem'
        actual = self.purl_obj.durl_to_purl(durl, '1.463.0', 'param1=one,param2=two')
        expect = 'pkg:gem/aws-partitions@1.463.0?param1=one,param2=two'
        self.assertEqual(expect, actual)

    def test_ruby_gem_durl_to_purl_version_success(self):
        durl = 'https://rubygems.org/downloads/aws-partitions-1.463.0.gem'
        actual = self.purl_obj.durl_to_purl(durl, '1.463.0')
        expect = 'pkg:gem/aws-partitions@1.463.0'
        self.assertEqual(expect, actual)

    def test_ruby_gem_durl_to_purl_main_success(self):
        durl = 'https://rubygems.org/downloads/aws-partitions-1.463.0.gem'
        actual = self.purl_obj.durl_to_purl(durl)
        expect = 'pkg:gem/aws-partitions'
        self.assertEqual(expect, actual)

    def test_ruby_gem_params_to_purl_all_success(self):
        actual = self.purl_obj.params_to_purl('gem', '', 'aws-partitions', '1.463.0', 'param1=one,param2=two','/src/main/sub-path')
        expect = 'pkg:gem/aws-partitions@1.463.0?param1=one,param2=two#/src/main/sub-path'
        self.assertEqual(expect, actual)

    def test_ruby_gem_params_to_purl_version_qualifier_success(self):
        actual = self.purl_obj.params_to_purl('gem', '', 'aws-partitions', '1.463.0', 'param1=one,param2=two')
        expect = 'pkg:gem/aws-partitions@1.463.0?param1=one,param2=two'
        self.assertEqual(expect, actual)

    def test_ruby_gem_params_to_purl_version_success(self):
        actual = self.purl_obj.params_to_purl('gem', '', 'aws-partitions', '1.463.0')
        expect = 'pkg:gem/aws-partitions@1.463.0'
        self.assertEqual(expect, actual)

    def test_ruby_gem_params_to_purl_main_success(self):
        actual = self.purl_obj.params_to_purl('gem', '', 'aws-partitions')
        expect = 'pkg:gem/aws-partitions'
        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
