from typing import NamedTuple, List, Union, Optional

#base
track_image_t = NamedTuple(
    "TrackImage",
    [("srcset", str), ("alt", str)]
)
artist_image_t = NamedTuple(
    "ArtistImage",
    [("src", str), ("alt", str)]
)
lyrics_t = NamedTuple(
    "Lyrics",
    [("name", str), ("url", str)],
)
artist_t = NamedTuple(
    "Artist",
    [("name", str), ("url", str), ("image", artist_image_t)],
)
track_t = NamedTuple(
    "Track",
    [("name", str), ("lyrics", lyrics_t), ("artist", List[artist_t]), ("image", track_image_t)],
)

#search.py
search_all_result_t = NamedTuple(
    "SearchResult",
    [("best", Optional[Union[track_t, artist_t]]), ("tracks", Optional[List[track_t]]), ("artists", Optional[List[artist_t]])],
)
