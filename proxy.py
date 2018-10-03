from flask import Flask, request, jsonify, render_template

import datetime
import struct
import binascii
import base64

import json

from TR50 import TR50http

def tr50_lora_send(content_json, dw_thing_key, dw_corrid, dw_thing_name, lora_app_id, lora_dev_id, lora_hardware_serial,
                   lora_gw_id, lora_gw_channel, lora_gw_rssi, lora_gw_snr, lora_gw_rf_chain,
                   lora_frequency, lora_modulation, lora_data_rate, lora_coding_rate, lora_port, lora_counter,
                   ccs811_co2=None, ccs811_voc=None,
                   dps310_pressure=None, dps310_temperature=None, mcp9808_temperature=None,
                   pms7003_pm_10_0=None, pms7003_pm_1_0=None, pms7003_pm_2_5=None,
                   sht31_humidity=None, sht31_temperature=None):

    config_lora = {
        'endpoint': 'http://api-de.devicewise.com/api',
        'app_id': '0000001', # it has to be locked ID value for each logic device. (generating from serial numbers?)
        'app_token': 'APP_TOKEN',
        'thing_key': dw_thing_key
    }

    tr50http = TR50http.TR50http(config_lora)

    result = tr50http.execute('thing.update', {'name': dw_thing_name, 'corrId': dw_corrid})
    print(tr50http.get_response())

    result = tr50http.execute('thing.attr.set', {'key': 'lora_app_id','value': lora_app_id, 'corrId': dw_corrid})
    print(tr50http.get_response())

    result = tr50http.execute('thing.attr.set', {'key': 'lora_dev_id', 'value': lora_dev_id, 'corrId': dw_corrid})
    print(tr50http.get_response())

    result = tr50http.execute('thing.attr.set', {'key': 'lora_hardware_serial', 'value': lora_hardware_serial, 'corrId': dw_corrid})
    print(tr50http.get_response())

    # Set Gateways Details

    result = tr50http.execute('thing.attr.set', {'key': 'lora_gateway_id', 'value': lora_gw_id, 'corrId': dw_corrid})
    print(tr50http.get_response())

    result = tr50http.execute('thing.attr.set', {'key': 'lora_frequency', 'value': lora_frequency, 'corrId': dw_corrid})
    print(tr50http.get_response())

    result = tr50http.execute('thing.attr.set', {'key': 'lora_modulation', 'value': lora_modulation, 'corrId': dw_corrid})
    print(tr50http.get_response())

    result = tr50http.execute('thing.attr.set', {'key': 'lora_data_rate', 'value': lora_data_rate, 'corrId': dw_corrid})
    print(tr50http.get_response())

    result = tr50http.execute('thing.attr.set', {'key': 'lora_coding_rate', 'value': lora_coding_rate, 'corrId': dw_corrid})
    print(tr50http.get_response())

    result = tr50http.execute('thing.attr.set', {'key': 'lora_port', 'value': lora_port, 'corrId': dw_corrid})
    print(tr50http.get_response())

    result = tr50http.execute('thing.attr.set', {'key': 'lora_counter', 'value': lora_counter, 'corrId': dw_corrid})
    print(tr50http.get_response())

    result = tr50http.execute('property.publish', {'key': 'lora_gateway_channel', 'value': lora_gw_channel, 'corrId': dw_corrid, 'aggregate': True})
    print(tr50http.get_response())

    result = tr50http.execute('property.publish', {'key': 'lora_gateway_rssi', 'value': lora_gw_rssi, 'corrId': dw_corrid, 'aggregate': True})
    print(tr50http.get_response())

    result = tr50http.execute('property.publish', {'key': 'lora_gateway_snr', 'value': lora_gw_snr, 'corrId': dw_corrid, 'aggregate': True})
    print(tr50http.get_response())

    result = tr50http.execute('property.publish', {'key': 'lora_gateway_rf_chain', 'value': lora_gw_rf_chain, 'corrId': dw_corrid, 'aggregate': True})
    print(tr50http.get_response())

    # log all json content

    result = tr50http.execute('log.publish', {'msg': content_json, 'corrId': dw_corrid})
    print(tr50http.get_response())


    # Set Sensors Data

    if ccs811_voc and ccs811_co2 != None:
        result = tr50http.execute('property.publish', {'key': 'ccs811_co2', 'value': ccs811_co2, 'corrId': dw_corrid, 'aggregate': True})
        print(tr50http.get_response())

        result = tr50http.execute('property.publish', {'key': 'ccs811_voc', 'value': ccs811_voc, 'corrId': dw_corrid, 'aggregate': True})
        print(tr50http.get_response())

        result = tr50http.execute('property.publish', {'key': 'dps310_pressure', 'value': dps310_pressure, 'corrId': dw_corrid, 'aggregate': True})
        print(tr50http.get_response())

        result = tr50http.execute('property.publish', {'key': 'dps310_temperature', 'value': dps310_temperature, 'corrId': dw_corrid, 'aggregate': True})
        print(tr50http.get_response())

        result = tr50http.execute('property.publish', {'key': 'mcp9808_temperature', 'value': mcp9808_temperature, 'corrId': dw_corrid, 'aggregate': True})
        print(tr50http.get_response())

        result = tr50http.execute('property.publish', {'key': 'pms7003_pm_10_0', 'value': pms7003_pm_10_0, 'corrId': dw_corrid, 'aggregate': True})
        print(tr50http.get_response())

        result = tr50http.execute('property.publish', {'key': 'pms7003_pm_1_0', 'value': pms7003_pm_1_0, 'corrId': dw_corrid, 'aggregate': True})
        print(tr50http.get_response())

        result = tr50http.execute('property.publish', {'key': 'pms7003_pm_2_5', 'value': pms7003_pm_2_5, 'corrId': dw_corrid, 'aggregate': True})
        print(tr50http.get_response())

    elif sht31_humidity and sht31_temperature != None:

        result = tr50http.execute('property.publish', {'key': 'sht31_humidity', 'value': sht31_humidity, 'corrId': dw_corrid, 'aggregate': True})
        print(tr50http.get_response())

        result = tr50http.execute('property.publish', {'key': 'sht31_temperature', 'value': sht31_temperature, 'corrId': dw_corrid, 'aggregate': True})
        print(tr50http.get_response())


app = Flask(__name__)


@app.route('/lorawan/<application>', methods=['POST'])
def lora_message(application):


    content = request.json # grab the json data from the POST request
    content_json = json.dumps(content)

    #print('Application: {}'.format(application))
    #print('Content: {}'.format(content))

    dw_thing_key = content['dev_id'] + '__' + content['hardware_serial']
    dw_corrid = content['metadata']['time'] + '__' + content['hardware_serial'] # 2018-10-02T09:20:59.918693098Z__077E464C6C05A883
    dw_thing_name = content['dev_id']

    lora_app_id = content['app_id']
    lora_dev_id = content['dev_id']
    lora_hardware_serial = content['hardware_serial']

    # Get Metadata->Gateways details

    lora_gw_id = content['metadata']['gateways'][0]['gtw_id'] # can be more GTW in one frame?
    lora_gw_channel = content['metadata']['gateways'][0]['channel']
    lora_gw_rssi = content['metadata']['gateways'][0]['rssi']
    lora_gw_snr = content['metadata']['gateways'][0]['snr']
    lora_gw_rf_chain = content['metadata']['gateways'][0]['rf_chain']

    lora_frequency = content['metadata']['frequency']
    lora_modulation = content['metadata']['modulation']
    lora_data_rate = content['metadata']['data_rate']
    lora_coding_rate = content['metadata']['coding_rate']
    lora_port = content['port']
    lora_counter = content['counter']

    if 'ccs811' in content['payload_fields']:
        print('Function #1')

        ccs811_co2 = content['payload_fields']['ccs811']['co2']
        ccs811_voc = content['payload_fields']['ccs811']['voc']

        dps310_pressure = round(content['payload_fields']['dps310']['pressure'], 2) # ,xx float
        dps310_temperature = round(content['payload_fields']['dps310']['temperature'], 2) # ,xx float

        mcp9808_temperature = round(content['payload_fields']['mcp9808']['temperature'], 2) # ,xx float

        pms7003_pm_10_0 = content['payload_fields']['pms7003']['pm_10_0']
        pms7003_pm_1_0 = content['payload_fields']['pms7003']['pm_1_0']
        pms7003_pm_2_5 = content['payload_fields']['pms7003']['pm_2_5']

        tr50_lora_send(content_json, dw_thing_key, dw_corrid, dw_thing_name, lora_app_id, lora_dev_id, lora_hardware_serial,
                       lora_gw_id, lora_gw_channel, lora_gw_rssi, lora_gw_snr, lora_gw_rf_chain,
                       lora_frequency, lora_modulation, lora_data_rate, lora_coding_rate, lora_port, lora_counter,
                       ccs811_co2=ccs811_co2, ccs811_voc=ccs811_voc,
                       dps310_pressure=dps310_pressure, dps310_temperature=dps310_temperature, mcp9808_temperature=mcp9808_temperature,
                       pms7003_pm_10_0=pms7003_pm_10_0, pms7003_pm_1_0=pms7003_pm_1_0, pms7003_pm_2_5=pms7003_pm_2_5, sht31_humidity=None, sht31_temperature=None)

    if 'sht31' in content['payload_fields']:
        print('Function #2')

        sht31_humidity = round(content['payload_fields']['sht31']['humidity'], 2) # ,xx float
        sht31_temperature = round(content['payload_fields']['sht31']['temperature'], 2) # ,xx float

        tr50_lora_send(content_json, dw_thing_key, dw_corrid, dw_thing_name, lora_app_id, lora_dev_id, lora_hardware_serial,
                       lora_gw_id, lora_gw_channel, lora_gw_rssi, lora_gw_snr, lora_gw_rf_chain,
                       lora_frequency, lora_modulation, lora_data_rate, lora_coding_rate, lora_port, lora_counter,
                       ccs811_co2=None, ccs811_voc=None, dps310_pressure=None, dps310_temperature=None,
                       mcp9808_temperature=None,
                       pms7003_pm_10_0=None, pms7003_pm_1_0=None, pms7003_pm_2_5=None, sht31_humidity=sht31_humidity, sht31_temperature=sht31_temperature)

    return('', 200)


@app.route('/') # the default REST method in Flask is GET
def show_print():
    return "--- TTN to deviceWISE PROXY ---"


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
