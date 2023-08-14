class Customer():
    def __init__(self, first_name, last_name, zip_code):
        self.first_name = first_name
        self.last_name = last_name
        self.zip_code = zip_code

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def info(self):
        return '{} living in {}'.format(self.full_name, self.zip_code)
