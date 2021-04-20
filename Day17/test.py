from db2 import *
session = Session()
getProductByCode(session, 'HH_01').name
getCustomerByPhone(session, '098321231').name

order = saveOrder(session, '098321231')
saveItem(session, order.id, 'HH_01', 10)