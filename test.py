import sys
from faker import Faker


from server import (
	db,
	Pelanggaran,
	Aplikasi)

fake = Faker()
fake.seed(2000)


def main(args):
	if args == "db":
		print "testing database with dummy data"

		print "testing table 'Pelanggaran'"

		for i in range(10):
			text = fake.text()

			p = Pelanggaran(text=text)
			db.session.add(p)

		db.session.commit()
		print Pelanggaran.query.all()


		print "testing aplikasi"

if __name__ == '__main__':
	if sys.argv[1] == 'db':
		db.create_all()
		main('db')
