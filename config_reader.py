def load_config(file_path):
    config = {}
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, value = line.split("=", 1)

            dict_key = key.strip()
            if dict_key in ['PORT', 'TESTCOUNT']:
                config[dict_key] = int(value.strip())
                continue

            config[dict_key] = value.strip()
    return config
