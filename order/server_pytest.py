import pytest
import scrape as scrape
from pytest_localserver.http import WSGIServer

def simple_app(environ, start_response):
    """Simplest possible WSGI application"""
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello world!\n']

@pytest.fixture
def testserver(request):
    """Defines the testserver funcarg"""
    server = WSGIServer(application=simple_app)
    server.start()
    request.addfinalizer(server.stop)
    return server

def test_retrieve_some_content(testserver):
    assert scrape(testserver.url) == 'Hello world!\n'