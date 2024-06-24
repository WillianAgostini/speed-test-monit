import ctypes
from sys import platform


class AbstractSystemActivityController:

    def keep_system_active(self):
        pass

    def release_system_activity(self):
        pass


class WindowsSystemActivityController(AbstractSystemActivityController):
    """
    Enables an application to inform the system that it is in use, thereby preventing
    the system from entering sleep or turning off the display while the application is running.
    https://stackoverflow.com/a/65401303/23547983
    https://learn.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-setthreadexecutionstate
    """

    ES_AWAYMODE_REQUIRED = 0x00000040
    ES_CONTINUOUS = 0x80000000
    ES_DISPLAY_REQUIRED = 0x00000002
    ES_SYSTEM_REQUIRED = 0x00000001
    ES_USER_PRESENT = 0x00000004

    def __init__(self):
        self.SetThreadExecutionState = ctypes.windll.kernel32.SetThreadExecutionState

    def keep_system_active(self):
        lastExecutionState = self.SetThreadExecutionState(
            self.ES_SYSTEM_REQUIRED | self.ES_CONTINUOUS | self.ES_DISPLAY_REQUIRED
        )

        if lastExecutionState is None:
            raise Exception("SetThreadExecutionState failed")

    def release_system_activity(self):
        self.SetThreadExecutionState(self.ES_CONTINUOUS)


def create_system_activity_controller() -> AbstractSystemActivityController:
    if platform == "win32":
        return WindowsSystemActivityController()

    return AbstractSystemActivityController()
