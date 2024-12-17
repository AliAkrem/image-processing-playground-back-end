from oct2py import Oct2Py
import logging

class OctaveEngineManager:
    _engine = None

    @classmethod
    def get_engine(cls):
        if cls._engine is None:
            try:
                cls._engine = Oct2Py()
                # Add path to Octave scripts
                cls._engine.addpath('matlab_scripts')
                logging.info("Octave Engine started successfully")
            except Exception as e:
                logging.error(f"Failed to start Octave engine: {str(e)}")
                raise
        return cls._engine

    @classmethod
    def close_engine(cls):
        if cls._engine is not None:
            cls._engine.exit()
            cls._engine = None
            logging.info("Octave Engine closed")