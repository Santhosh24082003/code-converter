from flask import Blueprint
from controllers.conversion_controller import convert

# Define a blueprint for the conversion routes
conversion_blueprint = Blueprint('conversion', __name__)

# Define the route for code conversion
@conversion_blueprint.route('/convert', methods=['POST'])
def convert_route():
    return convert()