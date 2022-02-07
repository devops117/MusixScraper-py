BASE_URL = "https://www.musixmatch.com"
USER_AGENT_HEADER = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0"}

#search.py
SEARCH_URL = f"{BASE_URL}/search"

MAIN_BOXES_CSS_SELECTOR = "div.main-panel > div.box"
SIDE_BOXES_CSS_SELECTOR = "div.side-panel > div.box"
BOX_TITLE_CSS_SELECTOR = "div.box-header > h3.box-title"

IMAGE_CSS_SELECTOR = "div.media-card-picture > img"

TRACK_CSS_SELECTOR = "div.box-content > div > ul.tracks.list > li > div.track-card.media-card.has-picture"
TRACK_TITLE_CSS_SELECTOR = "div.media-card-body > div.media-card-text > h2.media-card-title > a.title"
TRACK_ARTISTS_CSS_SELECTOR = "div.media-card-body > div.media-card-text > h3.media-card-subtitle > span.artist-field > span > a.artist"
ARTIST_CSS_SELECTOR = "div.box-content > ul.artists.list > li > div.artist-card.media-card.has-picture"
ARTIST_TITLE_CSS_SELECTOR = "div.media-card-body > div.media-card-text > h2.media-card-title > a.cover"
