#!/usr/bin/env python3

import datetime
import hashlib

epoch = datetime.datetime(2020, 1, 1)
year_in_secs = 60*60*24*365

def dob_generator(account, service="", minyears=18):
	id = account+service

	s_epoch = int(epoch.timestamp())
	s_max = s_epoch - (minyears * year_in_secs)
	s_min = s_max - (60 * year_in_secs)

	hash = hashlib.sha512(id.encode()).hexdigest()
	hash_val = int(hash, base=16)
	s_notrandom = hash_val % (s_max-s_min)

	return datetime.date.fromtimestamp(s_min + s_notrandom)

print(dob_generator("me@example.com","twitter"))
