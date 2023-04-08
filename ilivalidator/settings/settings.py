from .abstract_settings import *


class Settings(dict):
    """
    Settings class to override IliValidator defaults.
    """
    settings: list[AbstractSetting] = None

    def __init__(
        self,
        all_objects_accessible: Optional[bool] = None,
        log_file: Optional[str] = None,
        log_file_timestamp: Optional[str] = None,
        xtf_log: Optional[str] = None
    ) -> None:
        self.settings = list()
        self.settings.append(AllObjectsAccessible(all_objects_accessible))
        self.settings.append(LogFile(log_file))
        self.settings.append(LogFileTimestamp(log_file_timestamp))
        self.settings.append(XtfLog(xtf_log))

        self.__dict__ = {
            k: v for setting in self.settings for k, v in setting.items()}
