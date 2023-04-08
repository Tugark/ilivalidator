from typing import Optional, TypeVar, Generic

T = TypeVar('T')


class AbstractSetting(dict, Generic[T]):
    """
    An AbstractSetting subclasses the dict class and consists of a simple key-value pair; the key is mapped to
    the IliValidator setting names and the value specifies the configuration.

    If initialized empty, the setting is initialized as empty dict.
    """
    ilivalidator_setting: str

    def __init__(self, param: Optional[T] = None):
        setting = {}
        if param is not None:
            setting[self.ilivalidator_setting] = param
        dict.__init__(self, **setting)


class LogFile(AbstractSetting[str]):
    ilivalidator_setting = 'org.interlis2.validator.log'


class LogFileTimestamp(AbstractSetting[bool]):
    ilivalidator_setting = 'org.interlis2.validator.log.timestamp'


class XtfLog(AbstractSetting[str]):
    ilivalidator_setting = 'org.interlis2.validator.xtflog'


class AllObjectsAccessible(AbstractSetting[bool]):
    ilivalidator_setting = 'org.interlis2.validator.allobjectsaccessible'
