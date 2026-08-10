from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

from .base import ModeloBase
from .coleta_voo import ColetaVoo
from .voo_info import VooInfo

__all__ = ["db", "ModeloBase", "ColetaVoo", "VooInfo"]
