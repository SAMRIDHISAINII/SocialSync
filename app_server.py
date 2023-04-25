

from time import sleep
from resources.config import settings_core
from resources.server import mm_server


settings = settings_core()
server = mm_server()


########## APPLICATION LOOP
#####
while True:

    ## Process Pending Posts
    server.process_pending_scheduled_posts()

    ## Sleep for the specified amount of time
    sleep(settings.processing_delay_in_seconds)
