from dataclasses import dataclass


@dataclass(frozen=True)
class JwtAuth:
    refresh_token: str
    access_token: str

    @property
    def data(self) -> dict:
        return {"refresh": self.refresh_token, "access": self.access_token}
