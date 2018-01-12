# import key pieces from bottle package
from bottle import route, run, static_file, redirect
# import os for reading environment variables
import os


def get_static_root():
    """
    Return root directory for static content
    """
    return os.environ.get('STATIC_CONTENT_ROOT', '/opt/app-root/src/static')


@route('/')
def root_page():
    """
    Route for root path, just try to redirect to static/index.html
    """
    redirect('/static/index.html')


@route('/static/<path:path>')
def server_static(path):
    """
    Serve static content under /static
    """
    return static_file(path, get_static_root())


@route('/healthz')
def healthz():
    """
    Status endpoint for health checks
    """
    return 'OK'


if __name__ == '__main__':
    # Here we simply start the server process
    run(host='0.0.0.0', port=8080, reloader=True)
