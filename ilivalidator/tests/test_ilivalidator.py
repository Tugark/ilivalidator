from ilivalidator import Ilivalidator, settings as IliValidatorSettings
import os
import tempfile

TEST_DATA_PATH = "ilivalidator/tests/data/"

def test_validate_file_ok():
    valid = Ilivalidator.validate([TEST_DATA_PATH+"OeREBKRM_V2_0_Gesetze.xml"])
    assert valid == True

def test_validate_multiple_files_ok():
    valid = Ilivalidator.validate([TEST_DATA_PATH+"/OeREBKRM_V2_0_Gesetze.xml",TEST_DATA_PATH+"OeREBKRM_V2_0_Themen.xml"])
    assert valid == True

def test_validate_multiple_files_allobjectsaccessible_on_ok():
    settings = IliValidatorSettings.Settings(all_objects_accessible=True)
    valid = Ilivalidator.validate([TEST_DATA_PATH+"OeREBKRM_V2_0_Gesetze.xml",TEST_DATA_PATH+"OeREBKRM_V2_0_Themen.xml"], settings)
    assert valid == True

def test_validate_multiple_files_allobjectsaccessible_on_fail():
    settings = IliValidatorSettings.Settings(all_objects_accessible=True)
    print(f'=> settings: {settings}')
    valid = Ilivalidator.validate([TEST_DATA_PATH+"OeREBKRM_V2_0_Gesetze.xml",TEST_DATA_PATH+"OeREBKRM_V2_0_Themen_missing_REF.xml"], settings)
    assert valid == False

def test_validate_multiple_files_allobjectsaccessible_off_ok():
    settings = IliValidatorSettings.Settings(all_objects_accessible=False)
    valid = Ilivalidator.validate([TEST_DATA_PATH+"OeREBKRM_V2_0_Gesetze.xml",TEST_DATA_PATH+"OeREBKRM_V2_0_Themen_missing_REF.xml"], settings)
    assert valid == True

def test_validate_logfiles_on_ok():
    temp_dir = tempfile.TemporaryDirectory()
    log_file = os.path.join(temp_dir.name, "mylog.log")
    xtf_log_file = log_file + ".xtf"

    settings = IliValidatorSettings.Settings(log_file=log_file, log_file_timestamp=True, xtf_log=xtf_log_file)
    valid = Ilivalidator.validate([TEST_DATA_PATH+"OeREBKRM_V2_0_Gesetze.xml"], settings)
    assert valid == True

    with open(log_file, 'r') as file:
        content = file.read()
        assert -1 != content.find("Info: ...validation done")

    with open(xtf_log_file, 'r') as file:
        content = file.read()
        assert -1 != content.find("<Message>...validation done</Message>")