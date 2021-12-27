def get_token(remote_server_content):
    
    token = remote_server_content.split('var token')[1]
    token = token.split((";"))[0]
    token = token[4:-1]
    return token