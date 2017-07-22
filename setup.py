from setuptools.command.install import install
from distutils.core import setup

class PostInstallCommand(install):
    def run(self):
        import sveder
        sveder.open_sveder_com()
        install.run(self)


setup(
  name = 'sveder',
  packages = ['sveder'],
  version = '0.1',
  description = 'Visit sveder.com :)',
  author = 'Sveder',
  author_email = 'm@sveder.com',
  url = 'https://github.com/Sveder/import-sveder',
  download_url = 'https://github.com/Sveder/import-sveder/archive/0.1.tar.gz',
  keywords = ['sveder', 'shameless', 'self', 'promotion'],
)