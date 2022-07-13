from datetime import datetime

class DateFormatException(Exception):
	pass

class DateException(Exception):
	pass


def is_old_enough(birthdate,date_test):
	try:
		d1 = datetime.strptime(birthdate, "%Y/%m/%d")
		d2 = datetime.strptime(date_test, "%Y/%m/%d")
	except  ValueError:
		raise DateFormatException
	diff= d2.year - d1.year
	if(diff<0):
		raise DateException
	else:
		return (diff > 18)
