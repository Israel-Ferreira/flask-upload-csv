from flask import make_response, jsonify

def create_error_response(msg: str, status_code: int):
    json_body =  {"error_msg": msg}

    response =  make_response(jsonify(json_body), status_code)
    response.headers["Content-Type"] = "application/json"

    return response



def create_success_response(json_body, status_code):
    if json_body is None:
        response =  make_response(None, status_code)
    else:
        response =  make_response(jsonify(json_body), status_code)

    response.headers["Content-Type"] = "application/json"

    return response