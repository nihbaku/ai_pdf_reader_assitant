from litestar import Litestar
from routes import ask, upload_pdf

app = Litestar(route_handlers=[ask, upload_pdf])
