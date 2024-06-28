from app.dependencies.database import get_sync_db, get_async_db

# Synchronous database dependency
def get_db():
    return get_sync_db()

# Asynchronous database dependency
async def get_async_db():
    return get_async_db()
