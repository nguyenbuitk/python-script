import logging
import os


def is_having_vpn_connection(environment):
    rancher_main_address = 'rancher-main.{}.myovcloud.com'.format(environment)
    response = os.system("ping -c 1 -w2 " + rancher_main_address + " > /dev/null 2>&1")
    if response == 0:
        return True
    else:
        return False
        
def setup_logger(name, is_verbose):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    """setup logger
    """
    formatter = logging.Formatter('%(message)s')
    # console
    ch = logging.StreamHandler()
    if is_verbose:
        ch.setLevel(logging.DEBUG)
    else:
        ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # file
    fh = logging.FileHandler(name + '.log')
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger
    
def yes_or_no(question):
    reply = str(raw_input(question+' (y/n): ')).lower().strip()
    if reply[:1] == 'y':
        return True
    if reply[:1] == 'n':
        return False
    else:
        return yes_or_no("Please enter valid value")
        
def count_license(licenses):
	# Countable devices
	"""
	deviceCodeName = [
		"OVCLD-SWEDGE",
		"OVCLD-SWADV",
		"OVCLD-SWCORE",
		"OVCLD-APBASE",
		"OVCLD-APADV"
	]
	"""
	ignoreLicenses = [
		"OVCLD-BYOD",
		"OVCLD-GA"
	]
	
	# Counter
	c = 0
	if not licenses:
		ValueError("dlLicenses is corrupted")

	for l in licenses:
		if l["units"]:
			for l2 in l["units"]:
				if l2["maxCount"] and l2["unitId"] not in ignoreLicenses:
					c += int(l2["maxCount"])
	return c

def count_AP_license(licenses):
	# Countable devices
	"""
	deviceCodeName = [
		"OVCLD-SWEDGE",
		"OVCLD-SWADV",
		"OVCLD-SWCORE",
		"OVCLD-APBASE",
		"OVCLD-APADV"
	]
	"""
	ignoreLicenses = [

        "OVCLD-SWESSENTIAL",
        "OVCLD-SWCORE",
        "OVCLD-SWADV",
		"OVCLD-BYOD",
		"OVCLD-GA"
	]
	
	# Counter
	c = 0
	if not licenses:
		ValueError("dlLicenses is corrupted")

	for l in licenses:
		if l["units"]:
			for l2 in l["units"]:
				if l2["maxCount"] and l2["unitId"] not in ignoreLicenses:
					c += int(l2["maxCount"])
	return c

def count_ADV_license(licenses):
	# Countable devices
	"""
	deviceCodeName = [
		"OVCLD-SWEDGE",
		"OVCLD-SWADV",
		"OVCLD-SWCORE",
		"OVCLD-APBASE",
		"OVCLD-APADV"
	]
	"""
	ignoreLicenses = [

        "OVCLD-SWESSENTIAL",
        "OVCLD-SWCORE",
        "OVCLD-STELLAR-AP",
		"OVCLD-BYOD",
		"OVCLD-GA"
	]
	
	# Counter
	c = 0
	if not licenses:
		ValueError("dlLicenses is corrupted")

	for l in licenses:
		if l["units"]:
			for l2 in l["units"]:
				if l2["maxCount"] and l2["unitId"] not in ignoreLicenses:
					c += int(l2["maxCount"])
	return c

def count_ESS_license(licenses):
	# Countable devices
	"""
	deviceCodeName = [
		"OVCLD-SWEDGE",
		"OVCLD-SWADV",
		"OVCLD-SWCORE",
		"OVCLD-APBASE",
		"OVCLD-APADV"
	]
	"""
	ignoreLicenses = [

        "OVCLD-STELLAR-AP",
        "OVCLD-SWCORE",
        "OVCLD-SWADV",
		"OVCLD-BYOD",
		"OVCLD-GA"
	]
	
	# Counter
	c = 0
	if not licenses:
		ValueError("dlLicenses is corrupted")

	for l in licenses:
		if l["units"]:
			for l2 in l["units"]:
				if l2["maxCount"] and l2["unitId"] not in ignoreLicenses:
					c += int(l2["maxCount"])
	return c

def count_CORE_license(licenses):
	# Countable devices
	"""
	deviceCodeName = [
		"OVCLD-SWEDGE",
		"OVCLD-SWADV",
		"OVCLD-SWCORE",
		"OVCLD-APBASE",
		"OVCLD-APADV"
	]
	"""
	ignoreLicenses = [

        "OVCLD-SWESSENTIAL",
        "OVCLD-STELLAR-AP",
        "OVCLD-SWADV",
		"OVCLD-BYOD",
		"OVCLD-GA"
	]
	
	# Counter
	c = 0
	if not licenses:
		ValueError("dlLicenses is corrupted")

	for l in licenses:
		if l["units"]:
			for l2 in l["units"]:
				if l2["maxCount"] and l2["unitId"] not in ignoreLicenses:
					c += int(l2["maxCount"])
	return c
