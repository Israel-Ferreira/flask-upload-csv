from flask import Flask, request
from werkzeug.utils import secure_filename
from utils import file_extension_has_allowed, create_error_response, create_success_response


from prometheus_flask_exporter import PrometheusMetrics

from typing import List

from models.product import Product



import csv
import os


app = Flask(__name__)
metrics =  PrometheusMetrics(app)


metrics.info("app_info", "products-api", version="1.1")


app.config["UPLOAD_FOLDER"] = "temp"

products : List[Product]  = []



def read_csv(csv_file_path):
    with open(csv_file_path, "r", newline='') as csv_file:
        csv_reader =  csv.reader(csv_file, delimiter=";")

        csv_headers =  ['sku', 'model', 'manufacturer', 'price']

        for csv_line in csv_reader:
            if  not csv_line == csv_headers and not len(csv_line) == 0:
                print(csv_line)
            
                product =  Product(csv_line[0], csv_line[1], csv_line[2], csv_line[3])
                
                products.append(product)


@app.get("/products")
def get_products():
    json_resp = [product.to_dict() for product in products]
    return create_success_response(json_resp, 200)


@app.route("/products/import-products",methods=["POST"])
def upload_csv():
    if "file" not in request.files:
        error_msg = "O parâmetro file não está presente na requisição"
        return create_error_response(error_msg, 400)

    csv_file = request.files["file"]

    if csv_file and file_extension_has_allowed(csv_file.filename):

        secured_filename =  secure_filename(csv_file.filename)

        try:
            csv_file_path = os.path.join(app.config["UPLOAD_FOLDER"],secured_filename)
            csv_file.save(csv_file_path)

            read_csv(csv_file_path)

            return create_success_response({}, 201)
        except Exception as _:
            return create_error_response("Erro ao processar a requisição", 500)
        
    else:
        error_msg = "Extensão não permitida"
        return create_error_response(error_msg, 400)
    


@app.route("/products/<sku>")
def get_product_by_sku(sku):
    product_result =  [prdct for prdct in products if prdct.sku == sku]


    if len(product_result) == 0:
        return create_error_response("Produto não encontrado", 404)
    

    body =  product_result[0].to_dict()

    print(type(body))


    return create_success_response(body, 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False)
