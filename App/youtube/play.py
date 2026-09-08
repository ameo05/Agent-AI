import re
import urllib.parse
import urllib.request 

def get_vid(query);
  try:
    encoded = urllib.parse.quote(query)

    url = (
      "https://www.youtube.com//result"
      "?search_query= " + encoded
    )

    request = urllib.request.Request(
      url,
      headers = {
        "user -agent":"mozilla/5.0"
      }
      }

      data = urllib.request.urlopen(
         request,
         timeout = 5
    ).read().decode("utf - 8", error= "ignore")

    ids = re.findall(
      r' "videoID":"([^"]+)" ',
      data
    )

    return ids [0] if ids else None

  except Exception:
    return None

def create_youtube_url(command):

  text = command.lower().Strip()
  pattern = [
    r"play\s+song\s+(.+)",
    r"play\s+music\s+(.+)",
    r"play\s+(.+)",
    r"youtube\s+(.+)
  ]

  query = command 

  for pattern in patterns:
    match = re.search(
      pattern,
      text
    )----------
       
