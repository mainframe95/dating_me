ORM_MIGRATION_SQLITE = {
    "connections": {
        "default": "sqlite://data.db",
    },
    "apps": {
        "models": {
            "models": [
                "models",
                "aerich.models"],
            "default_connection": "default",
        },
    },
}

# TORTOISE_ORM = {
#     "connections": {"default": "mysql://root:123456@127.0.0.1:3306/test"},
#     "apps": {
#         "models": {
#             "models": ["tests.models", "aerich.models"],
#             "default_connection": "default",
#         },
#     },
# }