# aws db cred
# export SQLALCHEMY_DATABASE_URI=postgresql://postgres:admin123@tiffily-database.cpjvyspbrbam.ap-south-1.rds.amazonaws.com:5432/Tiffily

# local db cred
export SQLALCHEMY_DATABASE_URI=postgresql://postgres:admin@localhost:5432/Tiffily_DB


export JWT_SECRET_KEY=34664b98310e4415ae09460c608d0509@392dc1e9dafe644dd93c65fd24bbcbc8e
export FLASK_APP=run.py
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=5000
export FLASK_ENV=development
export DEBUG=True

flask run
# export PROFILE_SERVICE_DB_HOST=tiffily-database.cpjvyspbrbam.ap-south-1.rds.amazonaws.com
# export PROFILE_SERVICE_DB_USER=postgres
# export PROFILE_SERVICE_DB_PASSWORD=admin123
# export PROFILE_SERVICE_DB_NAME=Tiffily