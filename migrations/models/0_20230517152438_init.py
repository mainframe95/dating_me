from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "admin" (
    "id" CHAR(36) NOT NULL  PRIMARY KEY,
    "username" VARCHAR(60),
    "firstname" VARCHAR(50),
    "lastname" VARCHAR(50),
    "email" VARCHAR(255) NOT NULL,
    "access" VARCHAR(255) NOT NULL,
    "pwd" VARCHAR(255),
    "salt" VARCHAR(255),
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "gender" (
    "id" CHAR(36) NOT NULL  PRIMARY KEY,
    "label" VARCHAR(10) NOT NULL,
    "is_actived" INT NOT NULL  DEFAULT 0,
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "member" (
    "id" CHAR(36) NOT NULL  PRIMARY KEY,
    "username" VARCHAR(60),
    "firstname" VARCHAR(50),
    "lastname" VARCHAR(50),
    "email" VARCHAR(255) NOT NULL,
    "tel" VARCHAR(20) NOT NULL,
    "pwd" VARCHAR(255),
    "salt" VARCHAR(255),
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "gender_id" CHAR(36) NOT NULL REFERENCES "gender" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "hangon" (
    "id" CHAR(36) NOT NULL  PRIMARY KEY,
    "is_actived" INT NOT NULL  DEFAULT 1,
    "created_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMP NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "first_member_id" CHAR(36) NOT NULL REFERENCES "member" ("id") ON DELETE CASCADE,
    "second_member_id" CHAR(36) NOT NULL REFERENCES "member" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "team" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "tournament" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS "event" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "name" TEXT NOT NULL,
    "tournament_id" INT NOT NULL REFERENCES "tournament" ("id") ON DELETE CASCADE
);
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(100) NOT NULL,
    "content" JSON NOT NULL
);
CREATE TABLE IF NOT EXISTS "event_team" (
    "event_id" INT NOT NULL REFERENCES "event" ("id") ON DELETE CASCADE,
    "team_id" INT NOT NULL REFERENCES "team" ("id") ON DELETE CASCADE
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
