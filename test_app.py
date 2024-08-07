import threading
import time
from redis import Redis
import requests
from app import convert, main
import traceback

redis = Redis(host='127.0.0.1', port=6379, db=0)

def test_convert_span():
    message = b'\xef\x10\x00(\x18\x19xytb-uw-pt-7d876c8d-7vjg6\x18\x0beurus-uw-pt\x16\xc8\x96\xbd\x80\xe1a\x18D\x00\x1atyjygl-pt-uap\xfc\xf8\xf8\x92\xf10Tmesos-b9978739-070d-4056-83e5-a27c49d69e86\xaf\xae\xe9\x06\x18 e246fc1cfb4c428eb744a76cf996d10c&\xbc\x92\xc3\xe1\xd5\xbd\xb5\xe9\xc7\x01\x16\xf2\xc8\x92\xdb\xfd\xb6\xee\xb4\x8a\x01\x16\xa0\xb9\xb9\xe5\xe4a\x15\x80\x1f\x18\x19/eurus-uw/gateway/request\x14\xe4\x0f\x18\x10140.2.1.53:31003\x18\n140.2.1.11$\x00)<v\xbc\x92\xc3\xe1\xd5\xbd\xb5\xe9\xc7\x01\x15T\x15\xfa\x1e\x15\x04$\x90N\xd5\xe7\x9b\xf2\x97\x07\x00v\xbc\x92\xc3\xe1\xd5\xbd\xb5\xe9\xc7\x01\x15\x06\x15\x04\x15\xfc\x1e$\xf6N\xd5\xf1\xe1\xfd\x90\x05\x00v\xbc\x92\xc3\xe1\xd5\xbd\xb5\xe9\xc7\x01\x15\x00\x15\x02\x15\xfe\x1e$\xe6\x0f),\x15\\\x1c5\x90\x03\x00\x00\x15\xd4\x07\x1c\x18\x04POST\x00\x00\x15\x02\xa5\xd4\xe3\xda\x92\x07\x00\x18\rtyjygl-pt-uap\x14\xf4\x12\x18\x10140.2.1.53:31003E\x93\xaa\x88\x93\nT\xf4\x128\x04POST\x18\xa4\x0bx-real-ip,10.186.6.10;x-forwarded-for,10.186.6.10,10.186.6.10;x-forwarded-proto,http,http;x-forwarded-host,10.182.15.231:80,10.182.15.231;x-forwarded-port,12000,80;x-original-uri,/uw-non/gatewayapi;x-scheme,http;x-original-url,http://10.182.15.231:80/uw-non/gatewayapi;x-original-method,POST;content-length,4306;content-type,application/json; charset=UTF-8;routefild,reqOrganizationNo;routefildvalue,00000000000017;user-agent,Apache-HttpClient/4.5.2 (Java/1.8.0_121);accept-encoding,gzip,deflate;apptrace-traceid,tyjygl-pt-uap^1679640378492^mesos-b9978739-070d-4056-83e5-a27c49d69e86^14309167;apptrace-spanid,7199403087043781790;apptrace-pspanid,4986853524549816889;apptrace-flags,0;apptrace-pappname,tyjygl-pt-uap;apptrace-papptype,1210;pagentid,mesos-b9978739-070d-4056-83e5-a27c49d69e86;tsf-tags,%5B%7B%22k%22%3A%22tsf-gateway-ratelimit-context%22%2C%22v%22%3A%22grp-jbw21loe%22%2C%22f%22%3A%5B%5D%7D%5D;tsf-metadata,%7B%22ai%22%3A%22application-9maexny3%22%2C%22av%22%3A%2220211130v1%22%2C%22sn%22%3A%22xytb-gateway-pt%22%2C%22ii%22%3A%22xytb-gateway-pt-6c85b49f4f-2djnf%22%2C%22gi%22%3A%22group-qby8gmak%22%2C%22li%22%3A%22140.2.1.11%22%2C%22ni%22%3A%22namespace-z5yrloyj%22%7D;forwarded,proto=http;host="10.182.15.231:80";for="10.186.6.10:30484";x-forwarded-prefix,/uw-non/busi-biz-ns-pt/eurus-uw;x-b3-traceid,1d5b4afa2dd865a4;x-b3-spanid,fe4830ce06e18229;x-b3-parentspanid,1d5b4afa2dd865a4;x-b3-sampled,1;host,140.2.1.53:31003;accept,*/*\x18(Apache-HttpClient/4.5.2 (Java/1.8.0_121)\x18\xd2!1199008D42023/03/2811:51:00                                                                          1  1  1<?xml version="1.0" encoding="UTF-8"?><root documentation="\xe4\xb8\xad\xe5\x9b\xbd\xe5\xa4\xaa\xe5\xb9\xb3\xe6\xb4\x8b\xe4\xba\xba\xe5\xaf\xbf\xe4\xbf\x9d\xe9\x99\xa9\xe8\x82\xa1\xe4\xbb\xbd\xe6\x9c\x89\xe9\x99\x90\xe5\x85\xac\xe5\x8f\xb820230328"><app_node><base_info_node app_type="E" sale_type="09" sub_sale_type="17" mnum="1" distributor_code="JINY4717" distributor_name="test" distributor_tel="13062099798" sale_channel="10" app_no="eKrFIst700t7000" digital_sign="1" bill_send_type="0" assign_issue="1" issue_date="2023-03-29" submit_date="" rec_date="" pay_by_wn="0" is_fdg="0" csr_area_code="SHJ03010000000000000" producttype="" padno="" customerid="" bsnss_no="" conflag="" o_policyno="" base_no="" invoice_type="0" paytime="" is_sync="1" social_security="1" audit_flag="0" device_type="3" client_source="1" charg_no="" double_record="0"/><owner_node><cust_info_node birthdate="1971/06/10" gender="2" occupation_code="0001001" id="230102197106101508" id_type="0" id_2="" id_start_date="2022-11-26" id_expire_date="2042-11-26" last_name="" first_name="\xe7\x8e\x8b\xe4\xb8\x80" marital_status="2" nationality="CN" salary="10000" resident_country="CN" birth_erea="\xe6\xb2\xb3\xe5\x8c\x97\xe7\x9c\x81" clm_ind="0"/><address_set_node><address_node address_type="1" address_state="000000000000001006" address_city="000000000000001007" address_county="000000000000001340" address_street="\xe4\xb8\x96\xe7\x95\x8c\xe4\xb9\x8b\xe7\xaa\x97123\xe5\x8f\xb7" address_line1="\xe6\xb2\xb3\xe5\x8c\x97\xe7\x9c\x81\xe7\x9f\xb3\xe5\xae\xb6\xe5\xba\x84\xe5\xb8\x82\xe6\xad\xa3\xe5\xae\x9a\xe5\x8e\xbf\xe4\xb8\x96\xe7\x95\x8c\xe4\xb9\x8b\xe7\xaa\x97123\xe5\x8f\xb7"/></address_set_node><telecomm_set_node><telecomm_node phone_type="3" phone_number="18514644916"/></telecomm_set_node><email_set_node><email_node email="" notice_flag="1"/></email_set_node><account_set_node><account_node account_type="" account_name="" account_bankcode="" account_no="" account_draft=""/></account_set_node><tax_set_node><tax_node tax_type="01" tax_last_name="\xe4\xb8\x80" tax_first_name="\xe7\x8e\x8b" tax_natly="" tax_brth_area="" tax_brth_city="" tax_first_name_en=""/></tax_set_node></owner_node><relationship_node relationship_code="301"/><insured_node><cust_info_node birthdate="1971/06/10" gender="2" occupation_code="0001001" id="230102197106101508" id_type="0" id_2="" id_start_date="2022-11-26" id_expire_date="2042-11-26" last_name="" first_name="\xe7\x8e\x8b\xe4\xb8\x80" marital_status="2" nationality="CN" salary="10000" resident_country="CN" birth_erea="\xe6\xb2\xb3\xe5\x8c\x97\xe7\x9c\x81" identity_chk_date="2023/03/28" identity_chk_source="01" identity_chk_desc="\xe6\x97\xa0\xe9\x9c\x80\xe6\xa0\xa1\xe9\xaa\x8c\xef\xbc\x9a\xe6\x9c\xaa\xe6\x8e\x88\xe6\x9d\x83" identity_chk_ind="" clm_ind="0"/><address_set_node><address_node address_type="1" address_state="000000000000001006" address_city="000000000000001007" address_county="000000000000001340" address_street="\xe4\xb8\x96\xe7\x95\x8c\xe4\xb9\x8b\xe7\xaa\x97123\xe5\x8f\xb7" address_line1="\xe6\xb2\xb3\xe5\x8c\x97\xe7\x9c\x81\xe7\x9f\xb3\xe5\xae\xb6\xe5\xba\x84\xe5\xb8\x82\xe6\xad\xa3\xe5\xae\x9a\xe5\x8e\xbf\xe4\xb8\x96\xe7\x95\x8c\xe4\xb9\x8b\xe7\xaa\x97123\xe5\x8f\xb7"/></address_set_node><telecomm_set_node><telecomm_node phone_type="3" phone_number="18514644916"/></telecomm_set_node><email_set_node><email_node email="" notice_flag="1"/></email_set_node><tax_set_node><tax_node tax_type="01" tax_last_name="\xe4\xb8\x80" tax_first_name="\xe7\x8e\x8b" tax_natly="" tax_brth_area="" tax_brth_city="" tax_first_name_en=""/></tax_set_node></insured_node><beneficiary_set_node bnfcry_code="4"/><payment_node first_payment_method="7" payment_method="7" payment_amount="10000.00"/><coverage_set_node><coverage_node cvrg_code="44643200" cvrg_type="1" cvrg_ppp="20" cvrg_bp="whl_life" bllng_frequency="13" cvrg_unit="1.000000" cvrg_prem="10000" cvrg_sa="126465" cvrg_auto="" nfo_type="0" cupu_pymnt_freq="" base_sa=""/></coverage_set_node><underwriting_set_node><customer_uw_node who="1" salary="10000" height="155" weight="45"/><customer_uw_node who="2" salary="10000" height="155" weight="45"/><uw_node qc="43" oa="N" oc="" ia="Y" ic=""/><uw_node qc="1" oa="N" oc="" ia="N" ic=""/><uw_node qc="46" oa="N" oc="" ia="N" ic=""/><uw_node qc="175" oa="N" oc="" ia="N" ic=""/><uw_node qc="58" oa="N" oc="" ia="N" ic=""/><uw_node qc="5" oa="N" oc="" ia="N" ic=""/><uw_node qc="6" oa="N" oc="" ia="N" ic=""/><uw_node qc="39" oa="N" oc="" ia="N" ic=""/><uw_node qc="90" oa="N" oc="" ia="N" ic=""/><uw_node qc="136" oa="N" oc="" ia="N" ic=""/><uw_node qc="8" oa="N" oc="" ia="N" ic=""/><uw_node qc="9" oa="N" oc="" ia="N" ic=""/><uw_node qc="218" oa="N" oc="" ia="N" ic=""/></underwriting_set_node><special_clause_set_node><special_clause_node special_coverage="44643200" special_content=""/></special_clause_set_node><bnft_set_node/></app_node></root>\x18\x97\x011199008EH2023/03/2811:51:020000000                                                                 1  1  1  0127003\xe4\xba\xa4\xe6\x98\x93\xe6\x88\x90\xe5\x8a\x9f\xef\xbc\x8c\xe7\x94\xb5\xe8\x84\x91\xe6\xa0\xb8\xe4\xbf\x9d\xe9\x80\x9a\xe8\xbf\x87\xe3\x80\x82\x14\x90\x038*mesos-b9978739-070d-4056-83e5-a27c49d69e86\x18\x16Tomcat Servlet ProcessH\x0beurus-uw-pt\x18 e246fc1cfb4c428eb744a76cf996d10c\x00\n'
    lines = convert(redis, message)
    assert lines[0].tags['service'] == 'eurus-uw-pt'

# test send span chunk
def test_convert_span_chunk():
    message = b"\xef\x10\x00F\x18*mesos-374b3b23-a493-4be1-b94d-9416b0ee6e3d\x18\x06cbpt-1\x16\xb8\x9b\x94\xc3\xe1a\x14\xe4\x0f\x18\x12\x00\x0ccbpt-1\xdc\x8d\xca\xe1\xf00\x01\x93\x97\x08\x18 e246fc1cfb4c428eb744a76cf996d10c&\x9a\xf3\xdf\xe0\x8b\xcf\xaa\x8e2\x18\x1210.186.68.64:31001\x19\xfc\x14\x85\xf0\x03\x15r\x15\x02$\x9eO5\x14\xa5\xa9\xac\xab\x9d\x0b\x00\x85\xee\x03\x15r\x15\x02$\x9eO5\x12\xa5\x93\xa3\xd5\xf9\x0f\x00\x85\xfe\x03\x15v4\xfa#\x18\x1029.23.122.1:1521%\x1cX\x04ffdbU\xa0\x87\xa7\xdb\x0e\xfc\x18'jdbc:oracle:thin:@29.23.122.1:1521:ffdb\x18\x06ORACLE\x18\x04ffdb8(1f574af74e3acc575f29301360a43dfc75b3b214\x18\x0f999999,999999,2\x18\x12110227199106171607(/oracle.jdbc.driver.OracleResultSetImpl@1e55e084&\xf6\x9c\xbd\xe5\xe4a\x16\x00\x00\x00\x85\xfc\x03\x15t\x15\x02$\x9eO5\x1a\xa5\xa9\xac\xab\x9d\x0b\x00\x85\x82\x04\x15x4\xfa#\x18\x1029.23.122.1:1521%\x1cX\x04ffdbU\xa0\x87\xa7\xdb\x0e\xfc\x18'jdbc:oracle:thin:@29.23.122.1:1521:ffdb\x18\x06ORACLE\x18\x04ffdb8(42113a84e3182c3ff148949b168f43e2a75e9c95\x18\x0f999999,999999,2\x18\x12110227199106171607(/oracle.jdbc.driver.OracleResultSetImpl@7317c53c&\xf8\x9c\xbd\xe5\xe4a\x16\x00\x00\x00\x85\x80\x04\x15v\x15\x02$\x9eO5\x1a\xa5\xa9\xac\xab\x9d\x0b\x00\x85\xfa\x03\x15t\x15\x04$\x9eO5\x18\xa5\x84\x9a\xe9\xa2\x02\x00\x85\x88\x04\x15z4\xfa#\x18\x1029.23.122.1:1521%\x1cX\x04ffdbU\xa0\x87\xa7\xdb\x0e\xfc\x18'jdbc:oracle:thin:@29.23.122.1:1521:ffdb\x18\x06ORACLE\x18\x04ffdb8(d8601497ea3642ec76811b42893250d2ead331b9\x18\x012\x18\x12110227199106171607(/oracle.jdbc.driver.OracleResultSetImpl@7f3b5d77&\xfa\x9c\xbd\xe5\xe4a\x16\x00\x00\x00\x85\x86\x04\x15x\x15\x04$\x9eO5\x1a\xa5\xa9\xac\xab\x9d\x0b\x00\x85\x84\x04\x15x\x15\x04$\x9eO5\x18\xa5\xb9\x92\x9c\xa3\x03\x00\x85\xf8\x03\x15t\x15\x08$\x9eO5\x16\xa5\x84\xee\xbd\xe1\x0e\x00\x85\x90\x04\x15|\x15\x02$\xfa#\x18\x1029.23.122.1:1521%\x1cX\x04ffdbU\xa0\x87\xa7\xdb\x0e\xfc\x18'jdbc:oracle:thin:@29.23.122.1:1521:ffdb\x18\x06ORACLE\x18\x04ffdb8(1f574af74e3acc575f29301360a43dfc75b3b214\x18\x0f999999,999999,2\x18\x0f110227910617160(/oracle.jdbc.driver.OracleResultSetImpl@14249c55&\xfc\x9c\xbd\xe5\xe4a\x16\x02\x00\x00\x85\x8e\x04\x15|\x15\x02$\x9eO5\x1a\xa5\xa9\xac\xab\x9d\x0b\x00\x85\x94\x04\x15\x80\x014\xfa#\x18\x1029.23.122.1:1521%\x1cX\x04ffdbU\xa0\x87\xa7\xdb\x0e\xfc\x18'jdbc:oracle:thin:@29.23.122.1:1521:ffdb\x18\x06ORACLE\x18\x04ffdb8(42113a84e3182c3ff148949b168f43e2a75e9c95\x18\x0f999999,999999,2\x18\x0f110227910617160(/oracle.jdbc.driver.OracleResultSetImpl@21b5ca26&\x80\x9d\xbd\xe5\xe4a\x16\x00\x00\x00\x85\x92\x04\x15~\x15\x02$\x9eO5\x1a\xa5\xa9\xac\xab\x9d\x0b\x00\x85\x8c\x04\x15|\x15\x04$\x9eO5\x18\xa5\x84\x9a\xe9\xa2\x02\x00\x85\x9a\x04\x15\x82\x014\xfa#\x18\x1029.23.122.1:1521%\x1cX\x04ffdbU\xa0\x87\xa7\xdb\x0e\xfc\x18'jdbc:oracle:thin:@29.23.122.1:1521:ffdb\x18\x06ORACLE\x18\x04ffdb8(d8601497ea3642ec76811b42893250d2ead331b9\x18\x012\x18\x0f110227910617160(/oracle.jdbc.driver.OracleResultSetImpl@7492ac27&\x82\x9d\xbd\xe5\xe4a\x16\x00\x00\x00\x85\x98\x04\x15\x80\x01\x15\x02$\x9eO5\x1a\xa5\xa9\xac\xab\x9d\x0b\x00\x85\x96\x04\x15\x80\x01\x15\x02$\x9eO5\x18\xa5\xb9\x92\x9c\xa3\x03\x00\x85\x8a\x04\x15|\x15\x06$\x9eO5\x16\xa5\x84\xee\xbd\xe1\x0e\x00\x14\xe4\x0f\x18\x06cbpt-1\x18 e246fc1cfb4c428eb744a76cf996d10c&\x9a.\x18\x17http-bio-31001-exec-725\x00\n"
    lines = convert(redis, message)
    assert lines[0].tags['service'] == 'cbpt-1'

# read a line from messages file
def read_line(f):
    line = b""
    delimiter = b"topic=SpanTopic |"
    while True:
        b = f.read(1)
        if b == b"":
            break
        line += b
        if b == b"|" and line.endswith(delimiter):
            line = line[:-len(delimiter)]
            if line == b"":
                continue
            return line

def _test_print_messages():
    with open('./pinpoint-topic.msg', 'rb') as f:
        i = 0
        while i <= 2:
            line = read_line(f)
            print(str(line) + "\n---\n")
            i += 1

def _test_batch_send_message():
    with open('./pinpoint-topic.msg', 'rb') as f:
        i = 0
        while i <= 1:
            message = read_line(f)
            try:
                assert convert(redis, message).applicationName == 'applicationName'
            except Exception as e:
                print("Error: {} {}".format(str(e), traceback.format_exc()))
                continue
            i += 1

def test_handle():
    # Start flask server
    thread = threading.Thread(target=main)
    thread.start()

    # wait for flask server to start
    time.sleep(1)

    # send message to flask server
    with open('./pinpoint-topic.msg', 'rb') as f:
        i = 0
        while i <= 1:
            message = read_line(f)
            try:
                res = requests.post('http://localhost:8080', data=message)
                assert res.status_code == 200
            except Exception as e:
                print("Error: {} {}".format(str(e), traceback.format_exc()))
                continue
            i += 1
