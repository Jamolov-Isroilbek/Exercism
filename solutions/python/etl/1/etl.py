def transform(legacy_data):
    return {item.lower(): key for key, value in legacy_data.items() for item in value}
