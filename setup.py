from setuptools import setup, find_packages


setup(
    name='presso',
    version='1.0.0',
    description='Event-driven backtest/realtime quantitative trading system.',
    packages=find_packages(exclude=('*.test',
                                    '*.test.*',
                                    'test.*',
                                    'test',
                                    'docs')),
    entry_points={
        'console_scripts': [
            'presso = presso.cli.presso:main',
        ]
    },
    python_requires='>=3.6',
    install_requires=['aiohttp',
                      'numpy',
                      'toml']
)
