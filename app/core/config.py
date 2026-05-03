from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AmeriKash Agent System"
    app_version: str = "0.1.0"
    database_url: str = "sqlite:///./amerikash.db"
    audit_log_path: str = "audit_log.jsonl"
    password_hash_iterations: int = 210_000

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
