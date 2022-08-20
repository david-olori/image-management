
class Pagination():

    def __init__(self, offsset, pagesize):
        self._offset= offsset
        self.page_size = pagesize

    def setOffsset(self,offsset):
        self._offset = offsset

    def getOffsset(self):
        return self._offset

    def getNext(self):
        next = self._offset + self.page_size;
        self._offset=self._offset + self.page_size;

        return next;

    def getPrevious(self):
        previous = self._offset - self.page_size;
        self._offset = self._offset - self.page_size;
        return previous

    def getPageSize(self):
        return self.page_size;
