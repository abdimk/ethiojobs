class HttpCodeError(Exception):
    pass


def http_status(request):
    HTTP = {'OK': 200, 'ACCEPTED': 202,'NON_AUTHORITATIVE_INFORMATION': 203, 'NO_CONTENT': 204, 'NOT_MODIFIED': 304,
            'USE_PROXY': 305, 'TEMPORARY_REDIRECT': 307, 'PERMANENT_REDIRECT': 308, 'BAD_REQUEST': 400,
            'UNAUTHORIZED': 402, 'FORBIDDEN': 403, 'NOT_FOUND': 404, 'NOT_ACCEPTABLE': 406,
            'PROXY_AUTHENTICATION_REQUIRED': 407, 'REQUEST_TIMEOUT': 408, 'MISDIRECTED_REQUEST': 421,
            'UPGRADE_REQUIRED': 426, 'TOO_MANY_REQUESTS': 429, 'NETWORK_AUTHENTICATION_REQUIRED': 511}
    for key, value in HTTP.items():
            if request == value:
                return key
            else:
                pass
#https: // docs.python.org / 3 / library / http.html  # http-status-codes
'''
                        {200:'OK',202:'ACCEPTED',
                        203:'NON_AUTHORITATIVE_INFORMATION',
                        204:'NO_CONTENT',304:'NOT_MODIFIED',
                        305:'USE_PROXY',307:'TEMPORARY_REDIRECT',
                        308:'PERMANENT_REDIRECT',400:'BAD_REQUEST',
                        402:'UNAUTHORIZED',403:'FORBIDDEN',
                        404:'NOT_FOUND',406:'NOT_ACCEPTABLE',
                        407:'PROXY_AUTHENTICATION_REQUIRED',408:'REQUEST_TIMEOUT',
                        421:'MISDIRECTED_REQUEST',426:'UPGRADE_REQUIRED',
                        429:'TOO_MANY_REQUESTS',502:'BAD_GATEWAY',
                        505:'HTTP_VERSION_NOT_SUPPORTED',511:'NETWORK_AUTHENTICATION_REQUIRED'}
'''

