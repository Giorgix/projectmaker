from flask import Flask, render_template
from flask.views import View

project = Flask(__name__)


class RenderTemplateView(View):
    def __init__(self, template_name):
        self.template_name = template_name

    def dispatch_request(self):
        return render_template(self.template_name)


project.add_url_rule('/', view_func=RenderTemplateView.as_view
                     ('home', template_name='home/home.html'))
project.add_url_rule('/about/', view_func=RenderTemplateView.as_view
                     ('about', template_name='about/about.html'))
project.add_url_rule('/contact/', view_func=RenderTemplateView.as_view
                     ('contact', template_name='contact/contact.html'))


if __name__ == '__main__':
    project.run(debug=True)
