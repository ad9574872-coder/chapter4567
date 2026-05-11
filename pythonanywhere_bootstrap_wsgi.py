import os
import subprocess

HOME = '/home/AyushDutta977'
STARTED = os.path.join(HOME, '.chapter4567_deploy_started')
LOG = os.path.join(HOME, 'chapter4567_deploy.log')


def start_deploy_once():
    if os.path.exists(STARTED):
        return
    with open(STARTED, 'w') as marker:
        marker.write('started\n')

    command = r"""
set -eux
exec > /home/AyushDutta977/chapter4567_deploy.log 2>&1
mkdir -p /home/AyushDutta977/.virtualenvs
if [ -d /home/AyushDutta977/chapter4567/.git ]; then
    cd /home/AyushDutta977/chapter4567
    git pull
else
    git clone https://github.com/ad9574872-coder/chapter4567.git /home/AyushDutta977/chapter4567
    cd /home/AyushDutta977/chapter4567
fi
python3.13 -m venv /home/AyushDutta977/.virtualenvs/chapter4567-env
/home/AyushDutta977/.virtualenvs/chapter4567-env/bin/pip install --upgrade pip
/home/AyushDutta977/.virtualenvs/chapter4567-env/bin/pip install -r requirements.txt
/home/AyushDutta977/.virtualenvs/chapter4567-env/bin/python manage.py migrate --noinput
/home/AyushDutta977/.virtualenvs/chapter4567-env/bin/python manage.py collectstatic --noinput
echo DEPLOY_DONE
"""
    subprocess.Popen(
        ['/bin/bash', '-lc', command],
        cwd=HOME,
        start_new_session=True,
    )


start_deploy_once()


def application(environ, start_response):
    body = b'Deployment started. Check /home/AyushDutta977/chapter4567_deploy.log\n'
    start_response(
        '200 OK',
        [
            ('Content-Type', 'text/plain'),
            ('Content-Length', str(len(body))),
        ],
    )
    return [body]
