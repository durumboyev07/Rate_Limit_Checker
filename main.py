import time

requests = {}

while True:
    ip = input("IP: ")
    now = time.time()

    if ip not in requests:
        requests[ip] = []

    requests[ip] = [t for t in requests[ip] if now - t < 10]

    if len(requests[ip]) >= 3:
        print("Blocked")
    else:
        requests[ip].append(now)
        print("Allowed")
