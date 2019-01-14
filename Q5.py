import os
import sys
from azure.storage.blob import BlockBlobService
import re
from flask import Flask, jsonify, request
import pandas as pd
import numpy as np
from scipy.stats import rankdata as rd

app = Flask("Hello World")
my_result = {"result": "Enter URL", "uploaded_url": "none", "app name": app.name}


@app.route('/', methods=['GET'])
def get_result():
    return jsonify(my_result)


@app.route('/processjson', methods=['POST'])
def processjson():
    data = request.get_json()

    # extract container name and file name from url using regex
    my_url = data['my_url']
    pattern = re.compile(r'(?<=net\/).*?(?=\/)')
    matches = pattern.findall(my_url)
    container_name = matches[0]
    my_reg = r"(?<=" + container_name + "\/).*"
    pattern = re.compile(my_reg)
    matches = pattern.findall(my_url)
    local_file_name = matches[0]


    # download file
    block_blob_service = BlockBlobService(account_name='dsconvreport',
                                          account_key='2wIt3xVY2HR5mXfl2489ctyE1CIewgwA0am+jE85HkOfOBKc7Af0KHHb2YS9Z466T+v9KClZXYeht21M3oXFYw==')
    full_path_to_file = local_file_name
    block_blob_service.get_blob_to_path(container_name, local_file_name, full_path_to_file)

    # process data
    df = pd.read_excel(full_path_to_file)
    b = df.values.tolist()
    my_sup_val = []
    my_items = []
    my_ranks = []
    for i in b:
        if i[0] not in my_items:
            my_items.append(i[0])

    for j in my_items:
        for i in b:
            if i[0] == j:
                my_sup_val.append(i[2])
        my_ranks.extend(rd(my_sup_val, method="dense"))
        my_sup_val = []

    # make new file
    df["supplier_rank"] = my_ranks
    new_file = "Test_Supplierdata_gaurav.xlsx"
    df.to_excel(new_file)

    # Upload file
    block_blob_service.create_blob_from_path(container_name, new_file, new_file)

    output_url = "https://dsconvreport.blob.core.windows.net/"+container_name+"/"+ new_file
    my_result['result'] = "Uploaded Successfully"
    my_result['uploaded_url'] = output_url
    return jsonify({'output_url': output_url, 'Message': 'Successfully Downloaded and Uploaded'})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
