import flask

from api.v1 import api_v1
from messages.author_messages import NewAuthorRequest, UpdateAuthorRequest
from services.author_service import AuthorService
from settings.decorators.api_decorator import endpoint


# noinspection PyMethodParameters
@api_v1(name='author_api', url_prefix='authors')
class AuthorApi:

    # TODO 7 - Lot of service = AuthorService.get_instance(). Should I create a class and use it only once? (^.-)

    @endpoint(methods=['POST'])
    def new_author():
        service = AuthorService.get_instance()
        return service.create_author(NewAuthorRequest(flask.request.json))

    @endpoint(rule='<id>', methods=['GET'])
    def read_author(id):
        service = AuthorService.get_instance()  # TODO 9 - How to assure that ID has been filled?
        return service.get_author(id)

    @endpoint(rule='<id>', methods=['PUT'])
    def update_author(id):
        service = AuthorService.get_instance()
        request = UpdateAuthorRequest(flask.request.json)
        request.id = id
        return service.update_author(UpdateAuthorRequest(request))

    @endpoint(rule='<id>', methods=['DELETE'])
    def delete_author(id):
        service = AuthorService.get_instance()
        return service.delete_author(id)
