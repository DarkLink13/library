from os import environ as env

config = {
    'host':  env['HOST'],
    'database':  env['NAME'],
    'user': env['USER'],
    'password':  env['PASS'],
    'port':  env['PORT'],
}