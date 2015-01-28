import urllib2, re

spc = (('&#192;','A'),	('&#193;','A'),	('&#194;','A'),	('&#195;','A'),	('&#196;','A'),	('&#199;','C'),	('&#200;','E'),	('&#201;','E'), ('&#198;','AE'),
	('&#202;','E'),	('&#203;','E'),	('&#204;','I'),	('&#205;','I'),	('&#207;','I'),	('&#217;','U'),	('&#218;','U'),	('&#220;','U'),
	('&#219;','U'),	('&#224;','a'),	('&#225;','a'),	('&#226;','a'),	('&#227;','a'),	('&#228;','a'),	('&#231;','c'),	('&#232;','e'),
	('&#233;','e'),	('&#234;','e'),	('&#235;','e'),	('&#236;','i'),	('&#237;','i'),	('&#238;','i'),	('&#239;','i'),	('&#242;','o'),
	('&#243;','o'),	('&#244;','o'),	('&#245;','o'),	('&#249;','u'),	('&#250;','u'),	('&#251;','u'),	('&#252;','u'),	('&#221;','Y'),	('&#253;','y'))

def html_replace_clean(s):
	s = cleanHtml(s)
	for code,caracter in spc: s = s.replace(code,caracter)
	return s

def abrir_url(url):
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link

def cleanHtml(dirty):
    clean = re.sub('&quot;', '\"', dirty)
    clean = re.sub('&#039;', '\'', clean)
    clean = re.sub('&#215;', 'x', clean)
    clean = re.sub('&#038;', '&', clean)
    clean = re.sub('&#8216;', '\'', clean)
    clean = re.sub('&#8217;', '\'', clean)
    clean = re.sub('&#8211;', '-', clean)
    clean = re.sub('&#8220;', '\"', clean)
    clean = re.sub('&#8221;', '\"', clean)
    clean = re.sub('&#8212;', '-', clean)
    clean = re.sub('&amp;', '&', clean)
    clean = re.sub("`", '', clean)
    clean = re.sub('<em>', '[I]', clean)
    clean = re.sub('</em>', '[/I]', clean)
    return clean