from flask import Flask, jsonify, request
from detector import detector as D

application = Flask(__name__)

@application.route("/", methods=['POST'])
def detect():
    uploaded_image = request.files['image']
    uploaded_image = uploaded_image.read()

    dogs, dog_breed = False, ""

    # Check if there are dogs
    dogs = D.dog_detector(uploaded_image)

    # If we have a dog then we check the breed
    if dogs:
        dog_breed = D.breed_detector(uploaded_image)

    # create dict holding response
    response = {
        'dog_detected': dogs,
        'breed_detected': dog_breed
    }

    return jsonify(response)

if __name__ == "__main__":
    application.run()