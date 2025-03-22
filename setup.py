from setuptools import setup, find_packages
from pathlib import Path

def long_description() -> str:
    long_description: str = ''
    print("Extracting content from README.md...")
    try:
        base_dir: Path = Path(__file__).parent
        filepath: Path = base_dir / 'README.md'
        print("README PATH:", filepath)
        with open(filepath, 'r', encoding='utf-8') as file:
            long_description += file.read()
        print("README.md done.")
    except Exception as e:
        print(f"Failed to read README.md content: {e}")
    print("Extracting content from CHANGELOG.md...")
    try:
        base_dir: Path = Path(__file__).parent
        filepath: Path = base_dir / 'CHANGELOG.md'
        print("CHANGELOG PATH:", filepath)
        with open(filepath, 'r', encoding='utf-8') as file:
            long_description += f'\n\n{file.read()}'
        print("CHANGELOG.md done.")
    except Exception as e:
        print(f"Failed to read CHANGELOG.md content: {e}")
    print("Long description built successfully.")
    return long_description

setup(
    name='quickMethods',
    version='0.0.3',
    description='A simple library to make your life faster with quick methods!',
    long_description=long_description(),
    long_description_content_type='text/markdown',
    author='Orly Neto',
    author_email='orly2carvalhoneto@gmail.com',
    license='MIT License',
    keywords=['useful'],
    packages=find_packages())