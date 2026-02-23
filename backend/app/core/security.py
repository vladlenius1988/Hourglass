from passlib.context import CryptContext


pwd_context = CryptContext(schemes=["pbkdf2_sha256"], deprecated="auto")
MAX_BCRYPT_BYTES = 72

def _truncate_to_bcrypt(input_str: str) -> bytes:
    """Encode input to UTF-8 and truncate to bcrypt's 72-byte limit."""
    return input_str.encode("utf-8")[:MAX_BCRYPT_BYTES]


def hash_password(password: str) -> str:
    password_bytes = _truncate_to_bcrypt(password)
    # passlib accepts bytes; providing truncated bytes prevents the
    # underlying bcrypt implementation from raising on >72 bytes.
    return pwd_context.hash(password_bytes)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    password_bytes = _truncate_to_bcrypt(plain_password)
    return pwd_context.verify(password_bytes, hashed_password)