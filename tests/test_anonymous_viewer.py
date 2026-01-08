from src.core.anonymous_viewer import AnonymousStoryViewer

class FakeLookup:
    def profile_url(self, username: str) -> str:
        return "https://www.instagram.com/example/"

class FakeOnline:
    def view_url(self, url: str, options=None) -> str:
        return url

def test_view_profile_anonymously_returns_url():
    v = AnonymousStoryViewer(lookup=FakeLookup(), online=FakeOnline())
    url = v.view_profile_anonymously("example")
    assert url.endswith("/example/")
