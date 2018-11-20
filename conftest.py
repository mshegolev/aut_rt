# -*- coding: utf-8 -*-
from fixture.application import Application
import pytest

from model.creds import Creds
import rtconfig as cfg
USERNAME=cfg.creds['user']
PASSWORD=cfg.creds['password']
fixture = None


@pytest.fixture(scope="session")
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
        fixture.session.ensure_login(Creds(username=USERNAME, password=PASSWORD))
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(Creds(username=USERNAME, password=PASSWORD))
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture
