from datetime import datetime as dt
import os
import asyncpgsa
from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String, DateTime
)
from sqlalchemy.sql import select

metadata = MetaData()

urls = Table(
    'urls', metadata,

    Column('id', Integer, primary_key=True),
    Column('url', String(255), nullable=False, unique=True),
)

keywords = Table(
    'keywords', metadata,

    Column('id', Integer, primary_key=True),
    Column('keyword', String(255)),

    Column('url_id',
           Integer,
           ForeignKey('urls.id'))
)


async def init_db(app):
    dsn = construct_db_url()
    pool = await asyncpgsa.create_pool(dsn=dsn)
    app['db_pool'] = pool
    return pool


def construct_db_url():
    DSN = "postgresql://{user}:{password}@{host}:{port}/{database}"
    return DSN.format(
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASS'],
        database=os.environ['DB_NAME'],
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT'],
    )


