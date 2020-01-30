#!/usr/bin/env python
import dns.resolver

domain = input('Please input an domain: ')

A = dns.resolver.query(domain, 'A')
for i in A.response.answer:
    for j in i:
        if j.rdtype == 1:
            print(j.address)
