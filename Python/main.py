import humanize
from dateutil import parser
from buildbot.status.web import waterfall
from mercurial import subrepo
import test
import gnupg


def main():
    # method called directly
    x = humanize.intcomma(12345)
    print(x)

    # method + ctor called (different import)
    obj = parser.parser()
    obj.parse('Datestring')

    ##vulnerable function called
    vln = waterfall.WaterfallStatusResource()
    vln.body(None)

    ######vulneable function
    ## subrepo() --> _auditsubrepopath() [vulnerable]
    subrepo.subrepo(None, None)

    ########## gnupg
    gnupg.Crypt(None).status()




if '__main__' == __name__:
    main()
    test.filter()
