import pytest
import os
from ixnetwork_restpy.files import Files


def test_can_save_ixncfg_config_from_sessions(config_assistant, tmpdir):
    config_assistant.config.Vport.add().add().add().add()
    config_assistant.commit()
    session = config_assistant.config._parent
    config_assistant.config.SaveConfig(Files('sample.ixncfg'))
    config_assistant.commit()
    session.DownloadFile('sample.ixncfg', tmpdir.join('local.ixncfg').strpath)

    assert tmpdir.join('local.ixncfg').check(file=1)


def test_can_upload_ixncfg_config_to_session(config_assistant):
    session = config_assistant.config._parent
    file_name = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             'local.ixncfg')
    session.UploadFile(file_name)
    config_assistant.commit()
    config_assistant.config.NewConfig()
    config_assistant.commit()
    config_assistant.config.LoadConfig(Files('local.ixncfg', local_file=False))
    config_assistant.commit()
    assert len(config_assistant.config.Vport.find()) == 4


def test_upload_filename_with_special_chars(config_assistant):
    config =  config_assistant.config
    session = config_assistant.config._parent
    file_name = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                             'local.ixncfg')
    with open(file_name, 'rb') as fp:
        contents = fp.read()
    special_file_name = 'local+-)_(.ixncfg' 
    with open(special_file_name, 'wb') as fp:
        fp.write(contents)
    config_assistant.commit()
    config.LoadConfig(Files(special_file_name, local_file=True))
    config_assistant.commit()
    assert (file_exists(config, special_file_name) is True)
    session.RemoveFile(special_file_name)
    config_assistant.commit()
    assert (file_exists(config, special_file_name) is False)
    session.UploadFile(special_file_name)
    config_assistant.commit()
    assert (file_exists(config, special_file_name) is True)


def file_exists(ixnetwork, remote_filename):
    session = ixnetwork._parent
    for item in session.GetFileList()['files']:
        if item['name'] == remote_filename:
            return True
    return False



if __name__ == '__main__':
    pytest.main([
        '--server', '10.36.82.185:443:linux', 
        '--server', '10.36.83.80:11009:windows', 
        '-s', 
        __file__
    ])
