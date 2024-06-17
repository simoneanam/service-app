from appinit import *
import logging
import importlib
import sys
import pathlib

logger = logging.getLogger(__name__)

sys.path.append(pathlib.Path(__file__).parent.resolve())
_settings = get_settings()
logger.info(f" install APP: {_settings.module_name}")
for name_app in _settings.depends:
    try:
        logger.info(f"import app: {name_app}")
        sys.path.append(name_app)
        importlib.import_module(name_app)
    except ImportError as e:
        logger.error(f"Error import app: {name_app} msg: {e} ", exc_info=True)
