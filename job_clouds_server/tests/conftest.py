import pytest
from job_clouds_server import create_app


@pytest.fixture
def app():
    return create_app()


@pytest.fixture
def gen_image_good():
    return dict({
        'theme': 'neon',
        'channel': 'linkedin',
        'keywords': [
            {
                'text': 'foobar',
                'weight': 1
            }
        ]
    })


@pytest.fixture
def gen_image_invalid_channel():
    return dict({
        'theme': 'neon',
        'channel': 'foobar',
        'keywords': [
            {
                'text': 'foobar',
                'weight': 1
            }
        ]
    })


@pytest.fixture
def gen_image_invalid_theme():
    return dict({
        'theme': 'foobar',
        'channel': 'linkedin',
        'keywords': [
            {
                'text': 'foobar',
                'weight': 1
            }
        ]
    })
