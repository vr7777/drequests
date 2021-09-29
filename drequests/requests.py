def get(endpnt, auth):
        try:
            if endpnt in endpntlist:
                try:
                    r = requests.get("https://discord.com/api/v9/users/@me", headers={"authorization": auth})
                    json = r.json()
                    return json[f'{endpnt}']  
                except:
                    print("Error with request.")
            elif endpnt not in endpntlist:
                print("Internal Error Occured: ", "Endpoint does not exist.")
        except:
            print("Internal Error Occured: ", sys.exc_info()[0])
            
 def patch(endpnt, arg1, auth):
        try:
            if endpnt in endpntlist:
                content = {
                    endpnt: arg1
                }
                headers = {
                    "authorization": auth,
                }
                r = requests.patch("https://discord.com/api/v9/users/@me", headers=headers, json=content)
                if r.status_code == 200:
                    print('200: Request sent successfully.')
                else:
                    print(r.status_code, "Request could not be completed.")
                    print(r.content)
            elif endpnt not in endpntlist:
                print("Internal Error Occured: ", "Endpoint does not exist.")
        except:
            print("Internal Error Occured: ", sys.exc_info()[0])
