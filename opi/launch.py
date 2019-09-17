#!/usr/bin/python3
from pydm import Display
from pydm.widgets.related_display_button import PyDMRelatedDisplayButton
from pydm.widgets.label import PyDMLabel

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont

dipole = [
    'PA-RaPSD01:PS-DCLink-1A',
    'PA-RaPSD01:PS-DCLink-1B',
    'PA-RaPSD03:PS-DCLink-2A',
    'PA-RaPSD03:PS-DCLink-2B',
    'PA-RaPSD01:PS-DCLink-3A',
    'PA-RaPSD01:PS-DCLink-3B',
    'PA-RaPSD03:PS-DCLink-4A',
    'PA-RaPSD03:PS-DCLink-4B',
    'PA-RaPSD05:PS-DCLink-1A',
    'PA-RaPSD05:PS-DCLink-1B',
    'PA-RaPSD07:PS-DCLink-2A',
    'PA-RaPSD07:PS-DCLink-2B',
    'PA-RaPSD05:PS-DCLink-3A',
    'PA-RaPSD05:PS-DCLink-3B',
    'PA-RaPSD07:PS-DCLink-4A',
    'PA-RaPSD07:PS-DCLink-4B',
]
quadrupole = [
    'PA-RaPSA01:PS-DCLink-QFAP',
    'PA-RaPSA01:PS-DCLink-QFB',
    'PA-RaPSA03:PS-DCLink-QDAP12'
    'PA-RaPSA04:PS-DCLink-QDB',
    'PA-RaPSA06:PS-DCLink-Q12AA',
    'PA-RaPSA06:PS-DCLink-Q12BB',
    'PA-RaPSA06:PS-DCLink-Q12CC',
    'PA-RaPSA07:PS-DCLink-Q34A',
    'PA-RaPSA07:PS-DCLink-Q34B',
    'PA-RaPSA07:PS-DCLink-Q34C',
]
sextupole = [
    'PA-RaPSB01:PS-DCLink-SDB0',
    'PA-RaPSB04:PS-DCLink-SDB1',
    'PA-RaPSB05:PS-DCLink-SDB2',
    'PA-RaPSB07:PS-DCLink-SDB3',
    'PA-RaPSB03:PS-DCLink-SFB0',
    'PA-RaPSB08:PS-DCLink-SFB1',
    'PA-RaPSB10:PS-DCLink-SFB2',
    'PA-RaPSB04:SI-DCLink-SDA12',
    'PA-RaPSB01:SI-DCLink-SDAP0',
    'PA-RaPSB03:SI-DCLink-SFAP0',
    'PA-RaPSB10:SI-DCLink-SFP12',
    'PA-RaPSB08:SI-DCLink-SDP23',
    'PA-RaPSB05:SI-DCLink-SDA3SFA1',
    'PA-RaPSB07:SI-DCLink-SFA2SDP1',
]


def get_overview_detail(name):
    overview = PyDMRelatedDisplayButton('Overview')
    overview.macros = ['{"P":"' + name + '"}']
    overview.filenames = ['simple.ui']
    overview.openInNewWindow = True
    overview.showIcon = False

    detail = PyDMRelatedDisplayButton('Details')
    detail.macros = ['{"P":"' + name + '"}']
    detail.filenames = ['main.ui']
    detail.openInNewWindow = True
    detail.showIcon = False

    return overview, detail


class Launcher(Display):
    def __init__(self, parent=None, macros=None, **kwargs):
        super().__init__(parent=parent, ui_filename='launch.ui')

        grid_layout = QGridLayout()
        self.scrollAreaWidgetContents.setLayout(grid_layout)

        category_font = QFont()
        category_font.setBold(True)

        i = 0
        lbl = QLabel('Dipoles')
        lbl.setFont(category_font)
        grid_layout.addWidget(lbl, i, 0)
        i += 1

        for name in dipole:
            overview, detail  = get_overview_detail(name)

            grid_layout.addWidget(QLabel(name), i, 0)
            grid_layout.addWidget(overview, i, 1)
            grid_layout.addWidget(detail, i, 2)
            i += 1

        lbl = QLabel('Quadrupoles')
        lbl.setFont(category_font)
        grid_layout.addWidget(lbl, i, 0)
        i += 1
        for name in quadrupole:
            overview, detail  = get_overview_detail(name)

            grid_layout.addWidget(QLabel(name), i, 0)
            grid_layout.addWidget(overview, i, 1)
            grid_layout.addWidget(detail, i, 2)
            i += 1

        lbl = QLabel('Sextupoles')
        lbl.setFont(category_font)
        grid_layout.addWidget(lbl, i, 0)
        i += 1
        for name in sextupole:
            overview, detail  = get_overview_detail(name)

            grid_layout.addWidget(QLabel(name), i, 0)
            grid_layout.addWidget(overview, i, 1)
            grid_layout.addWidget(detail, i, 2)
            i += 1
