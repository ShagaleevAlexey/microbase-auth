from setuptools import setup, find_packages

setup(
    name='microbase-auth',
    version='0.1.0',
    packages=find_packages(),
    url='https://github.com/ShagaleevAlexey/microbase-auth',
    license='',
    author='Alexey Shagaleev',
    author_email='alexey.shagaleev@yandex.ru',
    description='This is auth manager for microservices',
    install_requires=[
        'PyJWT==1.6.4'
    ]
)
