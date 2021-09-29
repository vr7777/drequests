# drequests

# Example
```python
  from API import drequests, Endpoints as e

  auth = "DISCORD_TOKEN"
  
  username = drequests.get(e.username, auth)
  discriminator = drequests.get(e.discriminator, auth)
  print(f"{username}#{discriminator}")
  
  
  
  # Change About Me #

  drequests.patch(e.bio, "This is the new about me text", auth)
  newbio = drequests.get(e.bio, auth) # Print out the new about me
  print(newbio)
```
