class LoginRequiredMixin(object):
    """
    Ensures that user must be authenticated in order to access view.
    """
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(*args, **kwargs)