from setuptools import setup

setup(name='LivefyreI18n',
      version='1.0.0',
      description='Livefyre i18n configurations for end-user applications.',
      author='Livefyre',
      author_email='support@livefyre.com',
      url='https://github.com/livefyre/livefyre-i18n',
      packages=['nls'],
      package_data={'nls': ['nls/*.json']}
)
