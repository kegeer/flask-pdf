import os

from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db, models

env = os.environ.get('BLOG_ENV', 'dev')
app = create_app('app.config.%sConfig' % env.capitalize())
manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('server', Server(host='127.0.0.1', port=8090))
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(
        app = app,
        db = db,
        Client=models.Client,
        ClientSchema=models.ClientSchema,
        Result=models.Result,
        ResultSchema=models.ResultSchema,
        General=models.General,
        Info=models.Info,
        InfoSchema=models.InfoSchema,
        Metabolism=models.Metabolism,
        Species=models.Species,
        Genus=models.Genus,
        Disease=models.Disease,
        Ref=models.Ref,
        RefSchema=models.RefSchema,
    )

if __name__ == '__main__':
    manager.run()