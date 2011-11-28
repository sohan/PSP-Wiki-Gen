import mechanize
import cookielib

class Browser:
    def __init__(self):
        br = mechanize.Browser()
        cj = cookielib.LWPCookieJar()
        br.set_cookiejar(cj)

        # Browser options
        br.set_handle_equiv(True)
        br.set_handle_gzip(True)
        br.set_handle_redirect(True)
        br.set_handle_referer(True)
        br.set_handle_robots(False)

        # Follows refresh 0 but not hangs on refresh > 0
        br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

        # Want debugging messages?
        #br.set_debug_http(True)
        #br.set_debug_redirects(True)
        #br.set_debug_responses(True)

        # User-Agent (this is cheating, ok?)
        br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        self.browser = br

    def get_browser(self):
        return self.browser

class MakeWiki:
    def __init__(self):
        self.browser = Browser().get_browser()
        self.curr_response = None
        self.curr_html = None

    def open_page(self, url):
        self.curr_response = self.browser.open(url)
        self.curr_html = self.curr_response.read()

    def login(self, user, passwd):
        self.open_page('http://wiki.phisigmapi.org/pspwiki/index.php?title=Special:Userlogin&returnto=Main_Page')
        self.browser.select_form(name='userlogin')
        self.browser['wpName'] = user
        self.browser['wpPassword'] = passwd
        self.curr_response = self.browser.submit()
        self.curr_html = self.curr_response.read()

    def clean_name(self, name):
        name = '_'.join([p.capitalize() for p in name.split()])
        return name

    def make_template(self, name):
        name = self.clean_name(name)
        self.open_page('http://wiki.phisigmapi.org/pspwiki/index.php?title=%s&action=edit' % name)
        self.browser.select_form(name = 'editform')
        self.browser['wpTextbox1'] = '{{subst:Member Bio Template}}'
        self.curr_response = self.browser.submit()
        self.curr_html = self.curr_response.read()
