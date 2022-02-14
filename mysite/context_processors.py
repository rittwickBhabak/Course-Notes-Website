import environ

env = environ.Env()
environ.Env.read_env()

def site_name(request):
    return {
        'site_name': env('SITE_NAME')
    }