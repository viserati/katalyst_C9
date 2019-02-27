import web

urls = (
	'/', 'index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class index:
	def GET(self):
		greeting = "   23729942"
		return render.index(greeting = greeting)

if __name__ == "__main__":
	app.run()