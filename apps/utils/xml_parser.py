import xmltodict
import urllib2
import json

def parse_xml(url):
    url = 'http://108.163.217.230:2000/sms_integration/GetAttendanceData.aspx?\
            CharAction=Detail&Passwd=wolcott123456&SiteID=71&ShiftDoneDate=14-01-2016'
    page = urllib2.urlopen(url)
    data = page.read()
    page.close()
    data = xmltodict.parse(data)
    return json.dumps(data)
