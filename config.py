import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    # Blob Storage
    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT')
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY')
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER')

    # SQL Database values from Azure App Service → Environment Variables
    SQL_SERVER = os.environ.get('SQL_SERVER')
    SQL_DATABASE = os.environ.get('SQL_DATABASE')
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME')
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD')

    # ✅ CORRECT AZURE SQL CONNECTION STRING
    if SQL_SERVER:
        SQLALCHEMY_DATABASE_URI = (
            "mssql+pyodbc://{}:{}@{}:1433/{}"
            "?driver=ODBC+Driver+18+for+SQL+Server"
            "&Encrypt=yes&TrustServerCertificate=no&Connection Timeout=30;"
        ).format(
            SQL_USER_NAME,
            SQL_PASSWORD,
            SQL_SERVER,
            SQL_DATABASE
        )
    else:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Microsoft Authentication
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    CLIENT_ID = os.environ.get("CLIENT_ID")

    AUTHORITY = "https://login.microsoftonline.com/common"

    REDIRECT_PATH = "/getAToken"

    SCOPE = ["User.Read"]

    SESSION_TYPE = "filesystem"