def poll_wait_for_socket(poll,sock, read=False, write=False):
    if not read and not write:
        raise RuntimeError("poll error")
    mask = 0
    if read:
        mask |= select.POLLIN
    if write:
        mask |= select.POLLOUT
    poll.register(sock, mask)

def dns_check(ip,domain, active=DNS_RESERV):
    if active ==True:
        return str(resolver.query((reversename.from_address(ip)), "PTR")[0]) == domain
    else:
        return True
