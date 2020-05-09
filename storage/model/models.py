from sqlalchemy import Column, Integer, Date, ForeignKey, LargeBinary, create_engine, String
from sqlalchemy.orm import relationship

from helpers.DbHelpers import DbHelper

"""
pip install sqlalchemy
pip install mysql-connector-python
"""


class Directory(DbHelper().modelBase):
    """
        This class is the orm model that is used as a template in directory table generation
        The table has two one-to-many relationships (one with the files table and one with the directory server itself)
    """
    __tablename__ = 'directory'

    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String(50), index=True)
    creation_date = Column('creationDate', Date)

    parent_directory_id = Column('parent_directory_id', Integer, ForeignKey('directory.id'))

    files = relationship('File', back_populates='directory')
    subdirectories = relationship('Directory', back_populates='parent_directory')
    parent_directory = relationship('Directory', back_populates='subdirectories')


class File(DbHelper().modelBase):
    """
        This class is the orm model that is used as a template in directory table generation
        The table has two many-to-one relationship (with the directory table)
    """
    __tablename__ = 'file'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    content = Column('content', LargeBinary)
    directory_id = Column('directory_id', Integer, ForeignKey('directory.id'))
    directory = relationship('Directory', back_populates='files')


DbHelper().create_database(drop=True, echo=True)
