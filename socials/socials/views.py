from django.views.generic import TemplateView

class loggedInPage(TemplateView):
    template_name = 'loggedIn.html'

class loggedOutPage(TemplateView):
    template_name = 'loggedOut.html'

class HomePage(TemplateView):
    template_name = 'index.html'

class PostListPage(TemplateView):
    template_name = 'post_list.html'