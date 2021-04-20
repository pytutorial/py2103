from db import *

session = Session()
session.query(Author).all()  # select * from author

auth = Author(name='Nguyễn Tuân', alias='')
session.add(auth)
session.commit()

auth = session.query(Author).get(1)
#auth.alias = '---'
session.delete(auth)
session.commit()

book = Book(code='B1', name='Số đỏ', qty=5,author_id=2)
#book = Book()
#book.code = 'B1'
#book.name = 'Số đỏ'
#book.qty =...
session.add(book)
session.commit()