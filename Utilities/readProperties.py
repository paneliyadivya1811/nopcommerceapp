import configparser

config = configparser.ConfigParser()
config.read('Configurations/config.ini')

sections = config.sections()
print(f"Config file has sections: {sections}")

for section in sections:
    options = config.options(section)
    print(f"Section '{section}' has options: {options}")

    for option in options:
        value = config.get(section, option)
        print(f"Option '{option}' has value '{value}'")

class ReadConfig:
    @staticmethod
    def get_base_url():
        url = config.get('common_info', 'baseURL')
        return url

    @staticmethod
    def get_username():
        username = config.get('common_info', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('common_info', 'password')
        return password
