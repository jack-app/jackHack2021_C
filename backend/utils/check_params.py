def check_params(params, want_params):
    if params is None:
        return False
    return set(want_params).issubset(params)
