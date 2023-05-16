import multiprocessing

# Gunicorn configuration

# Bind the application to this host:port
bind = "0.0.0.0:8000"

# Number of worker processes
workers = multiprocessing.cpu_count() * 2 + 1

# Maximum number of simultaneous client connections
# You can adjust this value based on your needs
# Recommended formula: workers * 2 + 1
worker_connections = 1000

# Set the maximum number of requests a worker will process before restarting
# This helps prevent memory leaks
max_requests = 5000

# Set the maximum number of requests a worker will process before graceful restart
# This helps with long-running applications that may have memory leaks
max_requests_jitter = 500

# Set the timeout for graceful workers restart
timeout = 60

# Set the log level (debug, info, warning, error, critical)
loglevel = "info"

# Path to access log file
accesslog = "-"

# Path to error log file
errorlog = "-"

# Enable/disable Gunicorn's daemon mode
daemon = False
