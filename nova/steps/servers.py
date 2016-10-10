from autostepler import puzzle


class ServerSteps(object):

    @puzzle.output.server.create
    def create_server(self, server_name):
        server = {"type": "server", "name": server_name}
        print "Create server", server_name
        return server

    @puzzle.input.server
    @puzzle.output.server.delete
    def delete_server(self, server):
        print "Delete server", server
