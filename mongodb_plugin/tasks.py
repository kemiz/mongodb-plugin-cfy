from cloudify import exceptions, ctx
from cloudify.decorators import operation
from package_installer_plugin.utils import run
from package_installer_plugin.tasks import install_packages

__author__ = 'kemi'


@operation
def set_url(**_):
    try:
        # ctx.source.instance.runtime_properties['mongo_ip_address'] = ctx.target.instance.runtime_properties.host_ip
        # ctx.source.instance.runtime_properties['mongo_ip_port'] = ctx.target.instance.runtime_properties.host_port

        run(
            'ctx source instance runtime_properties mongo_ip_address $(ctx target instance runtime_properties ip)'
        )
        run(
            'ctx source instance runtime_properties mongo_ip_port $(ctx target instance runtime_properties port)'
        )
    except Exception as e:
        raise exceptions.RecoverableError('Failed to set mongo ip & port')


@operation
def install_pymongo(**_):
    """ Installs pymongo required for Diamond monitoring """

    config = ['package_list']['pymongo']
    install_packages(config)