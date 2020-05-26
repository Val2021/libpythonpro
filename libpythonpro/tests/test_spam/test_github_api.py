from libpythonpro import github_api


def test_buscar_avatar():
    url = github_api.buscar_avatar('renzo')
    assert 'https://avatars3.githubusercontent.com/u/402714?v=4' == url
