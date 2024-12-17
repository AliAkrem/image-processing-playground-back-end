# Flask API with Octave Runtime Integration

This project implements a Flask REST API that interfaces with Octave/MATLAB through the oct2py Python module.

## Prerequisites

Before setting up the project, ensure you have the following installed on your system:

- Python 3.8 or higher
- GNU Octave 6.0 or higher
- pip (Python package manager)

### Installing GNU Octave

#### Windows
1. Download the Octave installer from [GNU Octave Downloads](https://octave.org/download)
2. Run the installer and follow the installation wizard
3. Add Octave to your system PATH

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install octave
```

#### macOS
```bash
brew install octave
```

## Project Setup

1. Clone the repository
```bash
git clone https://github.com/AliAkrem/image-processing-playground-back-end
cd image-processing-playground-back-end
```

2. Create and activate a virtual environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

3. Install required Python packages
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask development server
```bash
flask run
```

2. The API will be available at `http://localhost:5000`

## API Endpoints

```base
Endpoint                       Methods  Rule                          
-----------------------------  -------  ------------------------------
api.health_check               GET      /api/health             
api.add_gaussian_noise         POST     /api/add-gaussian-noise       
api.add_slat_and_pepper_noise  POST     /api/add-salt-and-pepper-noise
api.average_filter             POST     /api/average_filter           
api.enhance_image_v1           POST     /api/enhance_v1               
api.enhance_image_v2           POST     /api/enhance_v2               
api.gaussian_filter            POST     /api/gaussian_filter                
api.max_filter                 POST     /api/max_filter               
api.median_filter              POST     /api/median_filter            
api.min_filter                 POST     /api/min_filter               
api.nagao_filter               POST     /api/nagao_filter             
api.prewitt_edge_detection     POST     /api/prewitt_edge_detection  
```
## Development

To contribute to this project:

1. Create a new branch for your feature
2. Make your changes
3. Submit a pull request

## License

MIT
