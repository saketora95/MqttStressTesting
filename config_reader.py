def load_config(file_path):
    config = {}
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):  # 忽略空行或註解行
                continue
            key, value = line.split("=", 1)
            config[key.strip()] = value.strip()
    return config
