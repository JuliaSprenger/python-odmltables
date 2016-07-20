# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 13:12:21 2016

@author: pick
"""

from PyQt4.QtGui import QApplication

from settings import Settings
from compsectionpages import ChooseFilePage, ChooseSectionsPage, SaveTablePage
from wizutils import OdmltablesWizard


class CompSectionWizard(OdmltablesWizard):
    settings = {}
    settingsfile = 'odmlconverter.conf'
    NUM_PAGES = 3
    (PageChooseFile, PageChooseSections, PageSaveTable) = range(NUM_PAGES)

    def __init__(self, parent=None):
        super(CompSectionWizard, self).__init__('Compare Section Wizard',
                                                parent)

        settings = Settings(self.settingsfile)

        self.setWizardStyle(self.ModernStyle)
        self.setOption(self.HaveHelpButton, True)

        self.setPage(self.PageChooseFile, ChooseFilePage(settings))
        self.setPage(self.PageChooseSections, ChooseSectionsPage(settings))
        self.setPage(self.PageSaveTable, SaveTablePage(settings))

        self.setStartId(self.PageChooseFile)

    def _createHelpMsgs(self):
        msgs = {}
        msgs[self.PageChooseFile] = self.tr("Select an input file using the "
                                            "browser and choose your output "
                                            "file format.")
        msgs[self.PageChooseSections] = self.tr("Choose the Sections you want "
                                                "to compare by moving them "
                                                "from the left to the right "
                                                "widget. You can filter the "
                                                "sections seen in the left "
                                                "tree by using the filter "
                                                "fields in the lower part of "
                                                "the page.")
        msgs[self.PageSaveTable] = self.tr("Select the output file for the "
                                           "table using the browser.")
        msgs[self.NUM_PAGES + 1] = self.tr("Sorry, for this page there is no "
                                           "help available.")
        return msgs


# main ========================================================================
def main():
    import sys

    app = QApplication(sys.argv)
    wiz = CompSectionWizard()
    wiz.show()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
