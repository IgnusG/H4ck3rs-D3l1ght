class Warnings:
    warnings = []
    exceptions = []

    @staticmethod
    def add_warning(warning: Warning):
        Warnings.warnings.append(warning)

    @staticmethod
    def add_exception(exception: Exception):
        Warnings.exceptions.append(exception)

    @staticmethod
    def list_all_exceptions():
        for exception in Warnings.exceptions:
            print('Nothing so far')
