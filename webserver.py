from flask import Flask, jsonify, request
import PIL
from io import BytesIO
from detector import detector as D

application = Flask(__name__)

@application.route("/", methods=['POST'])
def detect():
    try:
        uploaded_image = request.files.get('image', False)
        if uploaded_image:
            uploaded_image = uploaded_image.read()
        else:
            return err("No file sent")
    
        try:
            uploaded_image = PIL.Image.open(BytesIO(uploaded_image))
        except IOError:
            return err("File is not an image")

        dogs, dog_breed = False, None

        is_dog = D.dog_detector(uploaded_image)

        if is_dog:
            dog_breed = D.breed_detector(uploaded_image)
    
        response = {'dog_detected': is_dog,'breed_detected': dog_breed}
        return jsonify(response)

    except:
        return err()


def err(message="Unknown Error"):
    return jsonify({"Error": message})


if __name__ == "__main__":
    application.run()