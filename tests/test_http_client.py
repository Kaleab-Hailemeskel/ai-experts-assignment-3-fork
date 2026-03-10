import time

import requests

from app.http_client import Client
from app.tokens import OAuth2Token, token_from_iso


def test_client_uses_requests_session():
    c = Client()
    assert isinstance(c.session, requests.Session)


def test_token_from_iso_uses_dateutil():
    t = token_from_iso("ok", "2099-01-01T00:00:00Z")
    assert isinstance(t, OAuth2Token)
    assert t.access_token == "ok"
    assert not t.expired


def test_api_request_sets_auth_header_when_token_is_valid():
    c = Client()
    c.oauth2_token = OAuth2Token(access_token="ok", expires_at=int(time.time()) + 3600)

    resp = c.request("GET", "/me", api=True)

    assert resp["headers"].get("Authorization") == "Bearer ok"


def test_api_request_refreshes_when_token_is_missing():
    c = Client()
    c.oauth2_token = None

    resp = c.request("GET", "/me", api=True)

    assert resp["headers"].get("Authorization") == "Bearer fresh-token"


def test_api_request_refreshes_when_token_is_dict():
    c = Client()
    c.oauth2_token = {"access_token": "stale", "expires_at": 0}

    resp = c.request("GET", "/me", api=True)

    assert resp["headers"].get("Authorization") == "Bearer fresh-token"


def test_api_request_refreshes_without_initialization_of_oauth2_token_dict():
    c = Client()
    c.oauth2_token = {}

    resp = c.request("GET", "/me", api=True)

    assert resp["headers"].get("Authorization") == "Bearer fresh-token"

def test_api_request_sets_auth_header_when_token_is_valid_dict():
    c = Client()
    c.oauth2_token = {"access_token": "dict_one", "expires_at": int(time.time()) + 3600}

    resp = c.request("GET", "/me", api=True)

    assert resp["headers"].get("Authorization") == "Bearer dict_one"

def test_other_values_in_dict_token_dont_prevent_refresh():
    c = Client()
    c.oauth2_token = {"access_token": "stale", "expires_at": 0, "other_key": "other_value"}

    resp = c.request("GET", "/me", api=True)

    assert resp["headers"].get("Authorization") == "Bearer fresh-token" 
    assert c.oauth2_token.get("other_key") == "other_value"

def test_other_types_for_token_and_expires_will_prevent_refresh_for_data_integrity():
    c = Client()
    c.oauth2_token = {"access_token": 12345, "expires_at": "not-a-timestamp", "other_key": "other_value"}

    resp = c.request("GET", "/me", api=True)

    assert resp["headers"].get("Authorization") is None
    assert c.oauth2_token["access_token"] == 12345
    assert c.oauth2_token["expires_at"] == "not-a-timestamp"
    assert c.oauth2_token.get("other_key") == "other_value"
    assert isinstance(c.oauth2_token, dict)

def test_empty_Oauth2Token_does_not_prevent_refresh():
    c = Client()
    c.oauth2_token = OAuth2Token(access_token="", expires_at=0)

    resp = c.request("GET", "/me", api=True)

    assert resp["headers"].get("Authorization") == "Bearer fresh-token"

def test_empty_dict_does_not_prevent_refresh():
    c = Client()
    c.oauth2_token = {}

    resp = c.request("GET", "/me", api=True)

    assert resp["headers"].get("Authorization") == "Bearer fresh-token"    
    assert isinstance(c.oauth2_token, dict) 
    assert c.oauth2_token.get("access_token") == "fresh-token" 
    assert c.oauth2_token.get("expires_at") == 10**10