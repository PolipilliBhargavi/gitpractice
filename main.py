servers = ["qa", "test", "prod"] 
for server in servers:
    if server == "prod":
        print("warning its a prod server")
    else:
        print(server)