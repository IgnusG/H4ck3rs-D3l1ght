from helpers.error_handling import HackersWarning, HackersException


class Warnings:
    warnings = []
    exceptions = []

    @staticmethod
    def add_warning(warning: HackersWarning):
        for warning_item in Warnings.warnings:
            if warning_item.pointer - 1 == warning:
                return
        Warnings.warnings.append(warning)

    @staticmethod
    def add_exception(exception: HackersException):
        for exception_item in Warnings.exceptions:
            if exception_item.pointer-1 == exception:
                return
        Warnings.exceptions.append(exception)

    @staticmethod
    def list_all_exceptions():
        for exception in Warnings.exceptions:
            print('Nothing so far...')
