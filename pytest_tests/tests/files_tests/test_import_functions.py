from ixnetwork_restpy.files import Files

def test_can_save_ixncfg_config_from_sessions(ixnetwork,tmpdir):
    ixnetwork.Vport.add().add().add().add()
    session = ixnetwork._parent
    # saves the config on server
    ixnetwork.SaveConfig('sample.ixncfg')

    # download the remote saved configuration as some other local file
    session.DownloadFile('sample.ixncfg', tmpdir.join('local.ixncfg'))
    # checking if file exist
    assert tmpdir.join('local.ixncfg').check(file=1)

def test_can_upload_ixncfg_config_to_session(ixnetwork):
    session = ixnetwork._parent
    file_name = '.\\ixnetwork_restpy\\pytest_tests\\tests\\files_tests\\local.ixncfg'
    session.UploadFile(file_name)
    file_obj = Files(file_name)
    if file_obj.is_local_file:
        ixnetwork.LoadConfig(file_obj)
    assert file_obj.file_name in file_name.split('\\')

    # checking if the file is correctly uploaded of not
    assert any(file_name == files.get('name') for files in session.GetFileList().get('files'))

    # since the saved config has 4 ports
    assert len(ixnetwork.Vport.find()) == 4

# todo: try with json