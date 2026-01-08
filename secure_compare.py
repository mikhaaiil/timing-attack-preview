import hmac
import hashlib
import random
import time


def secure_compare_hmac(a: str, b: str) -> bool:
    return hmac.compare_digest(a.encode(), b.encode())


def secure_compare_hash(a: str, b: str) -> bool:
    hash_a = hashlib.sha256(a.encode()).hexdigest()
    hash_b = hashlib.sha256(b.encode()).hexdigest()
    return hash_a == hash_b


def compare_with_random_delay(a: str, b: str) -> bool:
    result = (a == b)
    time.sleep(random.uniform(0.01, 0.03))
    return result


if __name__ == "__main__":
    secret = "supersecret123"
    user_input = "supersecret123"

    print(f"HMAC comparison: {secure_compare_hmac(user_input, secret)}")
    print(f"Хэш-comparison: {secure_compare_hash(user_input, secret)}")

    print(f"With random delay: {compare_with_random_delay(user_input,
                                                          secret)}")
