from eduvpn.metadata import Metadata

def totp_enroll_window(builder, oauth, meta: Metadata, config_dict: dict, lets_connect: bool, secret=None) -> None: ...
def _make_qr(builder, oauth, meta: Metadata, config_dict: dict, lets_connect: bool, secret=None) -> None: ...
def _parse_user_input(builder, oauth, meta: Metadata, config_dict: dict, lets_connect: bool, secret) -> None: ...
def _enroll(builder, oauth, meta, config_dict, secret, key, lets_connect: bool) -> None: ...