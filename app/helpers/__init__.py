from app import app
from app.helpers import quick_field


app.jinja_env.globals.update(
    quick_field=quick_field
)
