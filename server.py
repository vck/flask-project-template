#/usr/bin/python


from flask import (
	Flask,
	request,
	render_template,
	redirect,
	url_for
)

from flask_sqlalchemy import SQLAlchemy as sql 
from flask_cache import Cache

import yaml
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test2.db'
app.config['CACHE_TYPE'] = 'RedisCache'
app.config['CACHE_REDIS_HOST'] = 'localhost'
app.config['CACHE_REDIS_PORT'] = '6379'

cache = Cache()
cache.init_app(app)
db = sql(app)


class Aplikasi(db.Model):

	__tablename__ = "Aplikasi"

	id = db.Column(db.Integer, primary_key=True)
	nama = db.Column(db.Text)
	icon_url = db.Column(db.Text)
	jenis = db.Column(db.Text)
	nama_perusahaan = db.Column(db.Text)
	waktu_input = db.Column(db.DateTime)


	def __init__(self, nama, icon_url, jenis, nama_perusahaan, waktu_input=None):
		self.nama = nama 
		self.icon_url = icon_url
		self.jenis = jenis 
		self.nama_perusahaan = nama_perusahaan

		if waktu_input is None:
			waktu_input = datetime.utcnow()

		self.waktu_input = waktu_input

	def __repr__(self):
		return '<Aplikasi %r>'%self.nama



class Pelanggaran(db.Model):

	__tablename__ = "Pelanggaran"

	id = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.Text)

	def __init__(self, text):
		self.text = text


	def __repr__(self):
		return '<Pelanggaran %r>'%self.text


@app.route('/')
@cache.cached(timeout=1440)
def index():	
	return render_template("index.html", data=Pelanggaran.query.all())


@cache.cached(timeout=1440)
@app.route('/tentang')
def tentang():
	return render_template("about.html")


@app.route('/input')
def admin_panel():
	return render_template('input.html')


@app.route('/simpan', methods=['POST'])
def simpan_data():
	if request.method == 'POST':

		payload = request.form['test']

		try:
			print yaml.load(payload)
		except:
			print "unable to parse payload!"

		return redirect(url_for('admin_panel'))

@cache.cached(timeout=1440)
@app.route('/<string:nama>')
def tampil_perlaman(nama):
	return render_template('index.html', name=nama)