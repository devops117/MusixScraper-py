from typing import Optional

import lxml.html

from constants import (
    SEARCH_URL,
    MAIN_BOXES_CSS_SELECTOR,
    SIDE_BOXES_CSS_SELECTOR,
    BOX_TITLE_CSS_SELECTOR,
    IMAGE_CSS_SELECTOR,
    TRACK_ARTISTS_CSS_SELECTOR,
    TRACK_CSS_SELECTOR,
    TRACK_TITLE_CSS_SELECTOR,
    ARTIST_CSS_SELECTOR,
    ARTIST_TITLE_CSS_SELECTOR,
)
from musixmatch_types import (
    lyrics_t,
    artist_t, artist_image_t,
    track_t, track_image_t,
    search_all_result_t,
)
from helper_func import parse_from_url


def _get_artist(box: lxml.html.HtmlElement) -> artist_t:
    """Gets artist info"""
    image = box.cssselect(IMAGE_CSS_SELECTOR)[0]
    image = artist_image_t(image.get("src"), image.get("alt"))

    title = box.cssselect(ARTIST_TITLE_CSS_SELECTOR)[0]
    artist_url = title.get("href")
    title = title.text_content()

    return artist_t(title, artist_url, image)


def _get_track(box: lxml.html.HtmlElement) -> track_t:
    """Gets track info"""
    image = box.cssselect(IMAGE_CSS_SELECTOR)[0]
    image = track_image_t(image.get("srcset"), image.get("alt"))

    title = box.cssselect(TRACK_TITLE_CSS_SELECTOR)[0]
    lyrics = lyrics_t(title.text_content(), title.get("href"))
    title = lyrics.name

    artists = [
        artist_t(x.text_content(), x.get("href"), image=None)
        for x in box.cssselect(TRACK_ARTISTS_CSS_SELECTOR)
    ]

    return track_t(title, lyrics, artists, image)


async def searchAll(songname: Optional[str]=None, artistname: Optional[str]=None) -> search_all_result_t:
    """
    Gets all results from default search endpoint
    """
    if artistname and songname: url=f"{SEARCH_URL}/{artistname} - {songname}"
    elif songname: url=f"{SEARCH_URL}/{songname}"
    else: raise ValueError("Give me either/both songname or/and artistname")

    parsed_doc = await parse_from_url(url)

    for box in parsed_doc.cssselect(MAIN_BOXES_CSS_SELECTOR) + parsed_doc.cssselect(SIDE_BOXES_CSS_SELECTOR):
        match str.strip(box.cssselect(BOX_TITLE_CSS_SELECTOR)[0].text_content()):
            case "Best Result":
                if best := box.cssselect(TRACK_CSS_SELECTOR):
                    best = _get_track(best[0])
                elif best := box.cssselect(ARTIST_CSS_SELECTOR):
                    best = _get_artist(best[0])
            case "Tracks":
                if tracks := box.cssselect(TRACK_CSS_SELECTOR):
                    tracks = [_get_track(x) for x in tracks]
            case "Artists":
                if artists := box.cssselect(ARTIST_CSS_SELECTOR):
                    artists = [_get_artist(x) for x in artists]
    return search_all_result_t(best, tracks, artists)
