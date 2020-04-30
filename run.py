from ayat import app
from ayat.authentication_routes import *
from ayat.programs_routes import *


if __name__ == '__main__':
    app.run(debug=True)