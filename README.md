# OC-Port-Registry
A port registry web application for OpenComputers.
[![Build Status](https://travis-ci.org/samis/OC-Port-Registry.svg?branch=master)](https://travis-ci.org/samis/OC-Port-Registry)

# Specification
The object of this application is to provide a central, easily accessible point of reference regarding use of ports by programs.

* It will use a web interface for users to log in (so that it is known who registered a port, not just what for),
* Users would be able to create a Project (to give the registration behind a port meaning, as well as to group multiple registrations if required).
* Users would then be able to register a port for usage, specifying the Project the registration refers to.
* Users would be available to view the complete lists of both ports and projects with all the relevant data.
* The web interface will not be complex, but it will not hide data.

This means it has a small number of requirements
* Requires a login system
    * Auth0 could be used, which would allow easy support of multiple authentication / identification providers.
* Requires a method of storage
    * A database could be used, such as PostgreSQL or MySQL.
* Requires a decent-looking web interface to display and modify the data.
