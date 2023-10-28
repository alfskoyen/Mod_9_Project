from setuptools import setup, find_packages

setup(
    name='Mod_9_Project',
    version='1.0.0',
    url='https://github.com/alfskoyen/Mod_9_Project',
    author='Alfred Haugen',
    author_email='author@gmail.com',
    description='Description of my package',
    packages=find_packages(),    
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1'],
)


