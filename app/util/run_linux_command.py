import subprocess
from flask import current_app as app

def run_cmd_error_handling(cmd):
    with app.app_context():
        app.logger.info("Running: " + cmd)
        try:
            p = subprocess.run(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,
                               universal_newlines=True, check=True)
            output = p.stdout.strip()
            app.logger.info("cmd success, output: "+ output)
            return p.returncode, output
        except subprocess.CalledProcessError as e:
            app.logger.info("This command failed to run: %s" % e.cmd)
            app.logger.info(e.output)
            app.logger.error(e.stderr)