from charms.docker import Docker
from charms.docker.compose import Compose

from charms.reactive import set_state
from charms.reactive import when
from charms.reactive import when_not

from charmhelpers.core.hookenv import config
from charmhelpers.core.hookenv import status_set
from charmhelpers.core.templating import render

@when('docker.available')
def start_redmine():
    ''' Starts a Redmine application in standalone configuration'''

    # Render the formation
    cfg = config()
    render('docker-compose.yml', 'files/redmine/docker-compose.yml', cfg)

    # Initialize the docker compose object, looking @ our work directory
    compose = Compose('files/redmine')

    # Launch the service(s)
    status_set('maintenance', "Fetching / Starting the redmine containers")
    compose.up()
    status_set('active', 'Redmine is running on port 10030')
