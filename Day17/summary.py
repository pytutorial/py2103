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

b1 = session.query(Book).get(1)
print(b1.author.name)


# equal
session.query(Book).filter(Book.code=='B1').all()

# > <
session.query(Book).filter(Book.qty>0).first()

#like
session.query(Book).filter(Book.name.like('%S%')).first()

#and
session.query(Book).filter(Book.qty>0,Book.author_id==2).first()

#or
from sqlalchemy import or_
session.query(Book).filter(or_(Book.name.like('%S%') ,
				Book.code.like('%S%') )
			   ).first()