class Customer():
    def __init__(self, first_name, last_name, zip_code):

        if not isinstance(first_name, str) or not first_name.strip():
            raise ValueError("First name should be a non-empty string.")
        if not isinstance(last_name, str) or not last_name.strip():
            raise ValueError("Last name should be a non-empty string.")
        if not isinstance(zip_code, int):
            raise ValueError("Zip code should be an integer.")

        self.first_name = first_name
        self.last_name = last_name
        self.zip_code = zip_code

    @property
    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    @property
    def info(self):
        return '{} living in {}'.format(self.full_name, self.zip_code)
