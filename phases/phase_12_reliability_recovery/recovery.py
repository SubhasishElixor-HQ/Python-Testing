def retry_with_limit(operation, max_attempts: int):
    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1")

    last_error = None
    for _ in range(max_attempts):
        try:
            return operation()
        except (TimeoutError, ConnectionError) as exc:
            last_error = exc

    raise RuntimeError("operation failed after retries") from last_error
