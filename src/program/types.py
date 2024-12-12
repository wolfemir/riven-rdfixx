from dataclasses import dataclass
from datetime import datetime
from typing import Generator, Optional, Union

from program.media.item import MediaItem
from program.services.content import (
    Listrr,
    Mdblist,
    Overseerr,
    PlexWatchlist,
    TraktContent,
)
from program.services.downloaders import AllDebridDownloader, RealDebridDownloader

# TorBoxDownloader,
from program.services.libraries import SymlinkLibrary
from program.services.scrapers import (
    Comet,
    Jackett,
    Knightcrawler,
    Mediafusion,
    Orionoid,
    Scraping,
    TorBoxScraper,
    Torrentio,
    Zilean,
)
from program.services.updaters import Updater
from program.symlink import Symlinker

# Typehint classes
Scraper = Union[Scraping, Torrentio, Knightcrawler, Mediafusion, Orionoid, Jackett, TorBoxScraper, Zilean, Comet]
Content = Union[Overseerr, PlexWatchlist, Listrr, Mdblist, TraktContent]
Downloader = Union[RealDebridDownloader,
                #    TorBoxDownloader,
                AllDebridDownloader]
Service = Union[Content, SymlinkLibrary, Scraper, Downloader, Symlinker, Updater]
MediaItemGenerator = Generator[MediaItem, None, MediaItem | None]

class ProcessedEvent:
    service: Service
    related_media_items: list[MediaItem]

@dataclass
class Event:
    emitted_by: Service
    item_id: Optional[str] = None
    content_item: Optional[MediaItem] = None
    run_at: datetime = datetime.now()

    @property
    def log_message(self):
        if self.content_item:
            return f"Event for {self.content_item.log_string}"
        return f"Event for Item ID: {self.item_id}"