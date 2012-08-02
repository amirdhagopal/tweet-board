import webapp2
import jinja2
import os

jinja_environment = jinja2.Environment( loader = jinja2.FileSystemLoader(os.path.dirname(__file__) ))


class MainPage(webapp2.RequestHandler):
	def get(self):
		
		template_values = {}
		template_values['query'] = self.request.get('query') or 'xconf'
		template_values['title'] = self.request.get('title') or 'Inspire, Ideate, Innovate'
		template_values['subject'] = self.request.get('subject') or self.request.get('query') or 'xconf'
		template_values['fullscreen'] = self.request.get('fullscreen') or 'true'
		template_values['interval'] = self.request.get('interval') or '15000'

		self.response.headers['Content-Type'] = 'text/html'
		template = jinja_environment.get_template('board.html')
		self.response.out.write(template.render(template_values))

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)