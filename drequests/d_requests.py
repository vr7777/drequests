import requests, sys


#class Apis(object):








endpntlist = ["accent_color", "avatar", "banner", "banner_color", "bio", "discriminator", "email", "flags", "id",
              "locale", "mfa_enabled", "nsfw_allowed", "phone", "premium_type", "premium_usage_flag",
              "public_flags", "purchased_flags", "token", "username", "verified", None]

class Endpoints(object):
    accent_color = "accent_color"
    avatar = "avatar"
    banner = "banner"
    banner_color = "banner_color"
    bio = "bio"
    discriminator = "discriminator"
    email = "email"
    flags = "flags"
    id = "id"
    locale = "locale"
    mfa_enabled = "mfa_enabled"
    nsfw_allowed = "nsfw_allowed"
    phone = "phone"
    premium_type = "premium_type"
    premium_usage_flags = "premium_usage_flags"
    public_flags = "public_flags"
    purchased_flags = "purchased_flags"
    tokenData = "token"
    username = "username"
    verified = "verified"
    

class drequests(object):
    """def __init__(self, endpnt, status, json):
        self.endpnt = endpnt
        self.status = status
        self.json = json[f'{endpnt}']

    def json(self):
        print()"""


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
  
    def test(api, endpnt, auth):
        try:
            if endpnt in endpntlist:
                try:
                    r = requests.get(f"https://discord.com/api/{api}/users/@me", headers={"authorization": auth})
                    json = r.json()
                    return json[f'{endpnt}']  
                except:
                    print("Error with request.")
            elif endpnt not in endpntlist:
                print("Internal Error Occured: ", "Endpoint does not exist.")
        except:
            print("Internal Error Occured: ", sys.exc_info()[0])




# True/False endpoints should be booleans... EX: "nsfw_allowed", True, "TOKEN HERE"
# Integer Endpoints should be of type int


