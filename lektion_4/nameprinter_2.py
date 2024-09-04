class NamePrinter:
    def print_name(self):
        print(f'The module name is {__name__}.')

if __name__ == '__main__':
    np = NamePrinter()
    np.print_name()
