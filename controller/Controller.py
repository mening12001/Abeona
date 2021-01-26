# Envisioned and defined by Razvan Manescu

import json

from flask import Flask, request

from model.Driver import Driver
from model.Order import Order
from router.Router import Router
from flask_executor import Executor
import uuid

app = Flask(__name__)

executor = Executor(app)
router = Router()
app.config['EXECUTOR_TYPE'] = 'thread'


@app.route('/async_obtain_routes_for', methods=['POST', 'GET'])
def async_obtain_routes_for():
    if request.method == 'POST':
        drivers_and_orders = request.get_json()
        actual_drivers = []
        actual_orders = []

        for driver in drivers_and_orders['drivers']:
            actual_drivers.append(Driver(**driver))

        for order in drivers_and_orders['orders']:
            actual_orders.append(Order(**order))

        job_id = str(uuid.uuid4())
        executor.submit_stored(job_id, router.obtain_routes_for, actual_orders, actual_drivers)
        return json.dumps({'status': 'started', 'job_id': job_id})
    else:
        job_id = str(request.args.get('job_id'))
        if not executor.futures.done(job_id):
            return json.dumps({'status': 'pending', 'job_id': job_id})
        future = executor.futures.pop(job_id)
        return json.dumps({'status': 'done', 'job_id': job_id, 'result': future.result()})


# not advised
@app.route('/obtain_routes_for', methods=['POST'])
def obtain_routes_for():
    drivers_and_orders = request.get_json()
    actual_drivers = []
    actual_orders = []

    for driver in drivers_and_orders['drivers']:
        actual_drivers.append(Driver(**driver))

    for order in drivers_and_orders['orders']:
        actual_orders.append(Order(**order))

    future = executor.submit(router.obtain_routes_for, actual_orders, actual_drivers)

    return json.dumps(future.result())

