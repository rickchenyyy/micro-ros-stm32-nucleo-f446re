from setuptools import find_packages, setup

package_name = 'ak60_commu_test'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ldsc',
    maintainer_email='nthuldsc@gmail.com',
    description='Example of using AK60 with microros through AK_60_publisher/AK_60_subscriber',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # 'command_publisher = ak60_commu_test.publisher:main',
            # 'feedback_subscriber = ak60_commu_test.subscriber:main',
            'pub_sub = ak60_commu_test.pub_sub:main'
        ],
    },
)
