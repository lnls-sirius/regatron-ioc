#!/usr/bin/python3
# -*- coding: utf-8 -*-
import logging
import os
import socket
import argparse

logger = logging.getLogger()

class Comm():
    def __init__(self, unix_socket_path, *args, **kwargs):
        self.unix_socket_path = unix_socket_path
        self.connection = None
        self.welcome_socket = None

    def serve(self):
        try:
            if os.path.exists(self.unix_socket_path):
                logger.warning('Unix socket {} already exist'.format(self.unix_socket_path))
                os.unlink(self.unix_socket_path)

            if self.welcome_socket != None:
                logger.warning('Welcome socket already istantiated')

            self.welcome_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
            self.welcome_socket.bind(self.unix_socket_path)
            logger.info('Unix socket created at {}'.format(self.unix_socket_path))
            self.welcome_socket.listen(1)

            while True:
                logger.info('Unix welcome socket listening')
                connection, client_address = self.welcome_socket.accept()
                logger.info('Client {} connected'.format(client_address))

                connection.settimeout(30)

                self.handle_connection(connection)
        except:
            logger.exception('Comm exception')
        finally:
            self.welcome_socket.close()
            os.remove(self.unix_socket_path)
            logger.info('Comm server shutdown')
            self.welcome_socket = None

    def handle_connection(self, connection):
        try:
            while True:
                command = connection.recv(1024)
                response = 'ok'
                connection.sendall('{}\r\n'.format(response).encode('utf-8'))
                logger.debug('{} {}'.format(command, len(command)))
        except:
            logger.exception('Connection exception')
        finally:
            logger.warning('Connection closed')
            connection.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='TopCon debug',
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--unix-socket-path', dest='unix_socket_path', help='UNIX socket address.', default='./unix-socket')
    parser.add_argument('--debug', action='store_true')
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO, format='%(asctime)-15s [%(levelname)s] %(message)s',
        datefmt='%d/%m/%Y %H:%M:%S')
    logger = logging.getLogger()

    comm = Comm(args.unix_socket_path)
    comm.serve()

