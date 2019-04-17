import os
import asyncpgsa
from sqlalchemy import (
    MetaData, Table, Column, ForeignKey,
    Integer, String
)

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
    DSN = "postgresql://{user}:{password}@{host}/{database}"
    return DSN.format(
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        database=os.environ['DB_NAME'],
        host=os.environ['DB_HOST'],
    )


async def set_url(conn, url):
    url_ent = urls.insert().values(url=url)
    rez = await conn.execute(url_ent)
    t = keywords.insert().values(url_id=rez.inserted_primary_key[0], keyword='aa')
    await conn.execute(t)

async def get_urls(conn):
    records = await conn.fetch(
        urls.select().order_by(urls.c.id)
    )

    return records

async def get_keywords(conn):
    records = await conn.fetch(
        urls.select().order_by(urls.c.id)
    )
    print(records)
    return records