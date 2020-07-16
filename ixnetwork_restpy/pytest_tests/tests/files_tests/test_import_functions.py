import os
from ixnetwork_restpy.files import Files


def test_can_save_ixncfg_config_from_sessions(ixnetwork,tmpdir):
    ixnetwork.Vport.add().add().add().add()
    session = ixnetwork._parent
    # saves the config on server
    ixnetwork.SaveConfig(Files('sample.ixncfg'))

    # download the remote saved configuration as some other local file
    session.DownloadFile('sample.ixncfg', tmpdir.join('local.ixncfg').strpath)
    # checking if file exist
    assert tmpdir.join('local.ixncfg').check(file=1)

def test_can_upload_ixncfg_config_to_session(ixnetwork):
    session = ixnetwork._parent
    file_name = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'local.ixncfg')
    session.UploadFile(file_name)
    ixnetwork.NewConfig()
    ixnetwork.LoadConfig(Files('local.ixncfg', local_file=False))

    # checking if the file has been uploaded, this needs to be tested locally
    # assert any(file_name == files.get('name') for files in session.GetFileList().get('files'))

    # verify the config that has been loaded has 4 ports
    assert len(ixnetwork.Vport.find()) == 4