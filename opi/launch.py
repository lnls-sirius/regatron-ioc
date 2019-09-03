#!/usr/bin/python3
from pydm import Display
from pydm.widgets.related_display_button import PyDMRelatedDisplayButton
from pydm.widgets.label import PyDMLabel

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy
from PyQt5.QtGui import QFont

dipole = [
    'PA-RaPSD01:SI-Reg:PS-B12-1_1A',
    'PA-RaPSD01:SI-Reg:PS-B12-1_1B',
    'PA-RaPSD03:SI-Reg:PS-B12-1_2A',
    'PA-RaPSD03:SI-Reg:PS-B12-1_2B',
    'PA-RaPSD01:SI-Reg:PS-B12-1_3A',
    'PA-RaPSD01:SI-Reg:PS-B12-1_3B',
    'PA-RaPSD03:SI-Reg:PS-B12-1_4A',
    'PA-RaPSD03:SI-Reg:PS-B12-1_4B',
    'PA-RaPSD05:SI-Reg:PS-B12-2_1A',
    'PA-RaPSD05:SI-Reg:PS-B12-2_1B',
    'PA-RaPSD07:SI-Reg:PS-B12-2_2A',
    'PA-RaPSD07:SI-Reg:PS-B12-2_2B',
    'PA-RaPSD05:SI-Reg:PS-B12-2_3A',
    'PA-RaPSD05:SI-Reg:PS-B12-2_3B',
    'PA-RaPSD07:SI-Reg:PS-B12-2_4A',
    'PA-RaPSD07:SI-Reg:PS-B12-2_4B',
]
quadrupole = [
    'PA-RaPSA01:SI-Reg:PS-QFAP',
    'PA-RaPSA01:SI-Reg:PS-QFB',
    'PA-RaPSA03:SI-Reg:PS-QDAP12',
    'PA-RaPSA04:SI-Reg:PS-QDB12',
    'PA-RaPSA06:SI-Reg:PS-Q12_A',
    'PA-RaPSA06:SI-Reg:PS-Q12_B',
    'PA-RaPSA06:SI-Reg:PS-Q12_C',
    'PA-RaPSA07:SI-Reg:PS-Q33_A',
    'PA-RaPSA07:SI-Reg:PS-Q33_B',
    'PA-RaPSA07:SI-Reg:PS-Q33_C',
]
sextupole = [
    'PA-RaPSB01:SI-Reg:PS-SDAP0',
    'PA-RaPSB01:SI-Reg:PS-SDB0',
    'PA-RaPSB03:SI-Reg:PS-SFAP0',
    'PA-RaPSB03:SI-Reg:PS-SFB0',
    'PA-RaPSB04:SI-Reg:PS-SDB1',
    'PA-RaPSB04:SI-Reg:PS-SDA12',
    'PA-RaPSB05:SI-Reg:PS-SDA3FA1',
    'PA-RaPSB05:SI-Reg:PS-SDB2',
    'PA-RaPSB07:SI-Reg:PS-SFA2DP1',
    'PA-RaPSB07:SI-Reg:PS-SDB3',
    'PA-RaPSB08:SI-Reg:PS-SDP23',
    'PA-RaPSB08:SI-Reg:PS-SFB1',
    'PA-RaPSB10:SI-Reg:PS-SFP12',
    'PA-RaPSB10:SI-Reg:PS-SFB2'
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
        super().__init__(parent=parent, ui_filename='launch_.ui')

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
