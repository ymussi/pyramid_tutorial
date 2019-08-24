from setuptools import setup, find_packages

setup(
    name='pyramid_tutorial',
    version_format="{tag}.dev{commitcount}",
    setup_requires=["setuptools-git-version"],
    packages = find_packages(),
    description='',
    author='Yuri Mussi',
    author_email='ymussi@gmail.com',
    license='BSD',
    url='',
    keywords = "Mussi",
    install_requires = ['pyramid',
                        'waitress',
                        'requires'],
    zip_safe=False
    ),