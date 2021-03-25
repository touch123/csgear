
from setuptools import setup

setup(
    name='LogSpider',
    version='1.0',
    packages=['LogSpider'],
    install_requires=[
        'PyYAML==5.4',
        'SQLAlchemy==1.3.7',
    ],
    package_data = {'LogSpider': ["README.md","LogSpider.yml","debug.yml"]},
    entry_points={'console_scripts':[
        'logspider = LogSpider.LogSpider:main',
    ]},
    url='https://github.com/touch123/csgear',
    license='',
    author='Max',
    author_email='0xc00005@gmail.com',
    description=''
)
