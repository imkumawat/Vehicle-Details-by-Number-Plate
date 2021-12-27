def get_SessionID(remote_response_headers):
    Set_Cookies = remote_response_headers.get('Set-Cookie')
    Set_Cookies= Set_Cookies.split(';')[0]
    cookies = {"PHPSESSID": "4m0eq73vr112ap2s8b46in0r6c"}
    cookies["PHPSESSID"] =Set_Cookies.split('=')[1]
    return cookies