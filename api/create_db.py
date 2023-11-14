from api.database.database import engine
from api.models import blog

blog.Base.metadata.create_all(bind=engine)
