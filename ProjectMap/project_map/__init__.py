from mcdrefoged.api.all import *

def on_load(server: PluginServerInterface, pre_module):
    server.logger.info("ProjectMap已加載")