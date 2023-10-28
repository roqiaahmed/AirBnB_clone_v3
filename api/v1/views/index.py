#!/usr/bin/python3xx
'''api status'''
import models
from models import storage
from models.base_model import BaseModel
from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', strict_slashes=False)
def returnstuff():
    '''return stuff'''
    return jsonify(status='OK')


@app_views.route('/stats', methods=['GET'])
def count():
    '''retrieves the number of each objects by type'''
    count_dict = {}
    for cls in classes:
        count_dict[cls] = storage.count(classes[cls])
    return jsonify(count_dict)


# @app_views.route('/stats', strict_slashes=False)
# def stuff():
#     '''JSON Responses'''
#     todos = {'states': State, 'users': User,
#             'amenities': Amenity, 'cities': City,
#             'places': Place, 'reviews': Review}
#     for key in todos:
#         todos[key] = storage.count(todos[key])
#     return jsonify(todos)
