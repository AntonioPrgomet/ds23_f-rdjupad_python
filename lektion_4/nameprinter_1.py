class NamePrinter:
    def print_name(self):
        print(f'The module name is {__name__}.')

np = NamePrinter()
np.print_name()
