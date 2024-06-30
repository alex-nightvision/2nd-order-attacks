import utils

def process_request(request):
    name = utils.get_name(request)
    response = utils.fetch_user_data(name)
    return response
