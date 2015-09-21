# MongoDB Plugin for Cloudify 3

A basic MongoDB plugin for Cloudify 3+ that enables the installation, start & termination of a MongoDB instance. The plugin also provides relationship implementations that can configure the deployed instance to work with a service / application node.

The implementation extends the Package Installer Plugin for the basic lifecycle operations and provides operation implementations for the relationships and installation of MongoDB-specific Diamond collectors ('pymongo').

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

- [https://github.com/kemiz/tomcat-plugin-cfy3](Tomcat WebApp and MongoDB)
