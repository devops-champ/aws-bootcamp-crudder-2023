from datetime import datetime, timedelta, timezone
import logging

from lib.db import db

class HomeActivities:
  def run(cognito_user_id=None): #added (Logger) to view logs in cloudwatch
    #Logger.info("HomeActivities")
    #now = datetime.now(timezone.utc).astimezone()

    results = db.query_array_json("""
      SELECT
        activities.uuid,
        users.display_name,
        users.handle,
        activities.message,
        activities.replies_count,
        activities.reposts_count,
        activities.likes_count,
        activities.reply_to_activity_uuid,
        activities.expires_at,
        activities.created_at
      FROM public.activities
      LEFT JOIN public.users ON users.uuid = activities.user_uuid
      ORDER BY activities.created_at DESC
    """)

    return results  