import unittest
from pypurl.purl import Purl


class GitlabPurlTestCase(unittest.TestCase):
    def setUp(self):
        self.purl_obj = Purl()

    def test_gitlab_purl_to_dict_version_success(self):
        purl_with_version = 'pkg:gitlab/gitlab-org/gitlab-foss@v14.1.8'
        r = self.purl_obj.purl_to_dict(purl_with_version)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'gitlab')
        self.assertEqual(r['namespace'], 'gitlab-org')
        self.assertEqual(r['name'], 'gitlab-foss')
        self.assertEqual(r['version'], 'v14.1.8')

    def test_gitlab_purl_to_dict_version_qualifier_success(self):
        purl_with_version_qualifiers = 'pkg:gitlab/gitlab-org/gitlab-foss@v14.1.8?param1=one,param2=two'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'gitlab')
        self.assertEqual(r['namespace'], 'gitlab-org')
        self.assertEqual(r['name'], 'gitlab-foss')
        self.assertEqual(r['version'], 'v14.1.8')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')

    def test_gitlab_purl_to_dict_version_qualifier_path_success(self):
        purl_with_version_qualifiers_subpath = 'pkg:gitlab/gitlab-org/gitlab-foss@v14.1.8?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'gitlab')
        self.assertEqual(r['namespace'], 'gitlab-org')
        self.assertEqual(r['name'], 'gitlab-foss')
        self.assertEqual(r['version'], 'v14.1.8')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')
        self.assertEqual(r['subpath'], '/src/main/sub-path')

    def test_gitlab_purl_to_dict_no_pkg_fail(self):
        purl_with_version_qualifiers_subpath = 'gitlab/gitlab-org/gitlab-foss@v14.1.8?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_gitlab_purl_to_dict_no_type_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:gitlab-org/gitlab-foss@v14.1.8?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_gitlab_purl_to_dict_no_namespace_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:gitlab/gitlab-foss@v14.1.8?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_gitlab_purl_to_dict_no_name_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:gitlab/gitlab-org@v14.1.8?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_gitlab_purl_to_dict_no_type_wrong_url_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:/gitlab-org/gitlab-foss@v14.1.8?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_gitlab_purl_to_dict_no_namespace_wrong_url_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:gitlab//gitlab-foss@v14.1.8?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_gitlab_purl_to_dict_no_name_wrong_url_fail(self):
        purl_with_version_qualifiers_subpath = 'pkg:gitlab/gitlab-org/@v14.1.8?param1=one,param2=two#/src/main/sub-path'
        r = self.purl_obj.purl_to_dict(purl_with_version_qualifiers_subpath)
        self.assertEqual(r, {})

    def test_gitlab_durl_to_dict_all_success(self):
        durl = 'https://gitlab.com/gitlab-org/gitlab-foss/-/archive/v14.1.8/gitlab-foss-v14.1.8.zip'
        r = self.purl_obj.durl_to_dict(durl, 'v14.1.8', 'param1=one,param2=two', '/src/main/sub-path')
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'gitlab')
        self.assertEqual(r['namespace'], 'gitlab-org')
        self.assertEqual(r['name'], 'gitlab-foss')
        self.assertEqual(r['version'], 'v14.1.8')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')
        self.assertEqual(r['subpath'], '/src/main/sub-path')

    def test_gitlab_durl_to_dict_version_qualifier_success(self):
        durl = 'https://gitlab.com/gitlab-org/gitlab-foss/-/archive/v14.1.8/gitlab-foss-v14.1.8.zip'
        r = self.purl_obj.durl_to_dict(durl, 'v14.1.8', 'param1=one,param2=two')
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'gitlab')
        self.assertEqual(r['namespace'], 'gitlab-org')
        self.assertEqual(r['name'], 'gitlab-foss')
        self.assertEqual(r['version'], 'v14.1.8')
        self.assertEqual(r['qualifiers'], 'param1=one,param2=two')

    def test_gitlab_durl_to_dict_version_success(self):
        durl = 'https://gitlab.com/gitlab-org/gitlab-foss/-/archive/v14.1.8/gitlab-foss-v14.1.8.zip'
        r = self.purl_obj.durl_to_dict(durl, 'v14.1.8')
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'gitlab')
        self.assertEqual(r['namespace'], 'gitlab-org')
        self.assertEqual(r['name'], 'gitlab-foss')
        self.assertEqual(r['version'], 'v14.1.8')

    def test_gitlab_durl_to_dict_main_success(self):
        durl = 'https://gitlab.com/gitlab-org/gitlab-foss/-/archive/master/gitlab-foss-master.zip'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r['scheme'], 'pkg')
        self.assertEqual(r['type'], 'gitlab')
        self.assertEqual(r['namespace'], 'gitlab-org')
        self.assertEqual(r['name'], 'gitlab-foss')

    def test_gitlab_durl_to_dict_main_wrong_http_fail(self):
        durl = 'https:gitlab.com/gitlab-org/gitlab-foss/-/archive/master/gitlab-foss-master.zip'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r, {})

    def test_gitlab_durl_to_dict_main_wrong_type_fail(self):
        durl = 'https://gitlab/gitlab-org/gitlab-foss/-/archive/master/gitlab-foss-master.zip'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r, {})

    def test_gitlab_durl_to_dict_main_wrong_namespace_fail(self):
        durl = 'https://gitlab.com//gitlab-foss/-/archive/master/gitlab-foss-master.zip'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r, {})

    def test_gitlab_durl_to_dict_main_wrong_name_fail(self):
        durl = 'https://gitlab.com/gitlab-org//-/archive/master/gitlab-foss-master.zip'
        r = self.purl_obj.durl_to_dict(durl)
        self.assertEqual(r, {})

    def test_gitlab_durl_to_purl_all_success(self):
        durl = 'https://gitlab.com/gitlab-org/gitlab-foss/-/archive/master/gitlab-foss-master.zip'
        r = self.purl_obj.durl_to_purl(durl, '9d8642e1d6b4d6c7de730f531278bc8e69b89b79', 'param1=one,param2=two',
                                       '/src/main/sub-path')
        p = 'pkg:gitlab/gitlab-org/gitlab-foss@9d8642e1d6b4d6c7de730f531278bc8e69b89b79?param1=one,param2=two#/src/main/sub-path'
        self.assertEqual(r, p)

    def test_gitlab_durl_to_purl_version_qualifier_success(self):
        durl = 'https://gitlab.com/gitlab-org/gitlab-foss/-/archive/master/gitlab-foss-master.zip'
        r = self.purl_obj.durl_to_purl(durl, '9d8642e1d6b4d6c7de730f531278bc8e69b89b79', 'param1=one,param2=two')
        p = 'pkg:gitlab/gitlab-org/gitlab-foss@9d8642e1d6b4d6c7de730f531278bc8e69b89b79?param1=one,param2=two'
        self.assertEqual(r, p)

    def test_gitlab_durl_to_purl_version_success(self):
        durl = 'https://gitlab.com/gitlab-org/gitlab-foss/-/archive/master/gitlab-foss-master.zip'
        r = self.purl_obj.durl_to_purl(durl, '9d8642e1d6b4d6c7de730f531278bc8e69b89b79')
        p = 'pkg:gitlab/gitlab-org/gitlab-foss@9d8642e1d6b4d6c7de730f531278bc8e69b89b79'
        self.assertEqual(r, p)

    def test_gitlab_durl_to_purl_main_success(self):
        durl = 'https://gitlab.com/gitlab-org/gitlab-foss/-/archive/master/gitlab-foss-master.zip'
        r = self.purl_obj.durl_to_purl(durl)
        p = 'pkg:gitlab/gitlab-org/gitlab-foss'
        self.assertEqual(r, p)

    def test_gitlab_params_to_purl_all_success(self):
        r = self.purl_obj.params_to_purl('gitlab', 'gitlab-org', 'gitlab-foss',
                                         '9d8642e1d6b4d6c7de730f531278bc8e69b89b79', 'param1=one,param2=two',
                                         '/src/main/sub-path')
        p = 'pkg:gitlab/gitlab-org/gitlab-foss@9d8642e1d6b4d6c7de730f531278bc8e69b89b79?param1=one,param2=two#/src/main/sub-path'
        self.assertEqual(r, p)

    def test_gitlab_params_to_purl_version_qualifier_success(self):
        r = self.purl_obj.params_to_purl('gitlab', 'gitlab-org', 'gitlab-foss',
                                         '9d8642e1d6b4d6c7de730f531278bc8e69b89b79', 'param1=one,param2=two')
        p = 'pkg:gitlab/gitlab-org/gitlab-foss@9d8642e1d6b4d6c7de730f531278bc8e69b89b79?param1=one,param2=two'
        self.assertEqual(r, p)

    def test_gitlab_params_to_purl_version_success(self):
        r = self.purl_obj.params_to_purl('gitlab', 'gitlab-org', 'gitlab-foss',
                                         '9d8642e1d6b4d6c7de730f531278bc8e69b89b79')
        p = 'pkg:gitlab/gitlab-org/gitlab-foss@9d8642e1d6b4d6c7de730f531278bc8e69b89b79'
        self.assertEqual(r, p)

    def test_gitlab_params_to_purl_main_success(self):
        r = self.purl_obj.params_to_purl('gitlab', 'gitlab-org', 'gitlab-foss')
        p = 'pkg:gitlab/gitlab-org/gitlab-foss'
        self.assertEqual(r, p)


if __name__ == '__main__':
    unittest.main()
