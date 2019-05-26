from abc import ABC

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class SqlAlchemyAdapter(ABC):
    session = None
    entity = None

    def __init__(self):
        self._session_maker()

    def create(self, entity):
        try:
            f = entity
            self.session.begin()
            self.session.add(f)
            self.session.commit()
            return entity
        except Exception as e:
            self.session.rollback()
            raise e

    def find_all(self):
        try:
            result = self.session.query(self.entity)
            return result.all()
        except Exception as e:
            raise e

    def _session_maker(self):
        driver = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' % ("root",
                                                                  "123456",
                                                                  "localhost",
                                                                  "3306",
                                                                  "db_notes")
        engine = create_engine(driver, echo=True, isolation_level="READ UNCOMMITTED", pool_recycle=180, encoding='utf8')
        self.session = scoped_session(sessionmaker(bind=engine, autocommit=True))
