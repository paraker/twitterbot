from app.twitterbot import TwitterBot
import pytest


@pytest.fixture
def bot():
    return TwitterBot(None)


def test_twitterbot(bot):
    assert bot.api is None


def test_twitter_auth(bot):
    with pytest.raises(TypeError):
        bot.twitter_auth()


def test_create_api_object(bot):
    bot.create_api_object()
    assert bot.api.wait_on_rate_limit is True
    assert bot.api.wait_on_rate_limit_notify is True


def test_verify_twitter_credentials(bot):
    assert bot.verify_twitter_credentials() == \
        "Error during auth: 'NoneType' object has no attribute 'verify_credentials'"
