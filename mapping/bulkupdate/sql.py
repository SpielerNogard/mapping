device_table = """CREATE TABLE `devices` (
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `name` TEXT,
    `ip` TEXT,
    `port` INTEGER,
    `arch` INTEGER,
    `pd_version` TEXT,
    `pogo_version` TEXT
);"""
