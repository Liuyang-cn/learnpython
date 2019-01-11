#config.py

configs = config_default.configs

try:
    import config_override
    configs = merge(configs, config_override.congigs)
except ImportError:
    pass