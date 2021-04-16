

import connexion

from swagger_server import encoder


app = connexion.App(__name__, specification_dir='./swagger/')
app.app.json_encoder = encoder.JSONEncoder
app.add_api('swagger.yaml', arguments={'title': 'Swagger Petstore'}, pythonic_params=True)
app.secret_key = '\xa2*\x0c\xf8\xf5\x0c\x14\x0b\x02o\x01j\x01\xb4%.*3\x97\xfb\xc6\xcf\xf6\xc4\xf9\x8a\xda\tM\xfd\xfd@'
