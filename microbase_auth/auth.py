from typing import List, Dict, Tuple
from enum import Enum

import jwt
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError, InvalidTokenError, DecodeError


class AuthSignatureType(Enum):
    User = 1
    Service = 2


class AuthManager:

    _signatures: Dict[AuthSignatureType, str] = []
    _default_sig_type: AuthSignatureType = AuthSignatureType.User
    _algo: str = 'HS256'

    def __init__(self):
        self._signatures = {}

    def _encode(self, payload: dict, sig: str, algo: str) -> str:
        return jwt.encode(payload, sig, algo).decode('utf-8')

    def _decode(self, token: str, sig: str, algo: str) -> dict:
        return jwt.decode(token, sig, algorithms=[algo])

    def get_default_sig(self, signature_type: AuthSignatureType) -> str:
        if signature_type is None:
            return self._signatures[self._default_sig_type]
        else:
            return self._signatures[signature_type]

    def set_signature(self, sig: str, type: AuthSignatureType, is_default=False):
        self._signatures[type] = sig

        if is_default:
            self._default_sig_type = type

    def get_token(self, payload: dict, signature_type:AuthSignatureType=None):
        token = self._encode(payload, self.get_default_sig(signature_type), self._algo)

        return token

    def get_payload(self, token: str, signature_type: AuthSignatureType=None) -> dict:
        payload = self._decode(token, self.get_default_sig(signature_type), self._algo)

        return payload

    def get_any_payload(self, token: str) -> Tuple[dict, AuthSignatureType]:
        for type in self._signatures:
            try:
                payload = self.get_payload(token, signature_type=type)
                return (payload, type)
            except Exception as e:
                pass

        return None