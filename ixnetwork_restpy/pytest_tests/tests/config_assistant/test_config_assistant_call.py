import pytest


def test_config_assist_call(config_assistant):
    config = config_assistant.config
    assert(config._xpathObj is not None)
    assert(len(config_assistant.config_json) == 0)
    assert(config._xpathObj._mode == 'config')


def test_empty_commit(config_assistant):
    config = config_assistant.config
    assert(config._xpathObj._mode == 'config')
    errors = config_assistant.commit()
    assert(config._xpathObj._mode == 'normal')
    assert(len(errors) == 0)


if __name__ == '__main__':
    pytest.main(['-s', __file__])
