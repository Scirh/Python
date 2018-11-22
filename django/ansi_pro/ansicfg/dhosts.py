#
# import json
# from sqlalchemy import create_engine
# from sqlalchemy import Column, String, Integer
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
#
# engin = create_engine('sqlite://///mnt/django/ansib_pro/db.sqlite3')
#
# Base = declarative_base()
# Session = sessionmaker(bind=engin)
# session = Session()
#
#
# class Hosts(Base):
#
#     __tablename__ = 'webansi_host'
#
#     id =  Column(Integer,primary_key=True)
#     hostname = Column(String(20))
#     group = Column(String(20))
#
# if __name__ == '__main__':
#     qset = session.query(Hosts.hostname,Hosts.group).all()
#     host_list = {}
#     for g,h in qset:
#         if g not in host_list:
#             host_list[g] = {}
#             host_list[g]['hosts'] = [h]
#         else:
#             host_list[g]['hosts'].append(h)
#         print json.dumps(host_list)

192.168.1.1
192.168.1.2
