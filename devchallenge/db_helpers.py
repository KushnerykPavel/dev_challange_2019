import os
from sqlalchemy import create_engine, MetaData

from keywords.db import construct_db_url
from keywords.db import urls, keywords


def setup_db():
    engine = get_engine()

    db_name = os.environ['DB_NAME']
    db_user = os.environ['DB_USER']
    db_pass = os.environ['DB_PASSWORD']

    with engine.connect() as conn:
        #teardown_db()

        conn.execute("CREATE USER %s WITH PASSWORD '%s'" % (db_user, db_pass))
        conn.execute("CREATE DATABASE %s" % db_name)
        conn.execute("GRANT ALL PRIVILEGES ON DATABASE %s TO %s" %
                     (db_name, db_user))


def teardown_db():
    engine = get_engine()

    db_name = os.environ['DB_NAME']
    db_user = os.environ['DB_USER']

    with engine.connect() as conn:
        # terminate all connections to be able to drop database
        conn.execute("""
          SELECT pg_terminate_backend(pg_stat_activity.pid)
          FROM pg_stat_activity
          WHERE pg_stat_activity.datname = '%s'
            AND pid <> pg_backend_pid();""" % db_name)
        conn.execute("DROP DATABASE IF EXISTS %s" % db_name)
        conn.execute("DROP ROLE IF EXISTS %s" % db_user)


def get_engine():
    db_url = construct_db_url()
    engine = create_engine(db_url, isolation_level='AUTOCOMMIT')
    return engine


def create_tables():
    engine = get_engine()

    meta = MetaData()
    meta.create_all(bind=engine, tables=[urls, keywords])


def drop_tables():
    engine = get_engine()

    meta = MetaData()
    meta.drop_all(bind=engine, tables=[urls, keywords])



if __name__ == '__main__':
    #teardown_db()
    #setup_db()
    create_tables()
