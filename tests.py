def log_request (req: 'flask_request', res: str) -> None:
    with open('log.txt', 'r+') as log:
        print (req+ ' '+res, file=log)