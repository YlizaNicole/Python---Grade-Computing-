from typing import Any, Mapping, Optional, ValuesView

from ..core import Env


class EnvSpec(object):
    def __init__(
        self, 
        id: str, 
        entry_point:Optional[str]=..., 
        reward_threshold:Optional[int]=..., 
        nondeterministic:bool=..., 
        max_episode_steps:Optional[int]=..., 
        kwargs:Optional[Mapping[str, Any]]=...
    ) -> None: ...
    def make(self, **kwargs: Any) -> Env: ...

class EnvRegistry(object):
    def make(self, path: str, **kwargs: Any) -> Env: ...
    def all(self) -> ValuesView[EnvSpec]: ...
    def spec(self, path: str) -> EnvSpec: ...
    def register(self, id: str, **kwargs: Any) -> None: ...

# Have a global registry
registry: EnvRegistry

def register(id: str, **kwargs: Any) -> None: ...
def make(id: str, **kwargs: Any) -> Env: ...
def spec(id: str) -> EnvSpec: ...
