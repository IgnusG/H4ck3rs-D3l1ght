class Warnings:
    warnings = []

    @staticmethod
    def add_warning(warning: Warning):
        Warnings.warnings.append(warning)
