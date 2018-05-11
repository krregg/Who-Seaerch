from html.parser import HTMLParser

# Parser for SI Domains
class ParseHTML(HTMLParser):
    """Instantiate the parser and fed it some HTML #####

    parser = ParseHTML()
    html = '<html><head><title>Test</title></head><body><div class="my-style">Parse me!</a></body></html>'
    parser.feed(html)
    print(parser.data)

    """
    def __init__(self):
        HTMLParser.__init__(self)
        self.recording = 0
        self.data = []

    def handle_starttag(self, tag, attributes):
        #print(tag)
        if tag != 'pre':
          return
        if self.recording:
          self.recording += 1
          return
        for name, value in attributes:
          if name == 'class' and value == 'df-raw':
            break
        else:
          return
        self.recording = 1

    def handle_endtag(self, tag):
        if tag == 'pre' and self.recording:
            self.recording -= 1

    def handle_data(self, data):
        if self.recording:
            self.data.append(data)



##### instantiate the parser and fed it some HTML #####
#parser = MyHTMLParser()
#html = '<html><head><title>Test</title></head><body><div class="my-style">Parse me!</a></body></html>'
#parser.feed(html)
#print(parser.data)
#####

