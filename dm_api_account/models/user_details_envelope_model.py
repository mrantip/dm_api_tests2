from datetime import datetime
from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, StrictStr, Field


class PagingSettings(BaseModel):
    postsPerPage: int
    commentsPerPage: int
    topicsPerPage: int
    messagesPerPage: int
    entitiesPerPage: int


class ColorSchema(Enum):
    MODERN = 'Modern'
    PALE = 'Pale'
    CLASSIC = 'Classic'
    CLASSIC_PALE = 'ClassicPale'
    NIGHT = 'Night'


class UserSettings(BaseModel):
    colorSchema: List[ColorSchema]
    nannyGreetingsMessage: StrictStr
    paging: PagingSettings


class BdParseMode(Enum):
    COMMON = 'Common'
    INFO = 'Info'
    POST = 'Post'
    CHAT = 'Chat'


class InfoBdText(BaseModel):
    value: StrictStr
    parseMode: List[BdParseMode]


class Rating(BaseModel):
    enabled: bool
    quality: int
    quantity: int


class Roles(Enum):
    GUEST = 'Guest'
    PLAYER = 'Player'
    ADMINISTRATOR = 'Administrator'
    NANNY_MODERATOR = 'NannyModerator'
    REGULAR_MODERATOR = 'RegularModerator'
    SENIOR_MODERATOR = 'SeniorModerator'


class UserDetails(BaseModel):
    login: StrictStr
    roles: List[Roles]
    mediumPictureUrl: Optional[StrictStr] = Field(None)
    smallPictureUrl: Optional[StrictStr] = Field(None)
    status: Optional[StrictStr] = Field(None)
    rating: Rating
    online: Optional[datetime] = Field(None)
    name: Optional[StrictStr] = Field(None)
    location: Optional[StrictStr] = Field(None)
    registration: Optional[datetime] = Field(None)
    icq: Optional[StrictStr] = Field(None)
    skype: Optional[StrictStr] = Field(None)
    originalPictureUrl: Optional[StrictStr] = Field(None)
    info: InfoBdText
    settings: UserSettings


class UserDetailsEnvelopeModel(BaseModel):
    resource: UserDetails
    metadata: Optional[StrictStr] = Field(None)
