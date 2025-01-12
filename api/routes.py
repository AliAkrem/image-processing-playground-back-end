from io import BytesIO
from flask import Blueprint, request, jsonify
import numpy as np
from .octave_engine import OctaveEngineManager
import base64
import logging
from io import BytesIO
from PIL import Image

api = Blueprint('api', __name__)


@api.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"})



@api.route('/add-gaussian-noise', methods=['POST'])
def add_gaussian_noise():
    try:
        # Check if the file part is present
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        # Retrieve the file
        file = request.files['image']
        
        # Ensure the file has a valid extension
        if file.filename.split('.')[-1].lower() not in ['png', 'jpg', 'jpeg', 'tif']:
            return jsonify({"error": "Unsupported file type"}), 400
        
        # Open the image file
        img = Image.open(file)
        
        # Convert to grayscale if not already
        if img.mode != 'L':
            img = img.convert('L')
            
        # Convert to numpy array
        img_array = np.array(img)
        
        # Process with Octave
        eng = OctaveEngineManager.get_engine()
        
        # Process grayscale image
        img_array_list = img_array.tolist()

        noisy_img = np.array(eng.add_gaussian_noise(img_array_list))

        # Ensure the array is in uint8 format
        noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)

        # Convert back to image format
        output = Image.fromarray(noisy_img, mode='L')

        buffered = BytesIO()

        output.save(buffered, format="PNG")

        img_str = base64.b64encode(buffered.getvalue()).decode()

        return jsonify({
            "success": True,
            "processed_image": f"data:image/png;base64,{img_str}"
        })

    except Exception as e:
        print(f"Error details: {str(e)}")  # For debugging
        return jsonify({"error": str(e)}), 500



@api.route('/add-salt-and-pepper-noise', methods=['POST'])
def add_slat_and_pepper_noise():
    try:
        # Check if the file part is present
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        # Retrieve the file
        file = request.files['image']
        
        # Ensure the file has a valid extension
        if file.filename.split('.')[-1].lower() not in ['png', 'jpg', 'jpeg', 'tif']:
            return jsonify({"error": "Unsupported file type"}), 400
        
        # Open the image file
        img = Image.open(file)
        
        # Convert to grayscale if not already
        if img.mode != 'L':
            img = img.convert('L')
            
        # Convert to numpy array
        img_array = np.array(img)
        
        # Process with Octave
        eng = OctaveEngineManager.get_engine()
        
        # Process grayscale image
        img_array_list = img_array.tolist()
        noisy_img = np.array(eng.add_salt_and_peeper_noise(img_array_list))

        # Ensure the array is in uint8 format
        noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)

        # Convert back to image format
        output = Image.fromarray(noisy_img, mode='L')
        buffered = BytesIO()
        output.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        return jsonify({
            "success": True,
            "processed_image": f"data:image/png;base64,{img_str}"
        })

    except Exception as e:
        print(f"Error details: {str(e)}")  # For debugging
        return jsonify({"error": str(e)}), 500



@api.route('/enhance_v1', methods=['POST'])
def enhance_image_v1():
    try:
        # Check if the file part is present
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        a = request.form.get('a', 30,  type=int)
        b = request.form.get('b', 200,  type=int)


        # Retrieve the file
        file = request.files['image']
        
        # Ensure the file has a valid extension
        if file.filename.split('.')[-1].lower() not in ['png', 'jpg', 'jpeg', 'tif']:
            return jsonify({"error": "Unsupported file type"}), 400
        
        # Open the image file
        img = Image.open(file)
        
        # Convert to grayscale if not already
        if img.mode != 'L':
            img = img.convert('L')
            
        # Convert to numpy array
        img_array = np.array(img)
        
        # Process with Octave
        eng = OctaveEngineManager.get_engine()
        
        # Process grayscale image
        img_array_list = img_array.tolist()
        noisy_img = np.array(eng.enhance_contrast_1(img_array_list, a, b))

        # Ensure the array is in uint8 format
        noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)

        # Convert back to image format
        output = Image.fromarray(noisy_img, mode='L')
        buffered = BytesIO()
        output.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()


        print()
        return jsonify({
            "success": True,
            
            "processed_image": f"data:image/png;base64,{img_str}"
        })

    except Exception as e:
        print(f"Error details: {str(e)}")  # For debugging
        return jsonify({"error": str(e)}), 500




@api.route('/enhance_v2', methods=['POST'])
def enhance_image_v2():
    try:
        # Check if the file part is present
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        a = request.form.get('a', 80,  type=int)
        b = request.form.get('b', 200,  type=int)


        # Retrieve the file
        file = request.files['image']
        
        # Ensure the file has a valid extension
        if file.filename.split('.')[-1].lower() not in ['png', 'jpg', 'jpeg', 'tif']:
            return jsonify({"error": "Unsupported file type"}), 400
        
        # Open the image file
        img = Image.open(file)
        
        # Convert to grayscale if not already
        if img.mode != 'L':
            img = img.convert('L')
            
        # Convert to numpy array
        img_array = np.array(img)
        
        # Process with Octave
        eng = OctaveEngineManager.get_engine()
        
        # Process grayscale image
        img_array_list = img_array.tolist()
        noisy_img = np.array(eng.enhance_contrast_2(img_array_list, a, b))

        # Ensure the array is in uint8 format
        noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)

        # Convert back to image format
        output = Image.fromarray(noisy_img, mode='L')
        buffered = BytesIO()
        output.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()


        print()
        return jsonify({
            "success": True,
            
            "processed_image": f"data:image/png;base64,{img_str}"
        })

    except Exception as e:
        print(f"Error details: {str(e)}")  # For debugging
        return jsonify({"error": str(e)}), 500



@api.route('/gaussian_filter', methods=['POST'])
def gaussian_filter():
    try:
        # Check if the file part is present
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        sigma  = request.form.get('sigma', 0.8,  type=float)
        filter_size = request.form.get('filter_size', 3,  type=int)

        logging.info(f"sigma : {sigma}, filter_size :  {filter_size}")
        

        # Retrieve the file
        file = request.files['image']
        
        # Ensure the file has a valid extension
        if file.filename.split('.')[-1].lower() not in ['png', 'jpg', 'jpeg', 'tif']:
            return jsonify({"error": "Unsupported file type"}), 400
        
        # Open the image file
        img = Image.open(file)
        
        # Convert to grayscale if not already
        if img.mode != 'L':
            img = img.convert('L')
            
        # Convert to numpy array
        img_array = np.array(img)
        
        # Process with Octave
        eng = OctaveEngineManager.get_engine()
        
        # Process grayscale image
        img_array_list = img_array.tolist()
        noisy_img = np.array(eng.gaussian_filter(img_array_list, sigma, filter_size))

        # Ensure the array is in uint8 format
        noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)

        # Convert back to image format
        output = Image.fromarray(noisy_img, mode='L')
        buffered = BytesIO()
        output.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()


        print()
        return jsonify({
            "success": True,
            "processed_image": f"data:image/png;base64,{img_str}"
        })

    except Exception as e:
        print(f"Error details: {str(e)}")  # For debugging
        return jsonify({"error": str(e)}), 500



@api.route('/average_filter', methods=['POST'])
def average_filter():
    try:
        # Check if the file part is present
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        # Retrieve the file
        file = request.files['image']
        
        # Ensure the file has a valid extension
        if file.filename.split('.')[-1].lower() not in ['png', 'jpg', 'jpeg', 'tif']:
            return jsonify({"error": "Unsupported file type"}), 400
        
        # Open the image file
        img = Image.open(file)
        
        # Convert to grayscale if not already
        if img.mode != 'L':
            img = img.convert('L')
            
        # Convert to numpy array
        img_array = np.array(img)
        
        # Process with Octave
        eng = OctaveEngineManager.get_engine()
        
        # Process grayscale image
        img_array_list = img_array.tolist()
        noisy_img = np.array(eng.moyen_filter(img_array_list))

        # Ensure the array is in uint8 format
        noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)

        # Convert back to image format
        output = Image.fromarray(noisy_img, mode='L')
        buffered = BytesIO()
        output.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()


        print()
        return jsonify({
            "success": True,
            "processed_image": f"data:image/png;base64,{img_str}"
        })

    except Exception as e:
        print(f"Error details: {str(e)}")  # For debugging
        return jsonify({"error": str(e)}), 500



@api.route('/median_filter', methods=['POST'])
def median_filter():
    try:
        # Check if the file part is present
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        # Retrieve the file
        file = request.files['image']
        
        # Ensure the file has a valid extension
        if file.filename.split('.')[-1].lower() not in ['png', 'jpg', 'jpeg', 'tif']:
            return jsonify({"error": "Unsupported file type"}), 400
        
        # Open the image file
        img = Image.open(file)
        
        # Convert to grayscale if not already
        if img.mode != 'L':
            img = img.convert('L')
            
        # Convert to numpy array
        img_array = np.array(img)
        
        # Process with Octave
        eng = OctaveEngineManager.get_engine()
        
        # Process grayscale image
        img_array_list = img_array.tolist()
        noisy_img = np.array(eng.midian_filter(img_array_list))

        # Ensure the array is in uint8 format
        noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)

        # Convert back to image format
        output = Image.fromarray(noisy_img, mode='L')
        buffered = BytesIO()
        output.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()


        print()
        return jsonify({
            "success": True,
            "processed_image": f"data:image/png;base64,{img_str}"
        })

    except Exception as e:
        print(f"Error details: {str(e)}")  # For debugging
        return jsonify({"error": str(e)}), 500


@api.route('/max_filter', methods=['POST'])
def max_filter():
    try:
        # Check if the file part is present
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        # Retrieve the file
        file = request.files['image']
        
        # Ensure the file has a valid extension
        if file.filename.split('.')[-1].lower() not in ['png', 'jpg', 'jpeg', 'tif']:
            return jsonify({"error": "Unsupported file type"}), 400
        
        # Open the image file
        img = Image.open(file)
        
        # Convert to grayscale if not already
        if img.mode != 'L':
            img = img.convert('L')
            
        # Convert to numpy array
        img_array = np.array(img)
        
        # Process with Octave
        eng = OctaveEngineManager.get_engine()
        
        # Process grayscale image
        img_array_list = img_array.tolist()
        noisy_img = np.array(eng.max_filter(img_array_list))

        # Ensure the array is in uint8 format
        noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)

        # Convert back to image format
        output = Image.fromarray(noisy_img, mode='L')
        buffered = BytesIO()
        output.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()


        print()
        return jsonify({
            "success": True,
            "processed_image": f"data:image/png;base64,{img_str}"
        })

    except Exception as e:
        print(f"Error details: {str(e)}")  # For debugging
        return jsonify({"error": str(e)}), 500



@api.route('/min_filter', methods=['POST'])
def min_filter():
    try:
        # Check if the file part is present
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        # Retrieve the file
        file = request.files['image']
        
        # Ensure the file has a valid extension
        if file.filename.split('.')[-1].lower() not in ['png', 'jpg', 'jpeg', 'tif']:
            return jsonify({"error": "Unsupported file type"}), 400
        
        # Open the image file
        img = Image.open(file)
        
        # Convert to grayscale if not already
        if img.mode != 'L':
            img = img.convert('L')
            
        # Convert to numpy array
        img_array = np.array(img)
        
        # Process with Octave
        eng = OctaveEngineManager.get_engine()
        
        # Process grayscale image
        img_array_list = img_array.tolist()
        noisy_img = np.array(eng.min_filter(img_array_list))

        # Ensure the array is in uint8 format
        noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)

        # Convert back to image format
        output = Image.fromarray(noisy_img, mode='L')
        buffered = BytesIO()
        output.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()


        print()
        return jsonify({
            "success": True,
            "processed_image": f"data:image/png;base64,{img_str}"
        })

    except Exception as e:
        print(f"Error details: {str(e)}")  # For debugging
        return jsonify({"error": str(e)}), 500


@api.route('/nagao_filter', methods=['POST'])
def nagao_filter():
    try:
        # Check if the file part is present
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        # Retrieve the file
        file = request.files['image']
        
        # Ensure the file has a valid extension
        if file.filename.split('.')[-1].lower() not in ['png', 'jpg', 'jpeg', 'tif']:
            return jsonify({"error": "Unsupported file type"}), 400
        
        # Open the image file
        img = Image.open(file)
        
        # Convert to grayscale if not already
        if img.mode != 'L':
            img = img.convert('L')
            
        # Convert to numpy array
        img_array = np.array(img)
        
        # Process with Octave
        eng = OctaveEngineManager.get_engine()
        
        # Process grayscale image
        img_array_list = img_array.tolist()
        noisy_img = np.array(eng.nagao_filter(img_array_list))

        # Ensure the array is in uint8 format
        noisy_img = np.clip(noisy_img, 0, 255).astype(np.uint8)

        # Convert back to image format
        output = Image.fromarray(noisy_img, mode='L')
        buffered = BytesIO()
        output.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()


        print()
        return jsonify({
            "success": True,
            "processed_image": f"data:image/png;base64,{img_str}"
        })

    except Exception as e:
        print(f"Error details: {str(e)}")  # For debugging
        return jsonify({"error": str(e)}), 500


@api.route('/prewitt_edge_detection', methods=['POST'])
def prewitt_edge_detection():
    try:
        # Check if the file part is present
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        # Retrieve the file
        file = request.files['image']
        
        # Ensure the file has a valid extension
        if file.filename.split('.')[-1].lower() not in ['png', 'jpg', 'jpeg', 'tif']:
            return jsonify({"error": "Unsupported file type"}), 400
        
        # Open the image file
        img = Image.open(file)
        
        # Convert to grayscale if not already
        if img.mode != 'L':
            img = img.convert('L')
            
        # Convert to numpy array
        img_array = np.array(img)
        
        # Process with Octave
        eng = OctaveEngineManager.get_engine()
        
        # Process grayscale image
        img_array_list = img_array.tolist()
        processed_img = np.array(eng.prewitt_edge_detection(img_array_list))

        # Convert to uint8 format (values should already be in 0-255 range)
        processed_img = processed_img.astype(np.uint8)

        # Convert back to image format
        output = Image.fromarray(processed_img, mode='L')
        buffered = BytesIO()
        output.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        return jsonify({
            "success": True,
            "processed_image": f"data:image/png;base64,{img_str}"
        })

    except Exception as e:
        print(f"Error details: {str(e)}")  # For debugging
        return jsonify({"error": str(e)}), 500
    


@api.route('/laplacian_edge_detection', methods=['POST'])
def laplacian_edge_detection():
    try:
        # Check if the file part is present
        if 'image' not in request.files:
            return jsonify({"error": "No image file provided"}), 400

        
        s = request.form.get('s', 20,  type=int)

        # Retrieve the file
        file = request.files['image']
        
        # Ensure the file has a valid extension
        if file.filename.split('.')[-1].lower() not in ['png', 'jpg', 'jpeg', 'tif']:
            return jsonify({"error": "Unsupported file type"}), 400
        



        # Open the image file
        img = Image.open(file)
        
        # Convert to grayscale if not already
        if img.mode != 'L':
            img = img.convert('L')
            

        # Convert to numpy array
        img_array = np.array(img)
        
        # Process with Octave
        eng = OctaveEngineManager.get_engine()
        
        # Process grayscale image
        img_array_list = img_array.tolist()
        processed_img = np.array(eng.laplacian_edge_detection(img_array_list, s))

        # Convert to uint8 format (values should already be in 0-255 range)
        processed_img = processed_img.astype(np.uint8)

        # Convert back to image format
        output = Image.fromarray(processed_img, mode='L')
        buffered = BytesIO()
        output.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()

        return jsonify({
            "success": True,
            "processed_image": f"data:image/png;base64,{img_str}"
        })

    except Exception as e:
        print(f"Error details: {str(e)}")  # For debugging
        return jsonify({"error": str(e)}), 500

