import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Path to Octave executable (usually /usr/bin/octave on Ubuntu)
    OCTAVE_PATH = os.getenv('OCTAVE_PATH', '/usr/bin/octave')
    
    # Server settings
    DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', 5000))
    
    # Optional: Path to your Octave scripts
    OCTAVE_SCRIPTS_PATH = os.path.join(os.getcwd(), 'octave_scripts')