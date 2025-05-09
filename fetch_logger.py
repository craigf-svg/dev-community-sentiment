from datetime import datetime, timezone
from models import db, FetchLog


def log_fetch_result(post_list, success_count, skipped_count):
    current_timestamp_utc = datetime.now(timezone.utc)
    print('fetch logger')
    print('skipped_count ', skipped_count)
    print('success_count ', success_count)
    print('current_timestamp ', current_timestamp_utc)
    try:
        log = FetchLog(
            created_at_utc=current_timestamp_utc,
            inserted_post_count=success_count,
            skipped_duplicate_post_count=skipped_count,
            duration_seconds=20,
            status='success'
        )
        db.session.add(log)
        db.session.commit()
        print('Fetch log successfully inserted!')
    except Exception as e:
        db.session.rollback()
        print(f"Fetch Error: {e}")
