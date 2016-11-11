from interswellar.models import Star

def and_search(*terms):
	return Star.query.all()

def or_search(*terms):
	return Star.query.all()