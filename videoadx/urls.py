from torneira.core.dispatcher import url
from controller import VideologController

urls = (
	url(r"/player/{user_id}/{source_id}/config.xml", VideologController, action='config', name="videolog-config"),
)
