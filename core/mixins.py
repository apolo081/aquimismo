from django.core.urlresolvers import reverse
from django.shortcuts import redirect


class IsAuthenticatedMixin(object):
    def is_authenticated(self,request):
        if not request.user.is_authenticated():
            return redirect(reverse('login_url'))
        return None