celery -A celery_app worker --loglevel=info

celery beat -A celery_app

-OR-


$ celery -B -A celery_app worker --loglevel=info
