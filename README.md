# MongoDB Plugin for Cloudify 3

A basic MongoDB plugin for Cloudify 3+ that enables the installation, start & termination of a MongoDB instance. The plugin also provides relationship implementations that can configure the deployed instance to work with a service / application node.

The implementation extends the [Package Installer Plugin](https://github.com/kemiz/cloudify-package-installer-plugin) for the basic lifecycle operations and provides operation implementations for the relationships and installation of MongoDB-specific Diamond collectors ('pymongo').

## Usage

```yaml
...
  host:
    type: cloudify.nodes.libcloud.Compute
    ...

  ##################################################################################
  # Tomcat server
  ##################################################################################

  tomcat_server:
    type: cloudify.nodes.TomcatServer
    relationships:
      - type: cloudify.relationships.contained_in
        target: host

  ##################################################################################
  # MongoDB node as a backend data-store for the example Tomcat application
  ##################################################################################

  mongodb:
    type: cloudify.nodes.MongoDB
    relationships:
      - type: cloudify.relationships.contained_in
        target: host
...
```

## Example Blueprints

- [Tomcat WebApp and MongoDB](https://github.com/kemiz/tomcat-plugin-cfy3)

## Advanced Configuration

Currently the MongoDB binaries are obtained from the official repository therefore we need to add the server certificate and add the MongoDB repo to our sources. You can change this to point to a URL that the package can be downloaded and the Package Installer Plugin will handle the installation. for more on the [Package Installer Plugin](https://github.com/kemiz/cloudify-package-installer-plugin) see [here](https://github.com/kemiz/cloudify-package-installer-plugin). You can also configure the port directly or provide an external configuration file to be used on startup of the service

```yaml
  ##################################################################################
  # MongoDB Type
  # MongoDB type that can be used to install and control an MongoDB node.
  # The implementation uses: "sudo service <service_name> start / stop / restart"
  # to control the service operation
  ##################################################################################

  cloudify.nodes.MongoDB:
    derived_from: cloudify.nodes.ServiceInstaller
    properties:
      service_name:
        default: 'mongod'
      version:
        default: '3.0'
      mongo_config:
        default:
          external_config_file:
          port: 27017
      config:
        default:
          package_list:
            - 'mongodb-org'
          custom_repo:
            name: 'mongodb-org-3.0'
            yum:
              name: 'mongodb-org-3.0'
              entry: '[mongodb-org-3.0]
                      name=MongoDB Repository
                      baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.0/x86_64/
                      gpgcheck=0
                      enabled=1'
            apt:
              key_server: 'hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10'
              entry: 'deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0 multiverse'
```
