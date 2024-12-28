from mcdrefoged.api.command import SimpleCommandBuilder, Integer, Text, GreedyText

def on_load(server: PluginServerInterface, pre_module):
    server.logger.info("ProjectMap已加載")