import json
from ixnetwork_restpy.files import Files

def test_can_import_export_json_as_string (ixnetwork):
    vports = [
    {
        'xpath': '/vport[1]',
        'name': 'vport 1'
    },
    {
        'xpath': '/vport[2]',
        'name': 'vport 2'
    }
    ]

    ixnetwork.ResourceManager.ImportConfig(json.dumps(vports), True)
    assert(len(ixnetwork.Vport.find()) == 2)

    config = ixnetwork.ResourceManager.ExportConfig(['/descendant-or-self::*'], False, 'json')

    ixnetwork.ResourceManager.ImportConfig(config, True)
    assert(len(ixnetwork.Vport.find()) == 2)


def test_can_import_export_json_as_file (ixnetwork):
    
    ixnetwork.Vport.add().add()
    
    ixnetwork.ResourceManager.ExportConfigFile(['/descendant-or-self::*'], False, 'json', Files('two_vports.json'))

    ixnetwork.ResourceManager.ImportConfigFile(Files('two_vports.json'), True)
    assert(len(ixnetwork.Vport.find()) == 2)