from cloudify import exceptions, ctx
from cloudify.decorators import operation
from package_installer_plugin.utils import run

__author__ = 'kemi'


@operation
def set_url(**_):
    try:
        # ctx.source.instance.runtime_properties['mongo_ip_address'] = ctx.target.instance.runtime_properties.host_ip
        # ctx.source.instance.runtime_properties['mongo_ip_port'] = ctx.target.instance.runtime_properties.host_port

        run(
            'ctx source instance runtime_properties mongo_ip_address $(ctx target instance host_ip)'
        )
        run(
            'ctx source instance runtime_properties mongo_ip_port $(ctx target instance host_port)'
        )
    except Exception as e:
        raise exceptions.RecoverableError('Failed to set mongo ip & port')