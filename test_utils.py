from utils import  extract_trace_id
from pinpoint_parser import xid

def test_extract_trace_id():
    assert extract_trace_id('x-real-ip,10.186.6.10;x-forwarded-for,10.186.6.10,10.186.6.10;x-forwarded-proto,http,http;x-forwarded-host,10.182.15.231:80,10.182.15.231;x-forwarded-port,12000,80;x-original-uri,/uw-non/gatewayapi;x-scheme,http;x-original-url,http://10.182.15.231:80/uw-non/gatewayapi;x-original-method,POST;content-length,4306;content-type,application/json; charset=UTF-8;routefild,reqOrganizationNo;routefildvalue,00000000000017;user-agent,Apache-HttpClient/4.5.2 (Java/1.8.0_121);accept-encoding,gzip,deflate;apptrace-traceid,tyjygl-pt-uap^1679640378492^mesos-b9978739-070d-4056-83e5-a27c49d69e86^14309167;apptrace-spanid,7199403087043781790;apptrace-pspanid,4986853524549816889;apptrace-flags,0;apptrace-pappname,tyjygl-pt-uap;apptrace-papptype,1210;pagentid,mesos-b9978739-070d-4056-83e5-a27c49d69e86;tsf-tags,%5B%7B%22k%22%3A%22tsf-gateway-ratelimit-context%22%2C%22v%22%3A%22grp-jbw21loe%22%2C%22f%22%3A%5B%5D%7D%5D;tsf-metadata,%7B%22ai%22%3A%22application-9maexny3%22%2C%22av%22%3A%2220211130v1%22%2C%22sn%22%3A%22xytb-gateway-pt%22%2C%22ii%22%3A%22xytb-gateway-pt-6c85b49f4f-2djnf%22%2C%22gi%22%3A%22group-qby8gmak%22%2C%22li%22%3A%22140.2.1.11%22%2C%22ni%22%3A%22namespace-z5yrloyj%22%7D;forwarded,proto=http;host="10.182.15.231:80";for="10.186.6.10:30484";x-forwarded-prefix,/uw-non/busi-biz-ns-pt/eurus-uw;x-b3-traceid,1d5b4afa2dd865a4;x-b3-spanid,fe4830ce06e18229;x-b3-parentspanid,1d5b4afa2dd865a4;x-b3-sampled,1;host,140.2.1.53:31003;accept,*/*') == '1d5b4afa2dd865a4'

def test_xid():
    buf = b'\x00\x1atyjygl-pt-uap\xfc\xf8\xf8\x92\xf10Tmesos-b9978739-070d-4056-83e5-a27c49d69e86\xaf\xae\xe9\x06'
    tid = xid(buf, "eurus-uw-pt", "xytb-uw-pt-7d876c8d-7vjg6")

    assert tid == 'tyjygl-pt-uap^1679640378492^mesos-b9978739-070d-4056-83e5-a27c49d69e86^14309167'

def test_xid_tuple():
        buf = b'\x00\x1atyjygl-pt-uap\xfc\xf8\xf8\x92\xf10Tmesos-b9978739-070d-4056-83e5-a27c49d69e86\xaf\xae\xe9\x06'
        tid = xid(buf, "eurus-uw-pt", "xytb-uw-pt-7d876c8d-7vjg6")

        (app_id, timestamp, agent_id, sequence) = tid.split('^')
        assert app_id == 'tyjygl-pt-uap'
        assert timestamp == '1679640378492'
        assert agent_id == 'mesos-b9978739-070d-4056-83e5-a27c49d69e86'
        assert sequence == '14309167'
