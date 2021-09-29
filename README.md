# drequests
drequests is a work in progress api wrapper for Discord's /v9/users/@me endpoint. Planning on adding more endpoints in the future. For now, this project is very useful for automating about me's and more. 

DM vr#7777 on Discord if you have any inquires/suggestions.




# Example
```python
  from d_requests import drequests, Endpoints as e

  auth = "DISCORD_TOKEN"
  
  username = drequests.get(e.username, auth)
  discriminator = drequests.get(e.discriminator, auth)
  print(f"{username}#{discriminator}")
  
  
  
  # Change About Me #

  drequests.patch(e.bio, "This is the new about me text", auth)
  newbio = drequests.get(e.bio, auth) # Print out the new about me
  print(newbio)
```

# Things to keep in mind #
* Discord has a rate limit for changing about me's.
* If you change an accounts about me with drequests, make sure to have a verified phone number attached. It **WILL** phone lock your account.
* Anything you do with this wrapper is completely on you, I take no responsibility for any mishaps that may happen.


# Installation 
```
pip install -U git+https://github.com/downvert1/drequests.git
```
